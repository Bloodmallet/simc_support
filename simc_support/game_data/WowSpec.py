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
            self.translations = Language.Translation(translations)

        talents = str(talents)
        if len(talents) != 7:
            raise ValueError("Wrong talent string length, expected 7")
        if len(talents.replace("1", "").replace("0", "")) != 0:
            raise ValueError("Expected talent string to contain only '1' and '0' charcters")
        self.talents = talents

        if raid_role not in set(k.value for k in RaidRole):
            raise ValueError(f"Unknown raid_role '{raid_role}'")
        self.raid_role = raid_role

        if role not in set(k.value for k in Role):
            raise ValueError(f"Uknown role '{role}'")
        self.role = role

        if stat not in set(k.value for k in Stat):
            raise ValueError(f"Uknown stat '{stat}'")
        self.stat = stat


empty_translation = {}
for lang in Language.LANGUAGES:
    empty_translation[lang] = ""

# Spec data here
BLOOD = WowSpec(
    250, WowClass.DEATHKNIGHT, empty_translation, "1101011", RaidRole.TANK, Role.MELEE,
    Stat.STRENGTH, "Blood", 'blood'
)

# original data
class_data = {
    "Death_Knight": {
        "id": 6,
        "specs": {
            "Blood": {
                "talents": "1101011",
                "raid_role": "tank",
                "role": "melee",
                "stat": "str",
                "id": 250,
            },
            "Frost": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "str",
                "id": 251,
            },
            "Unholy": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "str",
                "id": 252,
            }
        }
    },
    "Demon_Hunter": {
        "id": 12,
        "specs": {
            "Havoc": {
                "talents": "1110111",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 577,
            },
            "Vengeance": {
                "talents": "1111111",
                "raid_role": "tank",
                "role": "melee",
                "stat": "agi",
                "id": 581,
            }
        }
    },
    "Druid": {
        "id": 11,
        "specs": {
            "Balance": {
                "talents": "1000111",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 102,
            },
            "Feral": {
                "talents": "1000111",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 103,
            },
            "Guardian": {
                "talents": "1000111",
                "raid_role": "tank",
                "role": "melee",
                "stat": "agi",
                "id": 104,
            },
            "Restoration": {
                "talents": "0010000",
                "raid_role": "dd",
                "role": "melee",
                "stat": "int",
                "id": 105,
            }
        }
    },
    "Hunter": {
        "id": 3,
        "specs": {
            "Beast_Mastery": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "agi",
                "id": 253,
            },
            "Marksmanship": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "agi",
                "id": 254,
            },
            "Survival": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 255,
            }
        }
    },
    "Mage": {
        "id": 8,
        "specs": {
            "Arcane": {
                "talents": "1011011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 62,
            },
            "Fire": {
                "talents": "1011011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 63,
            },
            "Frost": {
                "talents": "1011011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 64,
            }
        }
    },
    "Monk": {
        "id": 10,
        "specs": {
            "Brewmaster": {
                "talents": "1010011",
                "raid_role": "tank",
                "role": "melee",
                "stat": "agi",
                "id": 268,
            },
            "Windwalker": {
                "talents": "1010011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 269,
            }
        }
    },
    "Paladin": {
        "id": 2,
        "specs": {
            "Protection": {
                "talents": "1101001",
                "raid_role": "tank",
                "role": "melee",
                "stat": "str",
                "id": 66,
            },
            "Retribution": {
                "talents": "1101001",
                "raid_role": "dd",
                "role": "melee",
                "stat": "str",
                "id": 70,
            }
        }
    },
    "Priest": {
        "id": 5,
        "specs": {
            "Discipline": {
                "talents": "1010111",
                "raid_role": "heal",
                "role": "ranged",
                "stat": "int",
                "id": 257,
            },
            "Holy": {
                "talents": "1010111",
                "raid_role": "heal",
                "role": "ranged",
                "stat": "int",
                "id": 257,
            },
            "Shadow": {
                "talents": "1010111",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 258,
            }
        }
    },
    "Rogue": {
        "id": 4,
        "specs": {
            "Assassination": {
                "talents": "1110011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 259,
            },
            "Outlaw": {
                "talents": "1010011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 260,
            },
            "Subtlety": {
                "talents": "1110011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 261,
            }
        }
    },
    "Shaman": {
        "id": 7,
        "specs": {
            "Elemental": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 262,
            },
            "Enhancement": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "melee",
                "stat": "agi",
                "id": 263,
            },
            "Restoration": {
                "talents": "0100000",
                "raid_role": "heal",
                "role": "ranged",
                "stat": "int",
                "id": 264,
            }
        }
    },
    "Warlock": {
        "id": 9,
        "specs": {
            "Affliction": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 265,
            },
            "Demonology": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 266,
            },
            "Destruction": {
                "talents": "1101011",
                "raid_role": "dd",
                "role": "ranged",
                "stat": "int",
                "id": 267,
            }
        }
    },
    "Warrior": {
        "id": 1,
        "specs": {
            "Arms": {
                "talents": "1010111",
                "raid_role": "dd",
                "role": "melee",
                "stat": "str",
                "id": 71,
            },
            "Fury": {
                "talents": "1010111",
                "raid_role": "dd",
                "role": "melee",
                "stat": "str",
                "id": 72,
            },
            "Protection": {
                "talents": "1010111",
                "raid_role": "tank",
                "role": "melee",
                "stat": "str",
                "id": 73,
            }
        }
    }
}
