import dataclasses
import json
import enum
import logging
import pkg_resources
import typing

from simc_support.game_data.Expansion import Expansion
from simc_support.game_data.Instance import Instance, InstanceType, RaidTier
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
from simc_support.game_data.Season import Season

logger = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class _Trinket:
    """1:1 mapping of json to class."""

    id: int  # 193773
    race_mask: int  # 18446744073709551615
    desc: str  # ""
    pad2: str  # ""
    pad1: str  # ""
    pad0: str  # ""
    name: str  # "Spoils of Neltharus"
    id_expansion: int  # 9
    dmg_range: float  # 0.0
    item_limit_category: int  # 0
    duration: int  # 0
    item_damage_modifier: float  # 0.0
    bag_family: int  # 0
    start_quest: int  # 0
    id_lang: int  # 0
    ranged_mod_range: float  # 0.0
    stat_socket_mul_1: float  # 0.0
    stat_socket_mul_2: float  # 0.0
    stat_socket_mul_3: float  # 0.0
    stat_socket_mul_4: float  # 0.0
    stat_socket_mul_5: float  # 0.0
    stat_socket_mul_6: float  # 0.0
    stat_socket_mul_7: float  # 0.0
    stat_socket_mul_8: float  # 0.0
    stat_socket_mul_9: float  # 0.0
    stat_socket_mul_10: float  # 0.0
    stat_alloc_1: int  # 6666
    stat_alloc_2: int  # 0
    stat_alloc_3: int  # 0
    stat_alloc_4: int  # 0
    stat_alloc_5: int  # 0
    stat_alloc_6: int  # 0
    stat_alloc_7: int  # 0
    stat_alloc_8: int  # 0
    stat_alloc_9: int  # 0
    stat_alloc_10: int  # 0
    stackable: int  # 1
    max_count: int  # 0
    req_rep_rank: int  # 0
    id_content_tuning: int  # 0
    sell_price: int  # 571854
    buy_price: int  # 2859270
    unk_3: int  # 1
    unk_2: float  # 1.0
    unk_1: float  # 1.0214999914169312
    flags_1: int  # 524288
    flags_2: int  # 8192
    flags_3: int  # 0
    flags_4: int  # 0
    faction_conv_id: int  # 0
    unk_901_1: int  # 0
    req_spell: int  # 0
    id_curve: int  # 0
    id_name_desc: int  # 0
    unk_l72_1: int  # 0
    id_holiday: int  # 0
    gem_props: int  # 0
    socket_bonus: int  # 0
    totem_category: int  # 0
    map: int  # 0
    area_1: int  # 0
    area_2: int  # 0
    item_set: int  # 0
    id_lock: int  # 0
    page_text: int  # 0
    delay: int  # 0
    req_rep_faction: int  # 0
    req_skill_rank: int  # 0
    req_skill: int  # 0
    class_mask: int  # 65535
    id_artifact: int  # 0
    unk_6: int  # 0
    unk_7: int  # 0
    socket_color_1: int  # 0
    socket_color_2: int  # 0
    socket_color_3: int  # 0
    sheath: int  # 0
    material: int  # 4
    page_mat: int  # 0
    bonding: int  # 1
    damage_type: int  #  0
    stat_type_1: int  #  5
    stat_type_2: int  #  -1
    stat_type_3: int  #  -1
    stat_type_4: int  #  -1
    stat_type_5: int  #  -1
    stat_type_6: int  #  -1
    stat_type_7: int  #  -1
    stat_type_8: int  #  -1
    stat_type_9: int  #  -1
    stat_type_10: int  # -1
    container_slots: int  # 0
    unk_5: int  # 0
    unk_4: int  # 0
    req_level: int  # 58
    inv_type: int  # 12
    quality: int  # 3
    name_en_US: str  # "Spoils of Neltharus"
    name_ko_KR: str  # "넬타루스의 전리품"
    name_fr_FR: str  # "Butin de Neltharus"
    name_de_DE: str  # "Schätze von Neltharus"
    name_zh_CN: str  # "奈萨鲁斯战利品"
    name_es_ES: str  # "Botín de Neltharus"
    name_ru_RU: str  # "Добыча Нелтария"
    name_it_IT: str  # "Spoglie di Neltharus"
    name_pt_PT: str  # "Espólios de Neltharus"
    on_use: bool  # true
    id_encounter: int  # 2501
    id_journal_instance: int  # 1199
    id_map: int  # 2519
    instance_type: typing.Optional[int]  # null
    ilevel: int = 0  # 250


@dataclasses.dataclass
class Trinket:

    _trinket: _Trinket = dataclasses.field(repr=False)

    _bonus_ids: typing.Optional[typing.List[int]] = dataclasses.field(
        default=None, repr=False
    )

    def __post_init__(self):
        self._simc_object = SimcObject(self.translations.US)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(item_id={self.item_id}, full_name='{self.full_name}')"

    @property
    def item_id(self) -> int:
        return self._trinket.id

    @property
    def source(self) -> Source:
        item_mapping = {
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

        if self.item_id in item_mapping.keys():
            return item_mapping[self.item_id]

        instance_mapping = {
            InstanceType.DUNGEON: Source.DUNGEON,
            InstanceType.RAID: Source.RAID,
        }

        if self._trinket.id_journal_instance == 1205:
            return Source.WORLD_BOSS

        if self.instance_type in instance_mapping.keys():
            return instance_mapping[self.instance_type]

        if "Crimson" in self.full_name:
            return Source.PVP

        if "Template" in self.full_name:
            return Source.TEMPLATE

        if "Alchemist" in self.full_name:
            return Source.PROFESSION

        if "Darkmoon Deck" in self.full_name:
            return Source.PROFESSION

        if "Idol of the" in self.full_name:
            return Source.PROFESSION

        return Source.UNKNOWN

    @property
    def itemlevels(self) -> typing.List[int]:

        levels: typing.List[int] = [
            self._trinket.ilevel,
        ]

        # add special cases here
        special_cases = {
            "Spiritual Alchemy Stone": {
                Season.SEASON_1: [
                    self._trinket.ilevel,
                    200,
                    230,
                    262,
                ]
            }
        }

        for season in self.seasons:
            if self.full_name in special_cases.keys():
                levels += special_cases[self.full_name][season]

            if self.source == Source.RAID:
                levels += ItemLevel.ITEM_LEVELS[self.source][season][self.raid_tier]

            if self.source in (Source.CALLING, Source.PVP, Source.DUNGEON):
                levels += ItemLevel.ITEM_LEVELS[self.source][season]

        if self.source == Source.PROFESSION:
            levels += [
                self._trinket.ilevel,
            ]

        levels = sorted(list(set(levels)))

        return levels

    @property
    def role(self) -> typing.Optional[Role]:
        return None

    @property
    def stats(self) -> typing.List[Stat]:
        """Get primary stats from items stat_type information.
        TODO: Can be extended using ItemEffect.id_specialization.
        TODO: what to do with trinkets without primary stats?

        Returns:
            typing.List[Stat]: [description]
        """
        stats = []
        translation = {3: Stat.AGILITY, 4: Stat.STRENGTH, 5: Stat.INTELLECT}
        for i in range(1, 11):
            type_id = getattr(self._trinket, f"stat_type_{i}")
            if type_id in translation:
                stats.append(translation[type_id])
            elif type_id == 71:
                stats.append(Stat.AGILITY)
                stats.append(Stat.STRENGTH)
                stats.append(Stat.INTELLECT)
            elif type_id == 72:
                stats.append(Stat.AGILITY)
                stats.append(Stat.STRENGTH)
            elif type_id == 73:
                stats.append(Stat.AGILITY)
                stats.append(Stat.INTELLECT)
            elif type_id == 74:
                stats.append(Stat.STRENGTH)
                stats.append(Stat.INTELLECT)
        return stats

    @property
    def class_mask(self) -> int:
        return self._trinket.class_mask

    def _get_translations(self, unified_key: str = "name") -> Translation:
        keys = [
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
        d = {}
        for key in keys:
            d[key.split("_")[1]] = getattr(self._trinket, f"{unified_key}_{key}")

        d["BR"] = d["PT"]
        d.pop("PT")

        return Translation(translations=d)

    @property
    def translations(self) -> Translation:
        return self._get_translations()

    @property
    def expansion_id(self) -> int:
        return self._trinket.id_expansion

    @property
    def on_use(self) -> bool:
        return self._trinket.on_use

    @property
    def bonus_ids(self) -> typing.List[int]:
        if self._bonus_ids is not None:
            return self._bonus_ids

        trinkets_with_bonus_id_options = {
            # Unbound Changeling
            178708: [
                6916,  # crit
                6917,  # haste
                6918,  # mastery
                6915,  # crit haste mastery
            ]
        }

        return trinkets_with_bonus_id_options.get(self.item_id, [])

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

    @property
    def expansion(self) -> Expansion:
        return Expansion(self.expansion_id)

    @property
    def instance(self) -> typing.Optional[Instance]:
        if self._trinket.id_journal_instance:
            try:
                return Instance(self._trinket.id_journal_instance)
            except ValueError:
                return Instance.NOT_MAPPED
        return None

    @property
    def instance_type(self) -> InstanceType:
        if self._trinket.instance_type:
            try:
                return InstanceType(self._trinket.instance_type)
            except ValueError:
                pass
        return InstanceType.UNKNOWN

    @property
    def raid_tier(self) -> typing.Optional[RaidTier]:
        if self.instance_type != InstanceType.RAID:
            return None

        if self.instance not in (Instance.VAULT_OF_THE_INCARNATES,):
            return None

        return RaidTier.get_raid_tier_from_encounter_id(self._trinket.id_encounter)

    @property
    def seasons(self) -> typing.List[Season]:
        seasons_ = Season.get_seasons_from_instance(self.instance)
        if seasons_:
            return seasons_

        if self.source == Source.WORLD_BOSS:
            return [Season.SEASON_1]

        # TODO: add more logic to present more trinkets as season trinkets

        return []

    def is_usable_by_class(self, class_id: int) -> bool:
        return bool(self.class_mask & 1 << (class_id - 1))

    def _stringify(self) -> str:
        return f"{self.item_id} {self.name} {self.stats} {self.source}"


def _load_trinkets() -> typing.List[Trinket]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "trinkets.json"))
    ) as f:
        loaded_trinkets = json.load(f)

    _trinkets = [_Trinket(**t) for t in loaded_trinkets]
    trinkets = [Trinket(t) for t in _trinkets]
    return trinkets

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

        if item["id_expansion"] == Expansion.LEGION and source == Source.DUNGEON:
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

    trinkets: typing.List[Trinket] = []
    for trinket in loaded_trinkets:
        if trinket["name"] == "Spoils of Neltharus":
            print(trinket)
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
    for name, data in trinket_metadata.items():
        if data.count > 1:
            logger.debug(f"{name}: {data.count}")
            trinket_block_list += [id for id in data.item_ids if id != data.max_id]

    logger.warning(
        f"Removing {len(trinket_block_list)} trinkets due to duplication. Keeping the highest ID of each."
    )
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


def get_trinket(id_or_full_name: str) -> Trinket:
    for trinket in TRINKETS:
        if str(trinket.item_id) == str(id_or_full_name) or str(
            trinket.full_name
        ) == str(id_or_full_name):
            return trinket
    raise FileNotFoundError("Trinket not found")


def get_versatility_trinket(stat: Stat) -> Trinket:
    """Returns a vers stat stick with the given Stat.

    Returns:
        Trinket -- Versatility Stat stick
    """
    empty_translation = EmptyTranslation()
    empty_translation.US = "Versatility Stat Stick"
    if stat == Stat.AGILITY:
        # "Stat Stick (Versatility)", "142506,bonus_id=607"
        t = get_trinket("142506")
        new_t = Trinket(t._trinket, [607])
        return new_t
    elif stat == Stat.INTELLECT:
        # "Stat Stick (Versatility)", "142507,bonus_id=607"
        t = get_trinket("142507")
        new_t = Trinket(t._trinket, [607])
        return new_t
    elif stat == Stat.STRENGTH:
        # "Stat Stick (Versatility)", "142508,bonus_id=607"
        t = get_trinket("142508")
        new_t = Trinket(t._trinket, [607])
        return new_t
    raise ValueError(f"Unknown stat {stat}. No Versatility trinket available.")
