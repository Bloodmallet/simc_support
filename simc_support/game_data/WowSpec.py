import itertools
import typing

from simc_support.game_data import Language, WowClass
from simc_support.game_data.RaidRole import RaidRole
from simc_support.game_data.Role import Role
from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data.Stat import Stat
from simc_support.game_data.Talent import TREES, Tree


class WowSpec(SimcObject):
    """World of Warcraft Class spec data."""

    def __init__(
        self,
        id: int,
        wow_class: WowClass.WowClass,
        translations: Language.Translation,
        raid_role: RaidRole,
        role: Role,
        stat: Stat,
        ptr=False,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.id: int = int(id)
        self.wow_class: WowClass.WowClass = wow_class

        if isinstance(translations, Language.Translation):
            self.translations: Language.Translation = translations
        else:
            self.translations = Language.Translation(translations=translations)

        if raid_role not in RaidRole:
            raise ValueError(f"Unknown raid_role '{raid_role}'")
        self.raid_role: RaidRole = raid_role

        if role not in Role:
            raise ValueError(f"Unknown role '{role}'")
        self.role: Role = role

        if stat not in Stat:
            raise ValueError(f"Unknown stat '{stat}'")
        self.stat: Stat = stat

        tree_info = TREES[self.wow_class.simc_name + "_" + self.simc_name]

        self.talent_trees: typing.Tuple[Tree, Tree] = (tree_info[0], tree_info[1])
        self.class_tree: Tree = self.talent_trees[0]
        self.spec_tree: Tree = self.talent_trees[1]
        self.full_node_order: typing.List[int] = tree_info[0].full_node_order

    def __repr__(self) -> str:
        return " ".join([super().__repr__(), self.wow_class.__repr__()])

    def __str__(self) -> str:
        return " ".join([super().__str__(), self.wow_class.__str__()])

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.full_name,
            "wow_class": {
                "id": self.wow_class.id,
                "name": self.wow_class.full_name,
            },
        }


# Spec data here
BLOOD = WowSpec(
    id=250,
    wow_class=WowClass.DEATHKNIGHT,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1110011",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Blood",
    simc_name="blood",
)
FROST_DK = WowSpec(
    id=251,
    wow_class=WowClass.DEATHKNIGHT,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Frost",
    simc_name="frost",
)
UNHOLY = WowSpec(
    id=252,
    wow_class=WowClass.DEATHKNIGHT,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Unholy",
    simc_name="unholy",
)
HAVOC = WowSpec(
    id=577,
    wow_class=WowClass.DEMONHUNTER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1110111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Havoc",
    simc_name="havoc",
)
VENGEANCE = WowSpec(
    id=581,
    wow_class=WowClass.DEMONHUNTER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1111111",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Vengeance",
    simc_name="vengeance",
)
BALANCE = WowSpec(
    id=102,
    wow_class=WowClass.DRUID,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000111",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Balance",
    simc_name="balance",
)
FERAL = WowSpec(
    id=103,
    wow_class=WowClass.DRUID,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Feral",
    simc_name="feral",
)
GUARDIAN = WowSpec(
    id=104,
    wow_class=WowClass.DRUID,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000111",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Guardian",
    simc_name="guardian",
)
RESTORATION_DRUID = WowSpec(
    id=105,
    wow_class=WowClass.DRUID,
    translations=Language.EmptyTranslation(),
    talents_blueprint="0010000",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.INTELLECT,
    full_name="Restoration",
    simc_name="restoration",
)
AUGMENTATION = WowSpec(
    id=1473,
    wow_class=WowClass.EVOKER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000111",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Augmentation",
    simc_name="augmentation",
)
DEVASTATION = WowSpec(
    id=1467,
    wow_class=WowClass.EVOKER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000111",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Devastation",
    simc_name="devastation",
)
PRESERVATION = WowSpec(
    id=1468,
    wow_class=WowClass.EVOKER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000111",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Preservation",
    simc_name="preservation",
)
BEASTMASTERY = WowSpec(
    id=253,
    wow_class=WowClass.HUNTER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.AGILITY,
    full_name="Beast_Mastery",
    simc_name="beast_mastery",
)
MARKSMANSHIP = WowSpec(
    id=254,
    wow_class=WowClass.HUNTER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.AGILITY,
    full_name="Marksmanship",
    simc_name="marksmanship",
)
SURVIVAL = WowSpec(
    id=255,
    wow_class=WowClass.HUNTER,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Survival",
    simc_name="survival",
)
ARCANE = WowSpec(
    id=62,
    wow_class=WowClass.MAGE,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1011011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Arcane",
    simc_name="arcane",
)
FIRE = WowSpec(
    id=63,
    wow_class=WowClass.MAGE,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1011011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Fire",
    simc_name="fire",
)
FROST_MAGE = WowSpec(
    id=64,
    wow_class=WowClass.MAGE,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1011011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Frost",
    simc_name="frost",
)
BREWMASTER = WowSpec(
    id=268,
    wow_class=WowClass.MONK,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010011",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Brewmaster",
    simc_name="brewmaster",
)
WINDWALKER = WowSpec(
    id=269,
    wow_class=WowClass.MONK,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Windwalker",
    simc_name="windwalker",
)
MISTWEAVER = WowSpec(
    id=270,
    wow_class=WowClass.MONK,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1000011",
    raid_role=RaidRole.HEAL,
    role=Role.MELEE,
    stat=Stat.INTELLECT,
    full_name="Mistweaver",
    simc_name="mistweaver",
)
PROTECTION_PALADIN = WowSpec(
    id=66,
    wow_class=WowClass.PALADIN,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1100101",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Protection",
    simc_name="protection",
)
RETRIBUTION = WowSpec(
    id=70,
    wow_class=WowClass.PALADIN,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1100101",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Retribution",
    simc_name="retribution",
)
HOLY_PALADIN = WowSpec(
    id=65,
    wow_class=WowClass.PALADIN,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1100111",
    raid_role=RaidRole.HEAL,
    role=Role.MELEE,
    stat=Stat.INTELLECT,
    full_name="Holy",
    simc_name="holy",
)
DISCIPLINE = WowSpec(
    id=256,
    wow_class=WowClass.PRIEST,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010111",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Discipline",
    simc_name="discipline",
)
HOLY_PRIEST = WowSpec(
    id=257,
    wow_class=WowClass.PRIEST,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010111",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Holy",
    simc_name="holy",
)
SHADOW = WowSpec(
    id=258,
    wow_class=WowClass.PRIEST,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010111",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Shadow",
    simc_name="shadow",
)
ASSASSINATION = WowSpec(
    id=259,
    wow_class=WowClass.ROGUE,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1110011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Assassination",
    simc_name="assassination",
)
OUTLAW = WowSpec(
    id=260,
    wow_class=WowClass.ROGUE,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Outlaw",
    simc_name="outlaw",
)
SUBTLETY = WowSpec(
    id=261,
    wow_class=WowClass.ROGUE,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1110011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Subtlety",
    simc_name="subtlety",
)
ELEMENTAL = WowSpec(
    id=262,
    wow_class=WowClass.SHAMAN,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Elemental",
    simc_name="elemental",
)
ENHANCEMENT = WowSpec(
    id=263,
    wow_class=WowClass.SHAMAN,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.AGILITY,
    full_name="Enhancement",
    simc_name="enhancement",
)
RESTORATION_SHAMAN = WowSpec(
    id=264,
    wow_class=WowClass.SHAMAN,
    translations=Language.EmptyTranslation(),
    talents_blueprint="0100000",
    raid_role=RaidRole.HEAL,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Restoration",
    simc_name="restoration",
)
AFFLICTION = WowSpec(
    id=265,
    wow_class=WowClass.WARLOCK,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Affliction",
    simc_name="affliction",
)
DEMONOLOGY = WowSpec(
    id=266,
    wow_class=WowClass.WARLOCK,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Demonology",
    simc_name="demonology",
)
DESTRUCTION = WowSpec(
    id=267,
    wow_class=WowClass.WARLOCK,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1101011",
    raid_role=RaidRole.DD,
    role=Role.RANGED,
    stat=Stat.INTELLECT,
    full_name="Destruction",
    simc_name="destruction",
)
ARMS = WowSpec(
    id=71,
    wow_class=WowClass.WARRIOR,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Arms",
    simc_name="arms",
)
FURY = WowSpec(
    id=72,
    wow_class=WowClass.WARRIOR,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010111",
    raid_role=RaidRole.DD,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Fury",
    simc_name="fury",
)
PROTECTION_WARRIOR = WowSpec(
    id=73,
    wow_class=WowClass.WARRIOR,
    translations=Language.EmptyTranslation(),
    talents_blueprint="1010111",
    raid_role=RaidRole.TANK,
    role=Role.MELEE,
    stat=Stat.STRENGTH,
    full_name="Protection",
    simc_name="protection",
)

WOWSPECS = [
    BLOOD,
    FROST_DK,
    UNHOLY,
    HAVOC,
    VENGEANCE,
    BALANCE,
    FERAL,
    GUARDIAN,
    RESTORATION_DRUID,
    AUGMENTATION,
    DEVASTATION,
    PRESERVATION,
    BEASTMASTERY,
    MARKSMANSHIP,
    SURVIVAL,
    ARCANE,
    FIRE,
    FROST_MAGE,
    BREWMASTER,
    WINDWALKER,
    MISTWEAVER,
    PROTECTION_PALADIN,
    RETRIBUTION,
    HOLY_PALADIN,
    DISCIPLINE,
    HOLY_PRIEST,
    SHADOW,
    ASSASSINATION,
    OUTLAW,
    SUBTLETY,
    ELEMENTAL,
    ENHANCEMENT,
    RESTORATION_SHAMAN,
    AFFLICTION,
    DEMONOLOGY,
    DESTRUCTION,
    ARMS,
    FURY,
    PROTECTION_WARRIOR,
]


def get_wow_spec(
    wow_class: typing.Union[WowClass.WowClass, str], wow_spec: str
) -> WowSpec:
    """Obtain WowSpec from a WowClass/Name and wow spec name combination.

    Args:
        wow_class (typing.Union[WowClass.WowClass, str]): Instance of a WowClass or the name of that WowClass, e.g. "Mage"
        wow_spec (str): Name of the WowSpec, e.g. "Arcane"

    Raises:
        ValueError: An appropriate WowSpec couldn't be found.

    Returns:
        WowSpec
    """
    if isinstance(wow_class, str):
        wow_class = WowClass.get_wow_class(wow_class)

    for spec in WOWSPECS:
        if spec.wow_class == wow_class and wow_spec in (spec.full_name, spec.simc_name):
            return spec
    raise ValueError(
        f"No WowSpec found of class '{wow_class.simc_name}' and spec '{wow_spec}'."
    )


def get_wow_spec_from_id(wow_spec_id: int) -> WowSpec:
    """Obtain WoWSpec from a spec ID.

    Args:
        wow_spec_id (int): e.g. 62 (which would be Arcane Mage)

    Raises:
        ValueError: An appropriate WowSpec couldn't be found.

    Returns:
        WowSpec
    """
    for spec in WOWSPECS:
        if spec.id == wow_spec_id:
            return spec
    raise ValueError(f"No WowSpec found with id '{wow_spec_id}'.")


def get_wow_spec_from_combined_simc_name(wow_class_spec_name: str) -> WowSpec:
    """Obtain WoWSpec from a combined Class_Spec string from SimC with whitespace replaced by underscore.

    Args:
        wow_class_spec_name (str): e.g. "Death_Knight_Frost"

    Raises:
        ValueError: An appropriate WowSpec couldn't be found.

    Returns:
        WowSpec
    """
    for spec in WOWSPECS:
        combined_name = f"{spec.wow_class} {spec.full_name}".replace(" ", "_")
        if combined_name == wow_class_spec_name:
            return spec
    raise ValueError(f"No WowSpec found for class_spec '{wow_class_spec_name}'.")
