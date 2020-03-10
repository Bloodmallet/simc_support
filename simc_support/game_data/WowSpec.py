from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data import WowClass
from simc_support.game_data import Language
import enum


class RaidRole(enum.Enum):
    TANK = "tank"
    DD = "dd"
    HEAL = "heal"


class Role(enum.Enum):
    MELEE = "melee"
    RANGED = "ranged"


class Stat(enum.Enum):
    STRENGTH = "str"
    AGILITY = "agi"
    INTELLECT = "int"


class WowSpec(SimcObject):
    """World of Warcraft Class spec data.
    """

    def __init__(
        self,
        id: int,
        wow_class: WowClass.WowClass,
        translations: Language.Translation,
        talents: str,
        raid_role: RaidRole,
        role: Role,
        stat: Stat,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.id = int(id)
        self.wow_class = wow_class

        if type(translations) == Language.Translation:
            self.translations = translations
        else:
            self.translations = Language.Translation(translations=translations)

        talents = str(talents)
        if len(talents) != 7:
            raise ValueError("Wrong talent string length, expected 7")
        if len(talents.replace("1", "").replace("0", "")) != 0:
            raise ValueError("Expected talent string to contain only '1' and '0' charcters")
        self.talents = talents

        if raid_role not in [k for k in RaidRole]:
            raise ValueError(f"Unknown raid_role '{raid_role}'")
        self.raid_role = raid_role

        if role not in [k for k in Role]:
            raise ValueError(f"Unknown role '{role}'")
        self.role = role

        if stat not in [k for k in Stat]:
            raise ValueError(f"Unknown stat '{stat}'")
        self.stat = stat


empty_translation = {}
for lang in Language.LANGUAGES:
    empty_translation[lang] = ""

# Spec data here
BLOOD = WowSpec(
    id=250,
    wow_class=WowClass.DEATHKNIGHT,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Blood",
    simc_name='blood',
)
FROST_DK = WowSpec(
    id=251,
    wow_class=WowClass.DEATHKNIGHT,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Frost",
    simc_name='frost',
)
UNHOLY = WowSpec(
    id=252,
    wow_class=WowClass.DEATHKNIGHT,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Unholy",
    simc_name='unholy',
)
HAVOC = WowSpec(
    id=577,
    wow_class=WowClass.DEMONHUNTER,
    translations=empty_translation,
    talents="1110111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Havoc",
    simc_name='havoc',
)
VENGEANCE = WowSpec(
    id=581,
    wow_class=WowClass.DEMONHUNTER,
    translations=empty_translation,
    talents="1111111",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Vengeance",
    simc_name='vengeance',
)
BALANCE = WowSpec(
    id=102,
    wow_class=WowClass.DRUID,
    translations=empty_translation,
    talents="1000111",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Balance",
    simc_name='balance',
)
FERAL = WowSpec(
    id=103,
    wow_class=WowClass.DRUID,
    translations=empty_translation,
    talents="1000111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Feral",
    simc_name='feral',
)
GUARDIAN = WowSpec(
    id=104,
    wow_class=WowClass.DRUID,
    translations=empty_translation,
    talents="1000111",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Guardian",
    simc_name='guardian',
)
RESTORATION_DRUID = WowSpec(
    id=105,
    wow_class=WowClass.DRUID,
    translations=empty_translation,
    talents="0010000",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.INTELLECT,
    full_name="Restoration",
    simc_name='restoration',
)
BEASTMASTERY = WowSpec(
    id=253,
    wow_class=WowClass.HUNTER,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.AGILITY,
    full_name="Beast_Mastery",
    simc_name='beast_mastery',
)
MARKSMANSHIP = WowSpec(
    id=254,
    wow_class=WowClass.HUNTER,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.AGILITY,
    full_name="Marksmanship",
    simc_name='marksmanship',
)
SURVIVAL = WowSpec(
    id=255,
    wow_class=WowClass.HUNTER,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Survival",
    simc_name='survival',
)
ARCANE = WowSpec(
    id=62,
    wow_class=WowClass.MAGE,
    translations=empty_translation,
    talents="1011011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Arcane",
    simc_name='arcane',
)
FIRE = WowSpec(
    id=63,
    wow_class=WowClass.MAGE,
    translations=empty_translation,
    talents="1011011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Fire",
    simc_name='fire',
)
FROST_MAGE = WowSpec(
    id=64,
    wow_class=WowClass.MAGE,
    translations=empty_translation,
    talents="1011011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Frost",
    simc_name='frost',
)
BREWMASTER = WowSpec(
    id=268,
    wow_class=WowClass.MONK,
    translations=empty_translation,
    talents="1010011",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Brewmaster",
    simc_name='brewmaster',
)
WINDWALKER = WowSpec(
    id=269,
    wow_class=WowClass.MONK,
    translations=empty_translation,
    talents="1010011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Windwalker",
    simc_name='windwalker',
)
PROTECTION_PALADIN = WowSpec(
    id=66,
    wow_class=WowClass.PALADIN,
    translations=empty_translation,
    talents="1101001",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Protection",
    simc_name='protection',
)
RETRIBUTION = WowSpec(
    id=70,
    wow_class=WowClass.PALADIN,
    translations=empty_translation,
    talents="1101001",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Retribution",
    simc_name='retribution',
)
DISCIPLINE = WowSpec(
    id=256,
    wow_class=WowClass.PRIEST,
    translations=empty_translation,
    talents="1010111",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Discipline",
    simc_name='discipline',
)
HOLY_PRIEST = WowSpec(
    id=257,
    wow_class=WowClass.PRIEST,
    translations=empty_translation,
    talents="1010111",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Holy",
    simc_name='holy',
)
SHADOW = WowSpec(
    id=258,
    wow_class=WowClass.PRIEST,
    translations=empty_translation,
    talents="1010111",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Shadow",
    simc_name='shadow',
)
ASSASSINATION = WowSpec(
    id=259,
    wow_class=WowClass.ROGUE,
    translations=empty_translation,
    talents="1110011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Assassination",
    simc_name='assassination',
)
OUTLAW = WowSpec(
    id=260,
    wow_class=WowClass.ROGUE,
    translations=empty_translation,
    talents="1010011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Outlaw",
    simc_name='outlaw',
)
SUBTLETY = WowSpec(
    id=261,
    wow_class=WowClass.ROGUE,
    translations=empty_translation,
    talents="1110011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Subtlety",
    simc_name='subtlety',
)
ELEMENTAL = WowSpec(
    id=262,
    wow_class=WowClass.SHAMAN,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Elemental",
    simc_name='elemental',
)
ENHANCEMENT = WowSpec(
    id=263,
    wow_class=WowClass.SHAMAN,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Enhancement",
    simc_name='enhancement',
)
RESTORATION_SHAMAN = WowSpec(
    id=264,
    wow_class=WowClass.SHAMAN,
    translations=empty_translation,
    talents="0100000",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Restoration",
    simc_name='restoration',
)
AFFLICTION = WowSpec(
    id=265,
    wow_class=WowClass.WARLOCK,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Affliction",
    simc_name='affliction',
)
DEMONOLOGY = WowSpec(
    id=266,
    wow_class=WowClass.WARLOCK,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Demonology",
    simc_name='demonology',
)
DESTRUCTION = WowSpec(
    id=267,
    wow_class=WowClass.WARLOCK,
    translations=empty_translation,
    talents="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Destruction",
    simc_name='destruction',
)
ARMS = WowSpec(
    id=71,
    wow_class=WowClass.WARRIOR,
    translations=empty_translation,
    talents="1010111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Arms",
    simc_name='arms',
)
FURY = WowSpec(
    id=72,
    wow_class=WowClass.WARRIOR,
    translations=empty_translation,
    talents="1010111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Fury",
    simc_name='fury',
)
PROTECTION_WARRIOR = WowSpec(
    id=73,
    wow_class=WowClass.WARRIOR,
    translations=empty_translation,
    talents="1010111",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Protection",
    simc_name='protection',
)
