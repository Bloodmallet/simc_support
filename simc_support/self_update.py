"""
This script updates data_files by using SimulationCrafts casc and dbc extractors.
Basically; execute this script once per patch.

e.g. python self_update.py -s ../../simulationcraft/ --beta --no-load --no-extract
"""
import argparse
import json
import logging
import os
import pathlib
import subprocess
import typing

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

fh = logging.FileHandler("debug.log", encoding="utf-8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

_LOCALES = [
    "en_US",
    "ko_KR",
    "fr_FR",
    "de_DE",
    "zh_CN",
    "es_ES",
    "ru_RU",
    "it_IT",
    "pt_PT",
]

DATA_PATH = "simc_support/game_data/data_files"


def get_spell_names(spells: typing.List[dict], spell_id: int) -> dict:
    for spell in spells:
        if spell_id == spell["id"]:
            spell_names = {"name": spell["name"]}
            for locale in _LOCALES:
                spell_names[f"name_{locale}"] = spell[f"name_{locale}"]
            return spell_names
    raise ValueError(f"No spell with id '{spell_id}' found.")


def merge_information(
    input_dict: dict,
    *,
    filter_function=any,
    match_field="id",
    translation_field="name",
) -> typing.List[dict]:

    logger.debug("Merging")
    result = []
    for i, locale in enumerate(_LOCALES):
        logger.debug(f"  {locale}")
        # prepare
        if i == 0:
            information: dict
            for information in input_dict[locale]:
                if not filter_function(information):
                    continue

                if translation_field:
                    information[f"{translation_field}_{locale}"] = information[
                        translation_field
                    ]

                result.append(information)

        # enrich
        else:
            if not translation_field:
                continue
            for information in result:

                for new_information in input_dict[locale]:
                    if information[match_field] == new_information[match_field]:
                        information[f"{translation_field}_{locale}"] = new_information[
                            translation_field
                        ]

    return result


def handle_arguments() -> argparse.ArgumentParser:
    """Scan user provided arguments and provide the corresponding argparse ArgumentParser.

    Returns:
        argparse.ArgumentParser: [description]
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-s",
        "--simc",
        nargs="?",
        default=None,
        help="Absolute path to your local SimulationCraft version.",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        default=os.path.join(pathlib.Path(__file__).parent.absolute(), "tmp"),
        help="Absolute path to the save location of DB files.",
    )
    parser.add_argument(
        "-w",
        "--wow",
        nargs="?",
        default=None,
        help="Absolute path to your World of Warcaft installation to get hotfixes. E.g. /games/World\ of\ Warcraft/_beta_",
    )
    parser.add_argument(
        "--no-load",
        action="store_true",
        help="Flag disables download from CDN. Instead only already present local files are used.",
    )
    parser.add_argument(
        "--no-extract",
        action="store_true",
        help="Flag disables exrating from db2 files. Instead only already present local files are used.",
    )
    parser.add_argument(
        "--ptr",
        action="store_true",
        help="Download PTR files",
    )
    parser.add_argument(
        "--beta",
        action="store_true",
        help="Download BETA files",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output",
    )
    parser.add_argument(
        "--env",
        nargs="?",
        default=None,
        help="Absolute path to the executable python-env file.",
    )
    return parser


def get_python(env: str = None) -> str:
    """Find and return the appropriate commandline input to use Python 3+

    Returns:
        str: Either "python" or "python3"
    """

    if env:
        return env

    def is_python() -> bool:
        cmd = ["python", "--version"]
        logger.debug(cmd)
        output = subprocess.run(cmd, stdout=subprocess.PIPE)
        return output.stdout.split()[1].startswith(b"3")

    def is_python3() -> bool:
        cmd = ["python3", "--version"]
        logger.debug(cmd)
        output = subprocess.run(cmd, stdout=subprocess.PIPE)
        return output.stdout.split()[1].startswith(b"3")

    if not (is_python() or is_python3()):
        raise SystemError("Python 3 is required.")

    return "python" if is_python() else "python3"


def casc(args: object) -> None:
    """Download all db2 files of all locales described in _LOCALES.

    Args:
        args (object): [description]

    Raises:
        SystemError: If Python 3+ is not available in commandline neither via 'python' nor 'python3'.
    """
    if args.no_load:
        logger.info("Skipping download")
        return
    logger.info("Downloading files (casc)")

    python = get_python(args.env)

    command = [
        python,
        "casc_extract.py",
        "--cdn",
        "-m",
        "batch",
    ]
    if args.ptr:
        command.append("--ptr")
    elif args.beta:
        command.append("--beta")

    for locale in _LOCALES:
        logger.info(locale)
        full_command = command + [
            "--locale",
            locale,
            "-o",
            os.path.join(args.output, locale),
        ]
        logger.debug(full_command)
        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.join(args.simc, "casc_extract"),
        )
        # ['python', 'casc_extract.py', '--cdn', '-m', 'batch', '--locale', 'pt_PT', '-o', 'D:\\Programme\\simc_support\\simc_support\\tmp\\pt_PT']
        while True:
            output = process.stdout.readline()
            if output == b"" and process.poll() is not None:
                break
            if output:
                logger.debug(output.strip().decode("ascii"))
        rc = process.poll()
        if rc != 0:
            logger.error(
                f"Error occured while loading {locale}. {process.communicate()[1]}"
            )

    logger.info("Downloaded files")


def get_compiled_data_path(args: object, locale: str) -> str:
    return os.path.join(args.output, "compiled", locale)


def dbc(args: object, files: typing.List[str]) -> None:
    """Extract and transforms files into JSON format.
    TODO: parallelize this

    Args:
        args (object): [description]
        files (typing.List[str]): [description]
    """
    if args.no_extract:
        logger.info("Skipping extraction")
        return
    logger.info("Extracting files (dbc)")

    python = get_python(args.env)

    wow_versions = os.listdir(os.path.join(args.output, _LOCALES[0]))
    logger.debug(f" Detected wow versions: {wow_versions}")
    wow_version = wow_versions[-1]

    command = [
        python,
        "dbc_extract.py",
        "-b",
        wow_version,
        "-t",
        "json",
    ]
    if args.wow:
        command.append("--hotfix")
        command.append(os.path.join(args.wow, "Cache/ADB/enUS/DBCache.bin"))

    for file in files:
        for locale in _LOCALES:
            logger.info(f"{file} {locale}")

            cmd = command + [
                "-p",
                os.path.join(args.output, locale, wow_version, "DBFilesClient"),
                file,
            ]

            pathlib.Path(os.path.join(get_compiled_data_path(args, locale))).mkdir(
                parents=True, exist_ok=True
            )

            logger.debug(cmd)
            process = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=os.path.join(args.simc, "dbc_extract3"),
            )
            if process.returncode != 0:
                logger.error(
                    f"Error occured while extracting {file} {locale}. {process.stderr.decode()}"
                )
            else:
                with open(
                    os.path.join(get_compiled_data_path(args, locale), f"{file}.json"),
                    "wb",
                ) as f:
                    f.write(process.stdout)


def update_trinkets(args: object) -> None:
    """Update data_files/trinkets.json

    Args:
        args (object): [description]

    Returns:
        None
    """
    logger.info("Update trinkets")

    ITEMSPARSE = "ItemSparse"
    ITEMXITEMEFFECT = "ItemXItemEffect"
    ITEMEFFECT = "ItemEffect"
    JOURNAL_ENCOUNTER_ITEM = "JournalEncounterItem"
    JOURNAL_ENCOUNTER = "JournalEncounter"
    JOURNAL_INSTANCE = "JournalInstance"
    MAP = "Map"

    WHITELIST = [
        181457,
        184842,
    ]

    def is_trinket(item: dict) -> bool:
        """See https://github.com/simulationcraft/simc/blob/shadowlands/engine/dbc/data_enums.hh#L335"""
        return item.get("inv_type") == 12

    def is_gte_uncommon(item: dict) -> bool:
        """See https://github.com/simulationcraft/simc/blob/shadowlands/engine/dbc/data_enums.hh#L369"""
        return item.get("quality") >= 2

    def is_shadowlands(item: dict) -> bool:
        """Tests for itemlevel and character level requirement."""

        def is_expansion(item: dict) -> bool:
            """Checks expansion id."""
            return item["id_expansion"] == 8

        def is_gte_level(item: dict) -> bool:
            """An Expansion starts at the last possible character level of the previous one."""
            return item.get("req_level") >= 50

        def is_gte_ilevel(item: dict) -> bool:
            """Value of normal Dungeon items at level 50."""
            return item.get("ilevel") >= 148

        # Unbound Changeling is somehow available for lvl 1
        return is_expansion(item) or is_gte_ilevel(item)  # and is_gte_level(item)

    def is_legion(item: dict) -> bool:
        """Tests for itemlevel and character level requirement."""

        def is_expansion(item: dict) -> bool:
            """Checks expansion id."""
            return item["id_expansion"] == 6

        return is_expansion(item)

    def is_whitelisted(item: dict) -> bool:
        return item.get("id") in WHITELIST or item.get("name") in WHITELIST

    def is_approved(item: dict) -> bool:
        is_a_good_one = (
            is_trinket(item)
            and is_gte_uncommon(item)
            and (is_shadowlands(item) or is_legion(item))
            or is_whitelisted(item)
        )

        return is_a_good_one

    dbc(
        args,
        [
            ITEMEFFECT,
            ITEMSPARSE,
            ITEMXITEMEFFECT,
            JOURNAL_ENCOUNTER,
            JOURNAL_ENCOUNTER_ITEM,
            JOURNAL_INSTANCE,
            MAP,
        ],
    )

    data = {}

    for locale in _LOCALES:
        with open(
            os.path.join(get_compiled_data_path(args, locale), f"{ITEMSPARSE}.json"),
            "r",
        ) as f:
            items = json.load(f)

        data[locale] = [item for item in items if is_approved(item)]

    # load itemeffect table
    with open(
        os.path.join(get_compiled_data_path(args, _LOCALES[0]), f"{ITEMEFFECT}.json"),
        "r",
    ) as f:
        _itemeffects = json.load(f)

    itemeffects = {}
    for effect in _itemeffects:
        itemeffects[effect["id"]] = effect

    logger.debug(itemeffects)

    # load ItemXItemEffect table
    with open(
        os.path.join(
            get_compiled_data_path(args, _LOCALES[0]), f"{ITEMXITEMEFFECT}.json"
        ),
        "r",
    ) as f:
        _itemxitemeffects = json.load(f)

    itemxitemeffects = {}
    for effect in _itemxitemeffects:
        if effect["id_parent"] in itemxitemeffects:
            itemxitemeffects[effect["id_parent"]].append(
                itemeffects[effect["id_item_effect"]]
            )
        else:
            itemxitemeffects[effect["id_parent"]] = [
                itemeffects[effect["id_item_effect"]]
            ]

    def is_on_use(item_id: int) -> bool:
        if item_id in itemxitemeffects:
            return any(
                map(lambda row: row["trigger_type"] == 0, itemxitemeffects[item_id])
            )
        return False

    def get_spec_mask(item_id: int) -> list:
        """Turns out...trinkets add only 0 as specialization ids...worthless approach.

        Args:
            item_id (int): [description]

        Returns:
            list: [description]
        """
        mask = []
        for effect in itemeffects:
            if item_id == effect["id_parent"]:
                mask.append(effect["id_specialization"])
        if len(mask) == 0:
            logger.info(f"No specializations found for {item_id}")
        else:
            logger.info(f"Specializations found for {item_id}: {mask}")
        return mask

    # load encounter_items table
    with open(
        os.path.join(
            get_compiled_data_path(args, _LOCALES[0]), f"{JOURNAL_ENCOUNTER_ITEM}.json"
        ),
        "r",
    ) as f:
        encounter_items = json.load(f)

    def get_id_encounter(item_id: int) -> typing.Optional[int]:
        for item in encounter_items:
            if item["id_item"] == item_id:
                return item["id_encounter"]
        return None

    # load encounter table
    with open(
        os.path.join(
            get_compiled_data_path(args, _LOCALES[0]), f"{JOURNAL_ENCOUNTER}.json"
        ),
        "r",
    ) as f:
        encounters = json.load(f)

    def id_journal_instance(id_encounter: int) -> typing.Optional[int]:
        if not id_encounter:
            return None
        for encounter in encounters:
            if encounter["id"] == id_encounter:
                return encounter["id_journal_instance"]
        return None

    # load instance table
    with open(
        os.path.join(
            get_compiled_data_path(args, _LOCALES[0]), f"{JOURNAL_INSTANCE}.json"
        ),
        "r",
    ) as f:
        instances = json.load(f)

    def get_id_map(id_journal_instance: int) -> typing.Optional[int]:
        if not id_journal_instance:
            return None
        for instance in instances:
            if instance["id"] == id_journal_instance:
                return instance["map"]
        return None

    # load map table
    with open(
        os.path.join(get_compiled_data_path(args, _LOCALES[0]), f"{MAP}.json"),
        "r",
    ) as f:
        maps = json.load(f)

    def get_instance_type(id_map: int) -> typing.Optional[int]:
        if not id_map:
            return None
        for map in maps:
            if map["id"] == id_map:
                return map["instance_type"]
        return None

    trinkets = merge_information(data, filter_function=is_approved)
    for trinket in trinkets:
        trinket["on_use"] = is_on_use(trinket["id"])
        trinket["id_encounter"] = get_id_encounter(trinket["id"])
        trinket["id_journal_instance"] = id_journal_instance(trinket["id_encounter"])
        trinket["id_map"] = get_id_map(trinket["id_journal_instance"])
        trinket["instance_type"] = get_instance_type(trinket["id_map"])

    logger.debug(trinkets)

    with open(os.path.join(DATA_PATH, "trinkets.json"), "w", encoding="utf-8") as f:
        json.dump(trinkets, f, ensure_ascii=False)

    logger.info(f"Updated {len(trinkets)} trinkets")


def update_wow_classes(args: object) -> None:
    logger.info("Update WowClasses")

    # TODO: class - race connection can be established via ChrClassRaceSex table
    CHRCLASSES = "ChrClasses"
    dbc(
        args,
        [
            CHRCLASSES,
        ],
    )
    data = {}

    for locale in _LOCALES:
        with open(
            os.path.join(get_compiled_data_path(args, locale), f"{CHRCLASSES}.json"),
            "r",
        ) as f:
            data[locale] = json.load(f)

    wow_classes = []

    wow_classes = merge_information(data, translation_field="name_lang")

    with open(os.path.join(DATA_PATH, "wow_classes.json"), "w", encoding="utf-8") as f:
        json.dump(wow_classes, f, ensure_ascii=False)

    logger.info(f"Updated {len(wow_classes)} WowClasses")


def update_covenants(args: object) -> None:
    logger.info("Update covenants")

    COVENANTS = "Covenant"

    dbc(args, [COVENANTS])
    data = {}
    for locale in _LOCALES:
        with open(
            os.path.join(get_compiled_data_path(args, locale), f"{COVENANTS}.json"),
            "r",
        ) as f:
            data[locale] = json.load(f)

    covenants = merge_information(data)

    with open(os.path.join(DATA_PATH, "covenants.json"), "w", encoding="utf-8") as f:
        json.dump(covenants, f, ensure_ascii=False)

    logger.info(f"Updated {len(covenants)} covenants")


# SoulbindConduit, SoulbindConduitItem, SoulbindConduitRank for the conduit stuff


def update_soul_binds(args: object) -> None:
    logger.info("Update soul binds")

    SOULBINDS = "Soulbind"
    TALENTS = "GarrTalent"
    RANKS = "GarrTalentRank"
    SPELLS = "SpellName"

    dbc(
        args,
        [
            SOULBINDS,
            TALENTS,
            RANKS,
            SPELLS,
        ],
    )
    data = {SOULBINDS: {}, TALENTS: {}, RANKS: {}, SPELLS: {}}
    for key in data:
        for locale in _LOCALES:
            with open(
                os.path.join(get_compiled_data_path(args, locale), f"{key}.json"),
                "r",
            ) as f:
                data[key][locale] = json.load(f)

    soul_binds = merge_information(data[SOULBINDS])

    talents = merge_information(data[TALENTS])

    ranks = merge_information(data[RANKS], translation_field=None)

    def get_spell_id(talent: dict) -> int:
        for rank in ranks:
            if rank["id_parent"] == talent["id"]:
                return rank["id_spell"]

    logger.debug("Enriching talent information")
    # enrich with talents
    talent_spells = []
    for soul_bind in soul_binds:
        logger.debug(f"Soul Bind {soul_bind['id']}")
        soul_bind["talents"] = [
            talent
            for talent in talents
            if talent["id_parent"] == soul_bind["id_garr_talent_tree"]
        ]
        for talent in soul_bind["talents"]:
            logger.debug(f"  Talent {talent['id']}")
            talent["spell_id"] = get_spell_id(talent)
            talent_spells.append(talent["spell_id"])

    # enrich talents with spells and spell translations
    def is_relevant_spell(information: dict) -> bool:
        return information["id"] in talent_spells

    spells = merge_information(data[SPELLS], filter_function=is_relevant_spell)

    for soul_bind in soul_binds:
        logger.debug(f"Soul Bind {soul_bind['id']}")
        for talent in soul_bind["talents"]:
            if talent["spell_id"] == 0:
                continue
            # node names are overwritten by their spells
            spell_names = get_spell_names(spells, talent["spell_id"])
            for key in spell_names:
                talent[key] = spell_names[key]

    with open(os.path.join(DATA_PATH, "soul_binds.json"), "w", encoding="utf-8") as f:
        json.dump(soul_binds, f, ensure_ascii=False)

    logger.info(f"Updated {len(soul_binds)} soul binds")


def update_legendaries(args: object) -> None:
    logger.info("Update legendaries")

    RUNEFORGELEGENDARYABILITY = "RuneforgeLegendaryAbility"
    SPECSETMEMBER = "SpecSetMember"

    dbc(
        args,
        [
            RUNEFORGELEGENDARYABILITY,
            SPECSETMEMBER,
        ],
    )
    data = {
        RUNEFORGELEGENDARYABILITY: {},
        SPECSETMEMBER: {},
    }
    for key in data:
        for locale in _LOCALES:
            with open(
                os.path.join(get_compiled_data_path(args, locale), f"{key}.json"),
                "r",
            ) as f:
                data[key][locale] = json.load(f)

    legendaries = merge_information(data[RUNEFORGELEGENDARYABILITY])
    specs = data[SPECSETMEMBER][_LOCALES[0]]

    for legendary in legendaries:
        legendary["spec_ids"] = list(
            [
                spec["id_spec"]
                for spec in specs
                if spec["id_parent"] == legendary["id_spec_set"]
            ]
        )

    with open(os.path.join(DATA_PATH, "legendaries.json"), "w", encoding="utf-8") as f:
        json.dump(legendaries, f, ensure_ascii=False)

    logger.info(f"Updated {len(legendaries)} legendaries")


def update_conduits(args: object) -> None:
    logger.info("Update conduits")

    CONDUIT = "SoulbindConduit"
    # ITEM = "SoulbindConduitItem"
    RANK = "SoulbindConduitRank"
    SPECSETMEMBER = "SpecSetMember"
    SPELLS = "SpellName"

    WHITELIST = []

    dbc(
        args,
        [
            CONDUIT,
            RANK,
            SPECSETMEMBER,
            SPELLS,
        ],
    )
    data = {
        CONDUIT: {},
        RANK: {},
        SPECSETMEMBER: {},
        SPELLS: {},
    }
    for key in data:
        for locale in _LOCALES:
            with open(
                os.path.join(get_compiled_data_path(args, locale), f"{key}.json"),
                "r",
            ) as f:
                data[key][locale] = json.load(f)

    conduits = merge_information(data[CONDUIT], translation_field=None)
    ranks = merge_information(data[RANK], translation_field=None)
    specs = data[SPECSETMEMBER][_LOCALES[0]]

    def _get_spell_id(conduit: dict) -> typing.Optional[int]:
        for rank in ranks:
            if rank["id_parent"] == conduit["id"]:
                return rank["id_spell"]
        return None

    def _get_ranks(conduit: dict) -> typing.List[int]:
        return list(
            [rank["rank"] for rank in ranks if rank["id_parent"] == conduit["id"]]
        )

    spell_ids = []
    almost_tank_spec_ids = [
        251,
        252,
        577,
        102,
        103,
        105,
        269,
        270,
        70,
        65,
        71,
        72,
    ]
    tank_ids = [
        250,
        581,
        104,
        268,
        66,
        73,
    ]
    for conduit in conduits:
        # id_spec_set is the id of a spec group, can be only one
        # id_parent is the id of a class
        conduit["spec_ids"] = [
            spec["id_spec"]
            for spec in specs
            if spec["id_parent"] == conduit["id_spec_set"]
        ]
        # special case: Adaptive Armor Fragment (id=284, spell_id=357902)
        # is available to all non-tank specs of tank-classes
        if (
            any([spec_id in tank_ids for spec_id in conduit["spec_ids"]])
            and conduit["id"] == 284
        ):
            conduit["spec_ids"] += almost_tank_spec_ids

        conduit["spell_id"] = _get_spell_id(conduit)
        conduit["ranks"] = sorted(_get_ranks(conduit))
        spell_ids.append(conduit["spell_id"])

    # enrich talents with spells and spell translations
    def is_relevant_spell(spell: dict) -> bool:
        return spell["id"] in spell_ids

    spells = merge_information(data[SPELLS], filter_function=is_relevant_spell)

    for conduit in conduits:
        try:
            translations = get_spell_names(spells, conduit["spell_id"])
        except ValueError:
            translations = {"name": None}
            for locale in _LOCALES:
                translations[f"name_{locale}"] = None
        for key in translations:
            conduit[key] = translations[key]

    def _is_conduit(conduit: dict) -> bool:
        return (
            conduit["name"]
            and len(conduit["ranks"]) == 15
            and len(conduit["spec_ids"]) > 0
            or conduit["id"] in WHITELIST
        )

    conduits = list([conduit for conduit in conduits if _is_conduit(conduit)])

    with open(os.path.join(DATA_PATH, "conduits.json"), "w", encoding="utf-8") as f:
        json.dump(conduits, f, ensure_ascii=False)

    logger.info(f"Updated {len(conduits)} conduits")


def update_talents(args: object) -> None:
    logger.info("Update talents")

    TALENTS = "Talent"
    SPELLS = "SpellName"

    dbc(args, [TALENTS, SPELLS])
    data = {
        TALENTS: {},
        SPELLS: {},
    }
    for key in data:
        for locale in _LOCALES:
            with open(
                os.path.join(get_compiled_data_path(args, locale), f"{key}.json"),
                "r",
            ) as f:
                data[key][locale] = json.load(f)

    talents = data[TALENTS][_LOCALES[0]]

    spell_ids = list([talent["id_spell"] for talent in talents])
    spells = merge_information(
        data[SPELLS], filter_function=lambda spell: spell["id"] in spell_ids
    )

    for talent in talents:
        spell_names = get_spell_names(spells, talent["id_spell"])
        for key in spell_names:
            talent[key] = spell_names[key]

    with open(os.path.join(DATA_PATH, "talents.json"), "w", encoding="utf-8") as f:
        json.dump(talents, f, ensure_ascii=False)

    logger.info(f"Updated {len(talents)} talents")


def update_shards_of_dominations(args: object) -> None:
    logger.info("Update Shards of Dominations")

    ITEM_SPARSE = "ItemSparse"
    GEM_PROPERTIES = "GemProperties"
    SPELL_ITEM_ENCHANTMENT = "SpellItemEnchantment"
    SPELL_NAME = "SpellName"
    SPELL_MISC = "SpellMisc"

    dbc(
        args,
        [
            ITEM_SPARSE,
            GEM_PROPERTIES,
            SPELL_ITEM_ENCHANTMENT,
            SPELL_NAME,
            SPELL_MISC,
        ],
    )
    data = {
        ITEM_SPARSE: {},
        GEM_PROPERTIES: {},
        SPELL_ITEM_ENCHANTMENT: {},
        SPELL_NAME: {},
        SPELL_MISC: {},
    }

    for key in data:
        for locale in _LOCALES:
            with open(
                os.path.join(get_compiled_data_path(args, locale), f"{key}.json"),
                "r",
            ) as f:
                data[key][locale] = json.load(f)

    def is_shard(entry: dict) -> bool:
        not_a_shard = [
            187120,
            186773,
        ]
        if entry["id"] in not_a_shard:
            return False
        return (
            entry["id_expansion"] == 7
            and entry["ilevel"] >= 255
            and entry["quality"] == 4
            and entry["req_level"] >= 50
            and entry["gem_props"] != 0
        )

    shards = list(filter(is_shard, data[ITEM_SPARSE]["en_US"]))

    shard_ids = list(set([shard["gem_props"] for shard in shards]))
    logger.info(f"shard_ids ({len(shard_ids)}): {shard_ids}")

    def is_relevant_gem_prop(entry: dict) -> bool:
        return entry["id"] in shard_ids

    relevant_gems = list(filter(is_relevant_gem_prop, data[GEM_PROPERTIES]["en_US"]))

    enchant_ids = [gem_prop["id_enchant"] for gem_prop in relevant_gems]
    logger.info(f"enchant_ids ({len(enchant_ids)}): {enchant_ids}")

    def is_shard_enchantment(entry: dict) -> bool:
        return entry["id"] in enchant_ids

    # gem_properties = data[GEM_PROPERTIES]
    spell_item_enchantments = list(
        filter(is_shard_enchantment, data[SPELL_ITEM_ENCHANTMENT]["en_US"])
    )

    properties = ("id_property_1", "id_property_2", "id_property_3")

    cutoff = 0
    # logger.info(json.dumps(spell_item_enchantments))
    shard_enchantment_ids = []
    for prop in properties:
        shard_enchantment_ids += [
            enchant[prop]
            for enchant in spell_item_enchantments
            if enchant[prop] > cutoff
        ]
    shard_enchantment_ids = list(set(shard_enchantment_ids))
    logger.info(
        f"shard_enchantment_ids ({len(shard_enchantment_ids)}): {shard_enchantment_ids}"
    )

    def is_shard_spell(entry: dict) -> bool:
        return entry["id"] in shard_enchantment_ids

    spell_names = merge_information(data[SPELL_NAME], filter_function=is_shard_spell)

    names = [spell["name"] for spell in spell_names]
    logger.info(f"names ({len(names)}): {names}")

    def is_misc(entry: dict) -> dict:
        return entry["id_parent"] in shard_enchantment_ids

    spell_miscs = list(filter(is_misc, data[SPELL_MISC]["en_US"]))

    for shard in shards:
        for gem in relevant_gems:
            if shard["gem_props"] == gem["id"]:
                shard["id_enchant"] = gem["id_enchant"]
        for enchant in spell_item_enchantments:
            if shard["id_enchant"] == enchant["id"]:
                for prop in properties:
                    shard[prop] = enchant[prop]
        for name in spell_names:
            if name["id"] in [shard[prop] for prop in properties]:
                for key in name.keys():
                    if "name_" in key:
                        shard[key] = name[key]
        for misc in spell_miscs:
            if misc["id_parent"] in [shard[prop] for prop in properties]:
                shard["school"] = misc["school"]
        # cleanse unwanted keys
        unwanted_keys = [
            "desc",
            "pad2",
            "pad1",
            "pad0",
            "dmg_range",
            "item_limit_category",
            "duration",
            "item_damage_modifier",
            "bag_family",
            "ranged_mod_range",
            "stackable",
            "max_count",
            "id_content_tuning",
            "sell_price",
            "buy_price",
            "unk_3",
            "unk_2",
            "unk_1",
            "flags_1",
            "flags_2",
            "flags_3",
            "flags_4",
            "faction_conv_id",
            "unk_901_1",
            "req_spell",
            "id_curve",
            # "id_name_desc",
            "unk_l72_1",
            "id_holiday",
            "socket_bonus",
            "totem_category",
            "map",
            "area_1",
            "area_2",
            "item_set",
            "id_lock",
            "start_quest",
            "page_text",
            "delay",
            "req_rep_faction",
            "req_skill_rank",
            "req_skill",
            "id_artifact",
            "unk_6",
            "unk_7",
            "socket_color_1",
            "socket_color_2",
            "socket_color_3",
            "sheath",
            "page_mat",
            "id_lang",
            "bonding",
            "damage_type",
            "container_slots",
            "req_rep_rank",
            "unk_5",
            "unk_4",
            "inv_type",
        ]
        for i in range(1, 11):
            unwanted_keys += [
                f"stat_socket_mul_{i}",
                f"stat_alloc_{i}",
                f"stat_type_{i}",
            ]
        for key in unwanted_keys:
            del shard[key]

    # save data to file
    with open(
        os.path.join(DATA_PATH, "damnation_shards.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(shards, f, ensure_ascii=False)

    logger.info(f"Updated {len(shards)} DamnationShards")


def main() -> None:
    args = handle_arguments().parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
    casc(args)
    update_trinkets(args)
    # update_wow_classes(args)
    # update_covenants(args)
    # update_soul_binds(args)
    # update_legendaries(args)
    # update_conduits(args)
    # update_talents(args)
    # update_shards_of_dominations(args)

    logger.debug("self_update done")


if __name__ == "__main__":
    main()
