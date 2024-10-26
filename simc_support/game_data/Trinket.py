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
    # unk_3: int  # 1
    unk_2: float  # 1.0
    unk_1: float  # 1.0214999914169312
    flags_1: int  # 524288
    flags_2: int  # 8192
    flags_3: int  # 0
    flags_4: int  # 0
    flags_5: int  # 0
    faction_conv_id: int  # 0
    id_modified_crafting_reagent_item: int  # 0
    req_spell: int  # 0
    id_curve: int  # 0
    id_name_desc: int  # 0
    # unk_l72_1: int  # 0
    id_holiday: int  # 0
    gem_props: int  # 0
    socket_bonus: int  # 0
    totem_category: int  # 0
    map: int  # 0
    area_1: int  # 0
    area_2: int  # 0
    item_set: int  # 0
    id_lock: int  # 0
    # page_text: int  # 0
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
    vendor_stack: int  # = -1  # no clue
    id_xmog_holiday: int  # = -1  # no clue
    id_page: int  # = -1
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
            # Dragonflight start
            200217: Source.RARE_MOB,  # Blazing Essence
            200563: Source.RARE_MOB,  # Primal Ritual Shell
            200859: Source.RARE_MOB,  # Seasoned Hunter's Trophy
            198407: Source.WORLD_QUEST,  # Azure Arcanic Amplifier
            198542: Source.WORLD_QUEST,  # Shikaari Huntress' Arrowhead
            198489: Source.WORLD_QUEST,  # Dreamscape Prism
            204810: Source.WORLD_QUEST,  # Drogbar Rocks
            204811: Source.WORLD_QUEST,  # Drogbar Stones
            204386: Source.WORLD_QUEST,  # Pocket Darkened Elemental Core
            204387: Source.WORLD_QUEST,  # Buzzing Orb Core
            204388: Source.WORLD_QUEST,  # Draconic Cauterizing Magma
            204714: Source.WORLD_QUEST,  # Satchel of Healing Spores
            204728: Source.WORLD_QUEST,  # Friendship Censer
            204736: Source.WORLD_QUEST,  # Heatbound Medallion
            204901: Source.WORLD_QUEST,  # Firecaller's Focus
            205191: Source.WORLD_QUEST,  # Underlight Globe
            205192: Source.WORLD_QUEST,  # Volatile Crystal Shard
            205193: Source.WORLD_QUEST,  # Sturdy Deepflayer Scute
            205194: Source.WORLD_QUEST,  # Fractured Crystalspine Quill
            205195: Source.WORLD_QUEST,  # Drakeforged Magma Charm
            205196: Source.WORLD_QUEST,  # Zaqali Hand Cauldron
            205200: Source.WORLD_QUEST,  # Stirring Twilight Ember
            205201: Source.WORLD_QUEST,  # Smoldering Howler Horn
            205229: Source.WORLD_QUEST,  # Magma Serpent Lure
            205262: Source.WORLD_QUEST,  # Magmaclaw Lure
            205276: Source.WORLD_QUEST,  # Deepflayer Lure
            192797: Source.CALLING,  # Gral's Discarded Tooth
            198695: Source.CALLING,  # Bottomless Reliquary Satchel
            # need to flag these because of timewalking :s
            133252: Source.DUNGEON,  # Rainsong
            133246: Source.DUNGEON,  # Heart of Thunder
            # Grim Batol is somehow not getting detected
            133304: Source.DUNGEON,  # Gale of Shadows
            133282: Source.DUNGEON,  # Skardyn's Grace
            133300: Source.DUNGEON,  # Mark of Khardros
            # need to somehow double check these
            215174: Source.DELVE,  # Concoction: Kiss of Death
            215171: Source.DELVE,  # Fungal Friend Flute
            215169: Source.DELVE,  # Everburning Lantern
            215178: Source.DELVE,  # Shadow-Binding Ritual Knife
            225648: Source.DELVE,  # Candle Confidant
            225656: Source.DELVE,  # Goldenglow Censer
            225651: Source.DELVE,  # Kaheti Shadeweaver's Emblem
            225649: Source.DELVE,  # Quickwick Candlestick
            225668: Source.DELVE,  # Unstable Power Suit Core
            225891: Source.DELVE,  # Vile Vial of Kaheti Bile
            226539: Source.DELVE,  # Scroll of Momentum
            225654: Source.DELVE,  # Imperfect Ascendancy Serum
            215170: Source.DELVE,  # Abyssal Trap
            225653: Source.DELVE,  # Siphoning Lightbrand
            225638: Source.DELVE,  # Spelunker's Waning Candle
            # 215172: Source.DELVE,  # Silken Chain Weaver
            225657: Source.DELVE,  # Detachable Fang
            225647: Source.WORLD_QUEST,  # Shining Arathor Insignia
            218307: Source.DELVE,  # Wildfire Wick
        }

        if self.item_id in item_mapping.keys():
            return item_mapping[self.item_id]

        if self.instance == Instance.DAWN_OF_THE_INFINITE:
            return Source.MEGA_DUNGEON

        instance_mapping = {
            InstanceType.DUNGEON: Source.DUNGEON,
            InstanceType.RAID: Source.RAID,
        }

        if self._trinket.id_journal_instance == 1205:
            return Source.WORLD_BOSS

        # disabled because Cataclysm now is also featured in m+
        # if self.expansion == Expansion.CATACLYSM and self.item_id > 100_000:
        #     return Source.TIMEWALKING
        # el
        if self.instance_type in instance_mapping.keys():
            return instance_mapping[self.instance_type]

        if "Aspirant" in self.full_name:
            return Source.LOW_PVP
        elif "Gladiator" in self.full_name:
            return Source.HIGH_PVP
        elif "Combatant" in self.full_name:
            return Source.PVP

        if "Template" in self.full_name:
            return Source.TEMPLATE
        if "Test Item" in self.full_name:
            return Source.TEMPLATE

        if "Alchemist" in self.full_name:
            return Source.PROFESSION

        if "Darkmoon Deck" in self.full_name:
            return Source.PROFESSION

        if "Idol of the" in self.full_name:
            return Source.PROFESSION

        if "Paracausal Fragment of " in self.full_name:
            return Source.CALLING

        return Source.UNKNOWN

    @property
    def itemlevels(self) -> typing.List[int]:
        # better than nothing
        levels: typing.List[int] = [
            self._trinket.ilevel,
        ]

        # add special cases here
        special_cases: typing.Dict[str, typing.Dict[Season, typing.List[int]]] = {}

        if self.seasons:
            # removing baseline itemlevel in case we have season information
            levels = []

        for season in self.seasons:
            if self.full_name in special_cases.keys():
                levels += special_cases[self.full_name][season]

            elif self.source == Source.RAID:
                if self.raid_tier in (None, RaidTier.UNKNOWN):
                    logger.warning(
                        "Raid Source was not yet properly set up. "
                        "Missing Raid tier! Add Encounter ID: "
                        f"'{self._trinket.id_encounter}' for '{self.full_name}'"
                    )
                levels += ItemLevel.ITEM_LEVELS[self.source][season][  # type: ignore
                    self.raid_tier
                ]

            elif self.source in (
                Source.CALLING,
                Source.PVP,
                Source.LOW_PVP,
                Source.HIGH_PVP,
                Source.DUNGEON,
                Source.RARE_MOB,
                Source.DELVE,
            ):
                levels += ItemLevel.ITEM_LEVELS[self.source][season]  # type: ignore

            elif self.source == Source.TIMEWALKING:
                levels = ItemLevel.ITEM_LEVELS[self.source][season][self.instance_type]  # type: ignore

            elif self.source in (
                Source.WORLD_QUEST,
                Source.MEGA_DUNGEON,
            ):
                levels = ItemLevel.ITEM_LEVELS[self.source][season]  # type: ignore
                if self.full_name == "Mirror of Fractured Tomorrows":
                    levels.extend(ItemLevel._df_s4_hero)  # hardcore
                    levels.extend(ItemLevel._df_s4_mythic)  # deathless

            elif self.source == Source.PROFESSION:
                levels += ItemLevel.ITEM_LEVELS[self.source][season]  # type: ignore
                epic_cutoff = 99999
                if "Darkmoon Deck:" in self.full_name:
                    levels = [level for level in levels if level < epic_cutoff]
                elif "Darkmoon Deck Box:" in self.full_name:
                    levels = [level for level in levels if level >= epic_cutoff]

            elif self.source == Source.WORLD_BOSS:
                # is REPLACED by prepared itemlevels, blizzard hotfixes are hot fixes
                levels = ItemLevel.ITEM_LEVELS[self.source][season]  # type: ignore

        if self.source == Source.PROFESSION:
            levels += [
                self._trinket.ilevel,
            ]

        if self.full_name == "Mirror of Fractured Tomorrows":
            levels += ItemLevel._df_s2_mythic[:-1]

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
        unknown_stats = {
            56285: [Stat.STRENGTH],  # Might of the Ocean
            133197: [Stat.STRENGTH],  # the newer "Might of the Ocean"
            110019: [Stat.STRENGTH, Stat.AGILITY],  # Xeri'tac's Unhatched Egg Sac
            137315: [Stat.STRENGTH, Stat.AGILITY],  # Writhing Heart of Darkness
            136715: [Stat.STRENGTH, Stat.AGILITY],  # Spiked Counterweight
            56290: [Stat.INTELLECT],  # Sea Star
            133201: [Stat.INTELLECT],  # the newer "Sea Star"
            56280: [Stat.STRENGTH, Stat.AGILITY],  # Porcelain Crab
            137306: [Stat.INTELLECT, Stat.AGILITY],  # Oakheart's Gnarled Root
            110009: [Stat.INTELLECT],  # Leaf of the Ancient Protectors
            193697: [Stat.AGILITY],  # Bottle of Spiraling Winds
            193762: [Stat.STRENGTH],  # Blazebinder's Hoof
            159630: [Stat.INTELLECT],  # Balefire Branch
            193791: [Stat.INTELLECT],  # Time-Breaching Talon
            159625: [Stat.STRENGTH],  # Vial of Animated Blood
        }
        """Game data doesn't provide primary stat information."""

        if self.item_id in unknown_stats:
            return unknown_stats[self.item_id]

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
        return min(self.itemlevels, default=-1)

    @property
    def max_itemlevel(self) -> int:
        return max(self.itemlevels, default=-1)

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
        unmapped_trinkets = {
            133300: Instance.GRIM_BATOL,  # Mark of Khardros
            133282: Instance.GRIM_BATOL,  # Skardyn's Grace
            133304: Instance.GRIM_BATOL,  # Gale of Shadows
        }
        return unmapped_trinkets.get(self.item_id, None)

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

        if self.instance not in (
            Instance.VAULT_OF_THE_INCARNATES,
            Instance.ABERUS_THE_SHADOWED_CRUCIBLE,
            Instance.AMIRDRASSIL_THE_DREAMS_HOPE,
            Instance.NERUBAR_PALACE,
            Instance.BLACKROCK_DEPTHS_EVENT,
        ):
            return None

        # special cases for rare drops
        #   - Whispering Incarnate Icon
        if self.item_id in (194301,):
            return RaidTier.MID
        #   - Screaming Black Dragonscale
        elif self.item_id in (202612,):
            return RaidTier.HIGH
        # - Neltharion's Call to Chaos
        # - Neltharion's Call to Dominance
        # - Neltharion's Call to Suffering
        # - Augury of the Primal Flame
        # - Blossom of Amirdrassil
        # - Fyrakk's Tainted Rageheart
        elif self.item_id in (
            204201,
            204202,
            204211,
            208614,
            207171,
            207174,
        ):
            return RaidTier.VERY_RARE

        return RaidTier.get_raid_tier_from_encounter_id(self._trinket.id_encounter)

    @property
    def seasons(self) -> typing.List[Season]:
        non_seasonal_items = [
            56370,
            191492,
        ]

        if self.item_id in non_seasonal_items:
            return []

        if (
            self.expansion == Expansion.DRAGONFLIGHT
            and self.source == Source.MEGA_DUNGEON
        ):
            return [Season.DF_SEASON_2, Season.DF_SEASON_3, Season.DF_SEASON_4]

        seasons_ = Season.get_seasons_from_instance(self.instance)
        if seasons_:
            return seasons_

        if self.expansion == Expansion.DRAGONFLIGHT:
            if self.source == Source.WORLD_BOSS:
                return [Season.DF_SEASON_1]

            if self.source == Source.PROFESSION and "zzOld" not in self.full_name:
                return [
                    Season.DF_SEASON_1,
                    Season.DF_SEASON_2,
                    Season.DF_SEASON_3,
                    Season.DF_SEASON_4,
                ]

            if self.source in (Source.PVP, Source.LOW_PVP, Source.HIGH_PVP):
                if self.full_name.startswith("Crimson"):
                    return [Season.DF_SEASON_1]
                elif self.full_name.startswith("Obsidian"):
                    return [Season.DF_SEASON_2]
                elif self.full_name.startswith("Verdant"):
                    return [Season.DF_SEASON_3]
                elif self.full_name.startswith("Draconic"):
                    return [Season.DF_SEASON_4]

            if self.source == Source.RARE_MOB:
                return [Season.DF_SEASON_1]

            if self.source == Source.WORLD_QUEST:
                return [
                    Season.DF_SEASON_1,
                    Season.DF_SEASON_2,
                    Season.DF_SEASON_3,
                    Season.DF_SEASON_4,
                ]

            if (
                self.source
                == Source.CALLING
                # and "Paracausal Fragment of " in self.full_name
            ):
                return [Season.DF_SEASON_2, Season.DF_SEASON_3, Season.DF_SEASON_4]

            if self.source == Source.TIMEWALKING and self.instance:
                return [Season.DF_SEASON_2]

        if self.expansion == Expansion.THE_WAR_WITHIN:
            if self.source == Source.WORLD_BOSS:
                return [Season.TWW_SEASON_1]

            if self.source == Source.PROFESSION:
                return [
                    Season.TWW_SEASON_1,
                ]

            if self.source == Source.DELVE:
                return [
                    Season.TWW_SEASON_1,
                ]

            if self.source in (Source.PVP, Source.LOW_PVP, Source.HIGH_PVP):
                if self.full_name.startswith("Forged"):
                    return [
                        Season.TWW_SEASON_1,
                    ]

            if self.source == Source.RARE_MOB:
                return [
                    Season.TWW_SEASON_1,
                ]

            if self.source == Source.WORLD_QUEST:
                return [
                    Season.TWW_SEASON_1,
                ]

            if self.source == Source.CALLING:
                return [
                    Season.TWW_SEASON_1,
                ]

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
