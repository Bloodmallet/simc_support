"""
This script updates data_files by using SimulationCrafts casc and dbc extractors.
Basically; execute this script once per patch.

e.g. python self_update.py -s ../../simulationcraft/ --beta --no-load --no-extract
"""
import json
import logging
import os
import typing
from update.extractor import Extractor
from update.utils import (
    ArgsObject,
    handle_arguments,
    dbc,
    casc,
    get_compiled_data_path,
    collect_localizations,
    safely_convert_to,
)
from update.talents import TalentLoader
from update.trinkets import TrinketExtractor

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

fh = logging.FileHandler("debug.log", encoding="utf-8", mode="w")
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


def update_trinkets(args: ArgsObject) -> None:
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
        return item.get("quality", -1) >= 2

    def is_shadowlands(item: dict) -> bool:
        """Tests for itemlevel and character level requirement."""

        def is_expansion(item: dict) -> bool:
            """Checks expansion id."""
            return item["id_expansion"] == 8

        def is_gte_level(item: dict) -> bool:
            """An Expansion starts at the last possible character level of the previous one."""
            return item.get("req_level", -1) >= 50

        def is_gte_ilevel(item: dict) -> bool:
            """Value of normal Dungeon items at level 50."""
            return item.get("ilevel", -1) >= 148

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

    trinkets = collect_localizations(data, filter_function=is_approved)
    for trinket in trinkets:
        trinket["on_use"] = is_on_use(safely_convert_to(trinket["id"], int, -1))
        trinket["id_encounter"] = get_id_encounter(
            safely_convert_to(trinket["id"], int, -1)
        )
        trinket["id_journal_instance"] = id_journal_instance(
            safely_convert_to(trinket["id_encounter"], int, -1)
        )
        trinket["id_map"] = get_id_map(
            safely_convert_to(trinket["id_journal_instance"], int, -1)
        )
        trinket["instance_type"] = get_instance_type(
            safely_convert_to(trinket["id_map"], int, -1)
        )

    logger.debug(trinkets)

    with open(os.path.join(DATA_PATH, "trinkets.json"), "w", encoding="utf-8") as f:
        json.dump(trinkets, f, ensure_ascii=False)

    logger.info(f"Updated {len(trinkets)} trinkets")


def update_wow_classes(args: ArgsObject) -> None:
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

    wow_classes = collect_localizations(data, translation_field="name_lang")

    with open(os.path.join(DATA_PATH, "wow_classes.json"), "w", encoding="utf-8") as f:
        json.dump(wow_classes, f, ensure_ascii=False)

    logger.info(f"Updated {len(wow_classes)} WowClasses")


def update_legendaries(args: ArgsObject) -> None:
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

    legendaries = collect_localizations(data[RUNEFORGELEGENDARYABILITY])
    specs = data[SPECSETMEMBER][_LOCALES[0]]

    for legendary in legendaries:

        legendary["spec_ids"] = list(
            [
                safely_convert_to(spec["id_spec"], int, -1)
                for spec in specs
                if spec["id_parent"] == legendary["id_spec_set"]
            ]
        )

    with open(os.path.join(DATA_PATH, "legendaries.json"), "w", encoding="utf-8") as f:
        json.dump(legendaries, f, ensure_ascii=False)

    logger.info(f"Updated {len(legendaries)} legendaries")


def main() -> None:
    args = handle_arguments()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    casc(args)

    updates: typing.List[typing.Callable[[ArgsObject], None]] = [
        # update_trinkets,
        # update_wow_classes,
        # update_legendaries,
    ]
    for update in updates:
        update(args)

    extractors: typing.List[typing.Type[Extractor]] = [
        # TalentLoader,
        TrinketExtractor
    ]
    for extractor in extractors:
        extractor(args).extract()

    logger.debug("self_update done")


if __name__ == "__main__":
    main()
