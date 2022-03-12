import dataclasses
import json
import logging
import pkg_resources
import typing

import simc_support.game_data.ItemLevel as ItemLevel
from simc_support.game_data.Language import (
    EmptyTranslation,
    Translation,
    _get_translations,
)
from simc_support.game_data.Role import Role
from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data.Source import Source
from simc_support.game_data.Stat import Stat
from simc_support.game_data.WowSpec import WowSpec

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Trinket:
    """Creates a Trinket instance

    Args:
        item_id (str): Item ID
        itemlevels (typing.List[int]): item is available at all these itemlevels
        role (Role):
        stats (typing.List[Stat]): primary stats
        translations (Translation): name of the item in all languages
        source (Source): Drop source.
        expansion_id (int): ID of the expansion. e.g. 6-Legion, 8-Shadowlands
        on_use (bool, optional): Is the trinket on use? Defaults to False.
        bonus_ids (typing.List[int]):
    """

    item_id: str
    itemlevels: typing.List[int]
    role: typing.Optional[Role]
    stats: typing.List[Stat]
    class_mask: int
    translations: Translation
    source: Source
    expansion_id: int
    on_use: bool = False
    bonus_ids: typing.List[int] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.itemlevels = sorted(list(set(self.itemlevels)))

        self._simc_object = SimcObject(self.translations.US)

        if isinstance(self.stats, list) or isinstance(self.stats, tuple):
            for element in self.stats:
                if element not in Stat:
                    raise TypeError("One or more provided stats are unknown.")
        else:
            raise TypeError(f"stats: Expected list or tuple. Got {type(self.stats)}")

        if isinstance(self.bonus_ids, list) or isinstance(self.bonus_ids, tuple):
            for bonus in self.bonus_ids:
                if not isinstance(bonus, int):
                    raise TypeError("One or more provided bonus IDs was not an INT.")
        else:
            raise TypeError(
                f"bonus_id: Expected list or tuple. Got {type(self.bonus_ids)}"
            )

    @property
    def full_name(self) -> str:
        return str(self._simc_object.full_name)

    @property
    def simc_name(self) -> str:
        return str(self._simc_object.simc_name)

    @property
    def name(self) -> str:
        return self.translations.US

    @property
    def min_itemlevel(self) -> int:
        return self.itemlevels[0]

    @property
    def max_itemlevel(self) -> int:
        return self.itemlevels[-1]

    def is_usable_by_class(self, class_id: int) -> bool:
        return bool(self.class_mask & 1 << (class_id - 1))

    def _stringify(self) -> str:
        return f"{self.item_id} {self.name} {self.stats} {self.source}"


def _load_trinkets() -> typing.List[Trinket]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "trinkets.json"))
    ) as f:
        loaded_trinkets = json.load(f)

    def _get_stats(item: dict) -> typing.List[Stat]:
        """Get primary stats from items stat_type information.
        TODO: Can be extended using ItemEffect.id_specialization.
        TODO: what to do with trinkets without primary stats?

        Args:
            item (dict): [description]

        Returns:
            typing.List[Stat]: [description]
        """
        stats = []
        translation = {3: Stat.AGILITY, 4: Stat.STRENGTH, 5: Stat.INTELLECT}
        for i in range(1, 11):
            if item[f"stat_type_{i}"] in translation:
                stats.append(translation[item[f"stat_type_{i}"]])
            elif item[f"stat_type_{i}"] == 71:
                stats.append(Stat.AGILITY)
                stats.append(Stat.STRENGTH)
                stats.append(Stat.INTELLECT)
            elif item[f"stat_type_{i}"] == 72:
                stats.append(Stat.AGILITY)
                stats.append(Stat.STRENGTH)
            elif item[f"stat_type_{i}"] == 73:
                stats.append(Stat.AGILITY)
                stats.append(Stat.INTELLECT)
            elif item[f"stat_type_{i}"] == 74:
                stats.append(Stat.STRENGTH)
                stats.append(Stat.INTELLECT)
        return stats

    def _get_itemlevels(item: dict, source: Source) -> typing.List[int]:

        # add special cases here
        if item["name"] == "Spiritual Alchemy Stone":
            return [
                item.get("ilevel", 0),
                200,
                230,
                262,
            ]

        # Tazavesh Dungeon m+ specific itemlevel
        if item["id_journal_instance"] == 1194:
            return ItemLevel.DUNGEON

        if item["id_expansion"] == 6 and source == Source.DUNGEON:
            combined_list = ItemLevel.DUNGEON_MYTHIC_DROPS + ItemLevel.VALOR_UPGRADES
            unique_set = set(combined_list)
            sorted_list = sorted(list(unique_set))
            return sorted_list

        if source == Source.DUNGEON or item["id"] == 190958:
            return ItemLevel.DUNGEON

        if source == Source.RAID and item["id_journal_instance"] == 1190:
            if item["id"] in (
                184027,  # Stone Legion Heraldry
                184028,  # Cabalist's Hymnal
                184030,  # Dreadfire Vessel
                184029,  # Manabound Mirror
                184031,  # Sanguine Vintage
            ):
                return ItemLevel.CASTLE_NATHRIA_ENDBOSSES
            else:
                return ItemLevel.CASTLE_NATHRIA

        if source == Source.RAID and item["id_journal_instance"] == 1193:
            if item["id"] in (
                186421,  # Forbidden Necromantic Tome
                186437,  # Relic of the Frozen Wastes
                186436,  # Resonant Silver Bell
                186438,  # Old Warrior's Soul
            ):
                return ItemLevel.SANCTUM_OF_DOMINATION_ENDBOSSES
            else:
                return ItemLevel.SANCTUM_OF_DOMINATION

        if source == Source.RAID and item["id_journal_instance"] == 1195:
            if item["id"] in (
                188252,  # Chains of Domination
                188254,  # Grim Eclipse
                188255,  # Heart of the Swarm
                188261,  # Intrusive Thoughts
                188253,  # Scars of Fraternal Strife
            ):
                return ItemLevel.SEPULCHER_OF_THE_FIRST_ONES_ENDBOSSES
            else:
                return ItemLevel.SEPULCHER_OF_THE_FIRST_ONES
        if source == source.KORTHIA:
            return ItemLevel.KORTHIA
        if source == Source.PROFESSION:
            return [
                item["ilevel"],
            ]
        if source == Source.PVP:
            if "Aspirant" in item["name"]:
                return [
                    itemlevel
                    for itemlevel in ItemLevel.PVP_HONOR
                    if itemlevel >= item.get("ilevel", 0)
                ]
            else:
                return [
                    itemlevel
                    for itemlevel in ItemLevel.PVP_CONQUEST
                    if itemlevel >= item.get("ilevel", 0)
                ]
        if source == Source.RARE_MOB:
            return ItemLevel.RARE_MOB.get(item["ilevel"], [item["ilevel"]])
        if source == Source.CALLING:
            return ItemLevel.CALLINGS
        if source == Source.ZERETH_MORTIS:
            return ItemLevel.ZERETH_MORTIS

        if item["id"] == 187447:  # Soul Cage Fragment
            return [ItemLevel.WORLD_BOSS_CHAINS_OF_DEVASTATION]
        return [
            item["ilevel"],
        ]

    def _get_bonus_ids(item: dict) -> typing.List[int]:
        ids = []

        # Unbound Changeling
        if item["id"] == 178708:
            # crit
            ids.append(6916)
            # haste
            ids.append(6917)
            # mastery
            ids.append(6918)
            # crit haste mastery
            ids.append(6915)

        return ids

    def _get_source(item: dict) -> Source:
        instance_mapping = {
            1: Source.DUNGEON,
            2: Source.RAID,
        }
        item_mapping = {
            # 175884: Source.PVP,
            # 175921: Source.PVP,
            # 178298: Source.PVP,
            # 178334: Source.PVP,
            # 178386: Source.PVP,
            # 178447: Source.PVP,
            # 181333: Source.PVP,
            # 181335: Source.PVP,
            # 181816: Source.PVP,
            # 184052: Source.PVP,
            # 184053: Source.PVP,
            # 184054: Source.PVP,
            # 184055: Source.PVP,
            # 184056: Source.PVP,
            # 184057: Source.PVP,
            # 184058: Source.PVP,
            # 184059: Source.PVP,
            # 184060: Source.PVP,
            184807: Source.WORLD_DROP,
            182455: Source.RARE_MOB,
            182454: Source.RARE_MOB,
            182453: Source.RARE_MOB,
            182452: Source.RARE_MOB,
            182451: Source.RARE_MOB,
            175729: Source.RARE_MOB,
            175943: Source.PROFESSION,
            175942: Source.PROFESSION,
            175941: Source.PROFESSION,
            171323: Source.PROFESSION,
            173069: Source.PROFESSION,
            173078: Source.PROFESSION,
            173087: Source.PROFESSION,
            173096: Source.PROFESSION,
            175728: Source.CALLING,
            181334: Source.CALLING,
            181357: Source.CALLING,
            181358: Source.CALLING,
            181359: Source.CALLING,
            181360: Source.CALLING,
            181457: Source.CALLING,
            181458: Source.CALLING,
            181459: Source.CALLING,
            181501: Source.CALLING,
            181502: Source.CALLING,
            181503: Source.CALLING,
            181507: Source.CALLING,
            184839: Source.CALLING,
            184840: Source.CALLING,
            184841: Source.CALLING,
            184842: Source.CALLING,
            190958: Source.DUNGEON,  # So'leah's Secret Technique
            190652: Source.DUNGEON,  # Ticking Sack of Terror
        }
        if item["instance_type"]:
            # use handcrafted mapping
            return instance_mapping[item["instance_type"]]
        # print(item)
        if (
            item["ilevel"] >= 200
            and item["map"] == 0
            and item["req_level"] == 60
            and item["quality"] == 3
        ):
            return Source.KORTHIA

        if (
            item["id_expansion"] == 8
            and item["ilevel"] == 226
            and item["req_level"] == 60
            and item["quality"] == 2
        ):
            return Source.ZERETH_MORTIS

        if "Cosmic" in item["name_en_US"] and "Gladiator" in item["name_en_US"]:
            return Source.PVP

        return item_mapping.get(item["id"], Source.UNKNOWN)

    # remove not available legion trinkets
    # id_journal_instance, id_map
    legion_instances: typing.List[typing.Tuple[int, int]] = [
        (740, 1501),  # Black Rook hold
        (800, 1571),  # Court of Stars
        (762, 1466),  # Darkheart Thicket
        (716, 1456),  # Eye of Azshara
        (767, 1458),  # Neltharion's Lair
        (707, 1493),  # Vault of the Wardens
    ]
    id_journal_instances = [i[0] for i in legion_instances]
    id_maps = [i[1] for i in legion_instances]

    # matching id_journal_instance but unmatching id_map
    match_only_id_journal = [
        f"{t['name_en_US']} ({t['id']}) id_map: {t['id_map']}"
        for t in loaded_trinkets
        if t["id_expansion"] == 6
        and t["id_journal_instance"] in id_journal_instances
        and t["id_map"] not in id_maps
    ]
    if match_only_id_journal:
        logger.warning(
            "The following legion trinkets are suspicious and not included! They match a valid id_journal_instance, but don't have the matching id_map."
        )
        logger.warning(match_only_id_journal)
    match_only_id_map = [
        f"{t['name_en_US']} ({t['id']}) id_map: {t['id_map']}"
        for t in loaded_trinkets
        if t["id_expansion"] == 6
        and t["id_journal_instance"] not in id_journal_instances
        and t["id_map"] in id_maps
    ]
    if match_only_id_map:
        logger.warning(
            "The following legion trinkets are suspicious and not included! They match a valid id_map, but don't have the matching id_journal_instance."
        )
        logger.warning(match_only_id_map)

    # remove non-timewalking legion trinkets
    filtered_trinkets = [
        t
        for t in loaded_trinkets
        if t["id_expansion"] != 6
        or t["id_expansion"] == 6
        and t["id_journal_instance"] in id_journal_instances
        and t["id_map"] in id_maps
    ]

    trinkets: typing.List[Trinket] = []
    for trinket in filtered_trinkets:
        source = _get_source(trinket)
        itemlevels = _get_itemlevels(trinket, source)
        if not itemlevels:
            continue
        translations = _get_translations(trinket)
        trinkets.append(
            Trinket(
                item_id=str(trinket["id"]),
                itemlevels=itemlevels,
                role=None,  # TODO
                stats=_get_stats(trinket),
                class_mask=trinket["class_mask"],
                translations=translations,
                source=source,
                on_use=trinket["on_use"],
                bonus_ids=_get_bonus_ids(trinket),
                expansion_id=trinket["id_expansion"],
            )
        )

    # filtering duplicates
    @dataclasses.dataclass
    class MetaData:
        count: int = 0
        item_ids: typing.List[str] = dataclasses.field(default_factory=list)

        @property
        def max_id(self) -> str:
            return max(self.item_ids)

    trinket_metadata: typing.Dict[str, MetaData] = {}
    for trinket in trinkets:
        if trinket.full_name not in trinket_metadata:
            trinket_metadata[trinket.full_name] = MetaData()

        trinket_metadata[trinket.full_name].count += 1
        trinket_metadata[trinket.full_name].item_ids.append(trinket.item_id)

    trinket_block_list: typing.List[str] = []
    for _, data in trinket_metadata.items():
        if data.count > 1:
            # print(f"{name}: {data['count']}")
            trinket_block_list += [id for id in data.item_ids if id != data.max_id]
    # print("to be blocked trinket ids:")
    # print(trinket_block_list)

    unique_trinkets = [t for t in trinkets if t.item_id not in trinket_block_list]

    return unique_trinkets


TRINKETS: typing.List[Trinket] = _load_trinkets()


def get_trinkets_for_spec(wow_spec: WowSpec) -> typing.Tuple[Trinket, ...]:
    """New function to return all available trinkets for a spec

    Arguments:
      wow_spec {WowSpec} -- instance of a WowSpec

    Returns:
      tuple[Trinket] -- Tuple of all Trinkets
    """

    trinkets: typing.List[Trinket] = []
    for trinket in TRINKETS:
        if trinket.is_usable_by_class(wow_spec.wow_class.id):
            if wow_spec.stat in trinket.stats or len(trinket.stats) == 0:
                trinkets.append(trinket)

    return tuple(trinkets)


def get_versatility_trinket(stat: Stat) -> Trinket:
    """Returns a vers stat stick with the given Stat.

    Returns:
        Trinket -- Versatility Stat stick
    """
    empty_translation = EmptyTranslation()
    empty_translation.US = "Versatility Stat Stick"
    all_classes = 2 ** 16 - 1
    if stat == Stat.AGILITY:
        # "Stat Stick (Versatility)", "142506,bonus_id=607"
        return Trinket(
            item_id="142506",
            bonus_ids=[
                607,
            ],
            itemlevels=[ItemLevel.CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.AGILITY,
            ],
            class_mask=all_classes,
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
            expansion_id=-1,
        )
    elif stat == Stat.INTELLECT:
        # "Stat Stick (Versatility)", "142507,bonus_id=607"
        return Trinket(
            item_id="142507",
            bonus_ids=[
                607,
            ],
            itemlevels=[ItemLevel.CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.INTELLECT,
            ],
            class_mask=all_classes,
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
            expansion_id=-1,
        )
    elif stat == Stat.STRENGTH:
        # "Stat Stick (Versatility)", "142508,bonus_id=607"
        return Trinket(
            item_id="142508",
            bonus_ids=[
                607,
            ],
            itemlevels=[ItemLevel.CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.STRENGTH,
            ],
            class_mask=all_classes,
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
            expansion_id=-1,
        )
    raise ValueError(f"Unknown stat {stat}. No Versatility trinket available.")


def get_trinket(id_or_full_name: str) -> Trinket:
    for trinket in TRINKETS:
        if str(trinket.item_id) == str(id_or_full_name) or str(
            trinket.full_name
        ) == str(id_or_full_name):
            return trinket
    raise FileNotFoundError("Trinket not found")
