from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data import Race
from simc_support.game_data.Language import Translation
from simc_support.game_data.Language import LANGUAGES


class WowClass(SimcObject):

    def __init__(self, id: int, races: list, translations: Translation, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.id = int(id)
        # double check input to be of Race class
        for race in races:
            if type(race) != Race.Race:
                raise TypeError("Expected races to be of Race type. Got {} instead.".format(type(race)))
            if race not in Race.RACES:
                raise ValueError("Unknown race {}.".format(race))
        self.races = races
        if type(translations) == Translation:
            self.translations = translations
        else:
            self.translations = Translation(translations)


empty_translation = {}
for lang in LANGUAGES:
    empty_translation[lang] = ""

DEATHKNIGHT = WowClass(6, Race.RACES, empty_translation, "Death Knight", 'death_knight')
DEMONHUNTER = WowClass(12, [
    Race.NIGHTELF,
    Race.BLOODELF,
], empty_translation, "Demon Hunter", 'demon_hunter')
DEMONHUNTER = WowClass(12, [
    Race.NIGHTELF,
    Race.BLOODELF,
], empty_translation, "Demon Hunter", 'demon_hunter')
DRUID = WowClass(
    11, [
        Race.NIGHTELF,
        Race.WORGEN,
        Race.KULTIRAN,
        Race.TAUREN,
        Race.TROLL,
        Race.HIGHMOUNTAINTAUREN,
        Race.ZANDALARITROLL,
    ], empty_translation, "Druid", 'druid'
)
HUNTER = WowClass(3, Race.RACES, empty_translation, "Hunter", 'hunter')
MAGE = WowClass(
    8, [
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.WORGEN,
        Race.VOIDELF,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Mage", 'mage'
)
MONK = WowClass(
    10, [
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.VOIDELF,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TAUREN,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.HIGHMOUNTAINTAUREN,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Monk", 'monk'
)
PALADIN = WowClass(
    2, [
        Race.DRAENEI,
        Race.DWARF,
        Race.HUMAN,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.BLOODELF,
        Race.TAUREN,
        Race.ZANDALARITROLL,
    ], empty_translation, "Paladin", 'paladin'
)
PRIEST = WowClass(
    5, [
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.WORGEN,
        Race.VOIDELF,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.PANDAREN_HORDE,
        Race.TAUREN,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Priest", 'priest'
)
ROGUE = WowClass(
    4, [
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.WORGEN,
        Race.VOIDELF,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Rogue", 'rogue'
)
SHAMAN = WowClass(
    7, [
        Race.DRAENEI,
        Race.DWARF,
        Race.PANDAREN_ALLIANCE,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.GOBLIN,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TAUREN,
        Race.TROLL,
        Race.HIGHMOUNTAINTAUREN,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Shaman", 'shaman'
)
WARLOCK = WowClass(
    9, [
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.WORGEN,
        Race.VOIDELF,
        Race.DARKIRONDWARF,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.ORC,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.VULPERA,
    ], empty_translation, "Warlock", 'warlock'
)
WARRIOR = WowClass(1, Race.RACES, empty_translation, "Warrior", 'warrior')

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
