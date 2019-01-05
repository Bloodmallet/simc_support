# -*- coding: utf-8 -*-
# Utility file for class specialisations
# Contains wow classes, specs, dps talent rows,
## races, trinkets

import json

# these values are used throughout the code to determine itemlevel "borders" of items
# usually used as a catch up mechanic, drops usually all items from previous content
TRADER_TOKEN = 300
WORLD_QUEST_ITEMLEVEL = 320
# standard dungeon itemlevel (normal, max level dungeon)
DUNGEON_ITEMLEVEL = 310
# highest available itemlevel from m+ dungeons. weekly chest is NOT included here
M_PLUS_ITEMLEVEL = 340
TITANFORGE_CAP = 400  # currently highest itemlevel titanforging cap
EXPANSION_START_ITEMLEVEL = 280


class Trinket(object):
    """docstring for trinket"""

    def __init__(
        self,
        name,
        item_id,
        min_itemlevel,
        max_itemlevel,
        max_itemlevel_drop,
        agility,
        intellect,
        strength,
        melee,
        ranged,
        legendary=False,
        source=None
    ):
        super(Trinket, self).__init__()
        self.name: str = str(name)
        self.item_id: str = str(item_id)
        self.min_itemlevel: int = int(min_itemlevel)
        self.max_itemlevel: int = int(max_itemlevel)
        self.max_itemlevel_drop: int = int(max_itemlevel_drop)
        self.agility: bool = bool(agility)
        self.intellect: bool = bool(intellect)
        self.strength: bool = bool(strength)
        self.melee: bool = bool(melee)
        self.ranged: bool = bool(ranged)
        self.legendary: bool = bool(legendary)
        self.source: str = str(source)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.item_id

    def get_source(self):
        return self.source


__class_data = {
    "Death_Knight": {
        "id": 6,
        "specs": {
            "Blood": {
                "talents": "1101011",
                "role": "melee",
                "stat": "str",
                "id": 250,
            },
            "Frost": {
                "talents": "1101011",
                "role": "melee",
                "stat": "str",
                "id": 251,
            },
            "Unholy": {
                "talents": "1101011",
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
                "role": "melee",
                "stat": "agi",
                "id": 577,
            },
            "Vengeance": {
                "talents": "1111111",
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
                "role": "ranged",
                "stat": "int",
                "id": 102,
            },
            "Feral": {
                "talents": "1000111",
                "role": "melee",
                "stat": "agi",
                "id": 103,
            },
            "Guardian": {
                "talents": "1000111",
                "role": "melee",
                "stat": "agi",
                "id": 104,
            }
        }
    },
    "Hunter": {
        "id": 3,
        "specs": {
            "Beast_Mastery": {
                "talents": "1101011",
                "role": "ranged",
                "stat": "agi",
                "id": 253,
            },
            "Marksmanship": {
                "talents": "1101011",
                "role": "ranged",
                "stat": "agi",
                "id": 254,
            },
            "Survival": {
                "talents": "1101011",
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
                "role": "ranged",
                "stat": "int",
                "id": 62,
            },
            "Fire": {
                "talents": "1011011",
                "role": "ranged",
                "stat": "int",
                "id": 63,
            },
            "Frost": {
                "talents": "1011011",
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
                "role": "melee",
                "stat": "agi",
                "id": 268,
            },
            "Windwalker": {
                "talents": "1010011",
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
                "role": "melee",
                "stat": "str",
                "id": 66,
            },
            "Retribution": {
                "talents": "1101001",
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
                "role": "ranged",
                "stat": "int",
                "id": 257,
            },
            "Holy": {
                "talents": "1010111",
                "role": "ranged",
                "stat": "int",
                "id": 257,
            },
            "Shadow": {
                "talents": "1010111",
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
                "role": "melee",
                "stat": "agi",
                "id": 259,
            },
            "Outlaw": {
                "talents": "1010011",
                "role": "melee",
                "stat": "agi",
                "id": 260,
            },
            "Subtlety": {
                "talents": "1110011",
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
                "role": "ranged",
                "stat": "int",
                "id": 262,
            },
            "Enhancement": {
                "talents": "1101011",
                "role": "melee",
                "stat": "agi",
                "id": 263,
            }
        }
    },
    "Warlock": {
        "id": 9,
        "specs": {
            "Affliction": {
                "talents": "1101011",
                "role": "ranged",
                "stat": "int",
                "id": 265,
            },
            "Demonology": {
                "talents": "1101011",
                "role": "ranged",
                "stat": "int",
                "id": 266,
            },
            "Destruction": {
                "talents": "1101011",
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
                "role": "melee",
                "stat": "str",
                "id": 71,
            },
            "Fury": {
                "talents": "1010111",
                "role": "melee",
                "stat": "str",
                "id": 72,
            },
            "Protection": {
                "talents": "1010111",
                "role": "melee",
                "stat": "str",
                "id": 73,
            }
        }
    }
}

__races = {
    "alliance": {
        "draenei": (
            "warrior", "paladin", "hunter", "priest", "shaman", "mage", "monk",
            "death_knight"
        ),
        "dwarf": (
            "warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage",
            "warlock", "monk", "death_knight"
        ),
        "gnome": (
            "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk",
            "death_knight"
        ),
        "human": (
            "warrior", "paladin", "hunter", "rogue", "priest", "mage", "warlock",
            "monk", "death_knight"
        ),
        "night_elf": (
            "warrior", "hunter", "rogue", "priest", "mage", "monk", "druid",
            "death_knight", "demon_hunter"
        ),
        "pandaren": (
            "warrior", "hunter", "rogue", "priest", "shaman", "mage", "monk"
        ),
        "worgen": (
            "warrior", "hunter", "rogue", "priest", "mage", "warlock", "druid",
            "death_knight"
        ),
        "void_elf": (
            "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk"
        ),
        "lightforged_draenei": ("warrior", "paladin", "hunter", "priest", "mage"),
        "dark_iron_dwarf": ("warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage", "warlock", "monk")
    },
    "horde": {
        "blood_elf": (
            "warrior", "paladin", "hunter", "rogue", "priest", "mage", "warlock",
            "monk", "death_knight", "demon_hunter"
        ),
        "goblin": (
            "warrior", "hunter", "rogue", "priest", "shaman", "mage", "warlock",
            "death_knight"
        ),
        "orc": (
            "warrior", "hunter", "rogue", "shaman", "mage", "warlock", "monk",
            "death_knight"
        ),
        "pandaren": (
            "warrior", "hunter", "rogue", "priest", "shaman", "mage", "monk"
        ),
        "tauren": (
            "warrior", "paladin", "hunter", "priest", "shaman", "monk", "druid",
            "death_knight"
        ),
        "troll": (
            "warrior", "hunter", "rogue", "priest", "shaman", "mage", "warlock",
            "monk", "druid", "death_knight"
        ),
        "undead": (
            "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk",
            "death_knight"
        ),
        "nightborne": (
            "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk"
        ),
        "highmountain_tauren": ("warrior", "hunter", "shaman", "monk", "druid"),
        "maghar_orc": ("warrior", "hunter", "rogue", "priest", "shaman", "mage", "monk")
    }
}

__race_translations = {
    "draenei": {
        'en_US': 'Draenei',
        'it_IT': 'Draenei',
        'de_DE': 'Draenei',
        'fr_FR': 'Draeneï',
        'ru_RU': 'Дреней',
        'es_ES': 'Draenei',
        'ko_KR': '드레나이',
        'cn_CN': '德莱尼'
    },
    "dwarf": {
        'en_US': 'Dwarf',
        'it_IT': 'Nano',
        'de_DE': 'Zwerg',
        'fr_FR': 'Nain',
        'ru_RU': 'Дворф',
        'es_ES': 'Enano',
        'ko_KR': '드워프',
        'cn_CN': '矮人'
    },
    "gnome": {
        'en_US': 'Gnome',
        'it_IT': 'Gnomo',
        'de_DE': 'Gnom',
        'fr_FR': 'Gnome',
        'ru_RU': 'Гном',
        'es_ES': 'Gnomo',
        'ko_KR': '노움',
        'cn_CN': '侏儒'
    },
    "human": {
        'en_US': 'Human',
        'it_IT': 'Umano',
        'de_DE': 'Mensch',
        'fr_FR': 'Humain',
        'ru_RU': 'Человек',
        'es_ES': 'Humano',
        'ko_KR': '인간',
        'cn_CN': '人类'
    },
    "night_elf": {
        'en_US': 'Night Elf',
        'it_IT': 'Elfo della Notte',
        'de_DE': 'Nachtelf',
        'fr_FR': 'Elfe de la nuit',
        'ru_RU': 'Ночной эльф',
        'es_ES': 'Elfo de la noche',
        'ko_KR': '나이트 엘프',
        'cn_CN': '暗夜精灵'
    },
    "worgen": {
        'en_US': 'Worgen',
        'it_IT': 'Worgen',
        'de_DE': 'Worgen',
        'fr_FR': 'Worgen',
        'ru_RU': 'Ворген',
        'es_ES': 'Huargen',
        'ko_KR': '늑대인간',
        'cn_CN': '狼人'
    },
    "void_elf": {
        'en_US': 'Void Elf',
        'it_IT': 'Elfo del Vuoto',
        'de_DE': 'Leerenelf',
        'fr_FR': 'Elfe du Vide',
        'ru_RU': 'Эльф Бездны',
        'es_ES': 'Elfo del Vacío',
        'ko_KR': '공허 엘프',
        'cn_CN': '虚空精灵'
    },
    "lightforged_draenei": {
        'en_US': 'Lightforged Draenei',
        'it_IT': 'Draenei Forgialuce',
        'de_DE': 'Lichtgeschmiedeter Draenei',
        'fr_FR': 'Draeneï sancteforge',
        'ru_RU': 'Озаренный дреней',
        'es_ES': 'Draenei forjado por la Luz',
        'ko_KR': '빛벼림 드레나이',
        'cn_CN': '光铸德莱尼'
    },
    "dark_iron_dwarf": {
        'en_US': 'Dark Iron Dwarf',
        'it_IT': 'Nano Ferroscuro',
        'de_DE': 'Dunkeleisenzwerg',
        'fr_FR': 'Nain sombrefer',
        'ru_RU': 'Дворф из клана Черного Железа',
        'es_ES': 'Enano Hierro Negro',
        'ko_KR': '검은무쇠 드워프',
        'cn_CN': '黑铁矮人'
    },
    "blood_elf": {
        'en_US': 'Blood Elf',
        'it_IT': 'Elfo del Sangue',
        'de_DE': 'Blutelf',
        'fr_FR': 'Elfe de sang',
        'ru_RU': 'Эльф крови',
        'es_ES': 'Elfo de sangre',
        'ko_KR': '블러드 엘프',
        'cn_CN': '血精灵'
    },
    "goblin": {
        'en_US': 'Goblin',
        'it_IT': 'Goblin',
        'de_DE': 'Goblin',
        'fr_FR': 'Gobelin',
        'ru_RU': 'Гоблин',
        'es_ES': 'Goblin',
        'ko_KR': '고블린',
        'cn_CN': '地精'
    },
    "orc": {
        'en_US': 'Orc',
        'it_IT': 'Orco',
        'de_DE': 'Orc',
        'fr_FR': 'Orc',
        'ru_RU': 'Орк',
        'es_ES': 'Orco',
        'ko_KR': '오크',
        'cn_CN': '兽人'
    },
    "pandaren": {
        'en_US': 'Pandaren',
        'it_IT': 'Pandaren',
        'de_DE': 'Pandaren',
        'fr_FR': 'Pandaren',
        'ru_RU': 'Пандарен',
        'es_ES': 'Pandaren',
        'ko_KR': '판다렌',
        'cn_CN': '熊猫人'
    },
    "tauren": {
        'en_US': 'Tauren',
        'it_IT': 'Tauren',
        'de_DE': 'Tauren',
        'fr_FR': 'Tauren',
        'ru_RU': 'Таурен',
        'es_ES': 'Tauren',
        'ko_KR': '타우렌',
        'cn_CN': '牛头人'
    },
    "troll": {
        'en_US': 'Troll',
        'it_IT': 'Troll',
        'de_DE': 'Troll',
        'fr_FR': 'Troll',
        'ru_RU': 'Тролль',
        'es_ES': 'Trol',
        'ko_KR': '트롤',
        'cn_CN': '巨魔'
    },
    "undead": {
        'en_US': 'Undead',
        'it_IT': 'Non Morto',
        'de_DE': 'Untoter',
        'fr_FR': 'Mort-vivant',
        'ru_RU': 'Нежить',
        'es_ES': 'No-muerto',
        'ko_KR': '언데드',
        'cn_CN': '亡灵'
    },
    "nightborne": {
        'en_US': 'Nightborne',
        'it_IT': 'Nobile Oscuro',
        'de_DE': 'Nachtgeborener',
        'fr_FR': 'Sacrenuit',
        'ru_RU': 'Ночнорожденный',
        'es_ES': 'Nocheterna',
        'ko_KR': '나이트본',
        'cn_CN': '夜之子'
    },
    "highmountain_tauren": {
        'en_US': 'Highmountain Tauren',
        'it_IT': 'Tauren di Alto Monte',
        'de_DE': 'Hochbergtauren',
        'fr_FR': 'Tauren de Haut-Roc',
        'ru_RU': 'Таурен Крутогорья',
        'es_ES': 'Tauren Monte Alto',
        'ko_KR': '높은산 타우렌',
        'cn_CN': '至高岭牛头人'
    },
    "maghar_orc": {
        'en_US': "Mag'har Orc",
        'it_IT': "Orco Mag'har",
        'de_DE': "Mag'har",
        'fr_FR': 'Orc mag’har',
        'ru_RU': "Маг'хар",
        'es_ES': "Orco Mag'har",
        'ko_KR': '마그하르 오크',
        'cn_CN': '玛格汉兽人'
    }
}

# bfa data
__trinket_list = [
    # dungeon trinkets
    Trinket( # atal'dazar
        "My'das Talisman", "158319", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # atal'dazar
        "Rezan's Gleaming Eye", "158712", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, False, True, False, False, source="Dungeon"
    ),
    Trinket( # atal'dazar
        "Vessel of Skittering Shadows", "159610", DUNGEON_ITEMLEVEL,
        TITANFORGE_CAP, TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    Trinket( # freehold
        "Harlan's Loaded Dice", "155881", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # Kings' Rest
        "Lustrous Golden Plumage", "159617", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # Shrine of the Storm
        "Briny Barnacle", "159619", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, False, True, False, False, source="Dungeon"
    ),
    Trinket( # Shrine of the Storm
        "Galecaller's Boon", "159614", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # Shrine of the Storm
        "Conch of Dark Whispers", "159620", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    Trinket( # Siege of Boralus
        "Dead-Eye Spyglass", "159623", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # Siege of Boralus
        "Hadal's Nautilus", "159622", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    Trinket( # Temple of Sethraliss
        "Tiny Electromental in a Jar", "158374", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # Temple of Sethraliss
        "Merektha's Fang", "158367", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, False, True, False, False, source="Dungeon"
    ),
    Trinket( # The Motherlode
        "Razdunk's Big Red Button", "159611", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, False, True, False, False, source="Dungeon"
    ),
    Trinket( # The Motherlode
        "Azerokk's Resonating Heart", "159612", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Dungeon"
    ),
    Trinket( # The Underrot
        "Lingering Sporepods", "159626", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, True, False, False, source="Dungeon"
    ),
    Trinket( # The Underrot
        "Rotcrusted Voodoo Doll", "159624", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    Trinket( # The Underrot
        "Vial of Animated Blood", "159625", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, False, True, False, False, source="Dungeon"
    ),
    Trinket( # Tol Dagor
        "Jes' Howler", "159627", DUNGEON_ITEMLEVEL, TITANFORGE_CAP, TRADER_TOKEN,
        False, False, True, False, False, source="Dungeon"
    ),
    Trinket( # Tol Dagor
        "Ignition Mage's Fuse", "159615", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    Trinket( # Waycrest Manor
        "Lady Waycrest's Music Box", "159631", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    Trinket( # Waycrest Manor
        "Balefire Branch", "159630", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Dungeon"
    ),
    # Trinket( # not obtainable
    #     "Cursed Captain's Charm", "161115", 290, TITANFORGE_CAP,
    #     TRADER_TOKEN, True, True, True, False, False
    # ),
    Trinket( # world boss
        "Azurethos' Singed Plumage", "161377", 355, TITANFORGE_CAP, TRADER_TOKEN,
        False, True, False, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "Drust-Runed Icicle", "161380", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
        True, False, False, False, source="World Boss"
    ),
    # Trinket( # ???
    #     "Dunewalker's Survival Kit", "161418", 340, TITANFORGE_CAP, TRADER_TOKEN,
    #     True, False, False, False, False
    # ),
    Trinket( # world boss
        "Galecaller's Beak", "161379", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
        False, True, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "Kraulok's Claw", "161419", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
        False, True, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "Permafrost-Encrusted Heart", "161381", 355, TITANFORGE_CAP, TRADER_TOKEN,
        True, False, False, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "Plume of the Seaborne Avian", "161378", 355, TITANFORGE_CAP, TRADER_TOKEN,
        True, False, False, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "Prism of Dark Intensity", "161376", 355, TITANFORGE_CAP, TRADER_TOKEN,
        False, False, True, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "Spiritbound Voodoo Burl", "161412", 355, TITANFORGE_CAP, TRADER_TOKEN, True,
        False, False, False, False, source="World Boss"
    ),
    Trinket( # world boss
        "T'zane's Barkspines", "161411", 340, TITANFORGE_CAP, TRADER_TOKEN, False,
        True, False, False, False, source="World Boss"
    ),
    Trinket( # inscription
        "Darkmoon Deck: Squalls", "159126", 355, 355,
        355, False, True, False, False, False, source="Profession"
    ),
    Trinket( # inscription
        "Darkmoon Deck: Fathoms", "159125", 355, 355,
        355, True, False, True, False, False, source="Profession"
    ),
    Trinket( # alchemy
        "Surging Alchemist Stone", "152632", 300, 300,
        300, True, True, True, False, False, source="Profession"
    ),
    Trinket( # world quest
        "Plunderbeard's Flask", "158164", WORLD_QUEST_ITEMLEVEL, TITANFORGE_CAP,
        TRADER_TOKEN, True, True, True, False, False, source="World Quest"
    ),
    Trinket( # Uldir
        "Frenetic Corpuscle", "160648", 340, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Raid"
    ),
    Trinket( # Uldir
        "Construct Overcharger", "160652", 340, TITANFORGE_CAP,
        TRADER_TOKEN, True, False, False, False, False, source="Raid"
    ),
    Trinket(  # Uldir
        "Vigilant's Bloodshaper", "160651", 340, TITANFORGE_CAP,
        TRADER_TOKEN, False, True, False, False, False, source="Raid"
    ),
    Trinket( # Tol Dagor
        name="Kul Tiran Cannonball Runner", item_id="159628", min_itemlevel=WORLD_QUEST_ITEMLEVEL, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="Dungeon"
    ),
    Trinket(  # Uldir
        name="Vanquished Tendril of G'huun", item_id="160654", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="Raid"
    ),
    Trinket(  # world drop
        name="Landoi's Scrutiny", item_id="163935", min_itemlevel=350, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Drop"
    ),
    Trinket(  # world drop
        name="'Bygone Bee' Almanac", item_id="163936", min_itemlevel=350, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="World Drop"
    ),
    Trinket(  # world drop
        name="Leyshock's Grand Compilation", item_id="163937", min_itemlevel=350, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="World Drop"
    ),
    Trinket( # wq
        name="Kaja-fied Banana", item_id="161125", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # uldir
        name="Syringe of Bloodborne Infirmity", item_id="160655", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="Raid"
    ),
    Trinket(  # uldir
        name="Disc of Systematic Regression", item_id="160650", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="Raid"
    ),
    Trinket(  # uldir
        name="Twitching Tentacle of Xalzaix", item_id="160656", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="Raid"
    ),
    Trinket(  # alchemy
        name="Endless Tincture of Fractional Power", item_id="152636", min_itemlevel=300, max_itemlevel=300,
        max_itemlevel_drop=300, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="Profession"
    ),
    Trinket(  # stormsong valley
        name="Galewind Chimes", item_id="155568", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # wq
        name="Gilded Loa Figurine", item_id="158153", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # wq
        name="Emblem of Zandalar", item_id="158154", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # wq
        name="Dinobone Charm", item_id="158155", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # wq
        name="Pearl Diver's Compass", item_id="158162", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # wq
        name="First Mate's Spyglass", item_id="158163", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # stormsong valley
        name="Whirlwing's Plumage", item_id="158215", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # stormsong valley
        name="Living Oil Cannister", item_id="158216", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    # Trinket(  # stormsong valley - tank
    #     name="Dadalea's Wing", item_id="158218", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
    #     max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True
    # ),
    Trinket(  # stormsong valley
        name="Vial of Storms", item_id="158224", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # stormsong valley
        name="Doom Shroom", item_id="158555", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # waycrest manor
        name="Gore-Crusted Butcher's Block", item_id="159616", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="Dungeon"
    ),
    Trinket(  # stormsong valley
        name="Snowpelt Mangler", item_id="160263", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # nazmir
        name="Incessantly Ticking Clock", item_id="161113", min_itemlevel=325, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
   Trinket(  # vol'dun
        name="Ravasaur Skull Bijou", item_id="161119", min_itemlevel=325, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # nazmir
        name="Crawg Gnawed Femur", item_id="163703", min_itemlevel=325, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # airdrop
        name="Dread Gladiator's Badge", item_id="161902", min_itemlevel=325, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="PvP"
    ),
    Trinket(  # warfront world boss
        name="Lion's Grace", item_id="161472", min_itemlevel=370, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # warfront world boss
        name="Lion's Guile", item_id="161473", min_itemlevel=370, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # warfront world boss
        name="Lion's Strength", item_id="161474", min_itemlevel=370, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # warfront world boss
        name="Doom's Fury", item_id="161463", min_itemlevel=370, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # warfront world boss
        name="Doom's Hatred", item_id="161461", min_itemlevel=370, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # warfront world boss
        name="Doom's Wake", item_id="161462", min_itemlevel=370, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # pvp
        name="Dread Gladiator's Insignia", item_id="161676", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="PvP"
    ),
    Trinket(  # pvp
        name="Dread Gladiator's Medallion", item_id="161674", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="PvP"
    ),
    Trinket(  # wq
        name="Berserker's Juju", item_id="161117", min_itemlevel=280, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="World Quest"
    ),
    Trinket(  # profession alchemy
        name="Emblazoned Alchemist Stone", item_id="166976", min_itemlevel=355, max_itemlevel=415,
        max_itemlevel_drop=355, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="Profession"
    ),
    Trinket(  # World Boss Dark Shore
        name="Ancient Knot of Wisdom", item_id="161417", min_itemlevel=355, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=355, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # World Boss Dark Shore
        name="Forest Lord's Razorleaf", item_id="166794", min_itemlevel=355, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=355, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # World Boss Dark Shore
        name="Knot of Ancient Fury", item_id="161413", min_itemlevel=355, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=355, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="World Boss"
    ),
    Trinket(  # Emissary
        name="Razzashi Tooth Medallion", item_id="165667", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Quest"
    ),
    Trinket(  # Emissary
        name="Moonstone of Zin-Azshari", item_id="165666", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="World Quest"
    ),
    Trinket(  # Emissary
        name="Ancient Tuskarr Sea Charm", item_id="165661", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="World Quest"
    ),
    Trinket(  # Emissary
        name="Sea Giant's Tidestone", item_id="165664", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=False, intellect=True, strength=False, melee=False, ranged=False, source="World Quest"
    ),
    Trinket(  # Emissary
        name="Kezan Stamped Bijou", item_id="165662", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Quest"
    ),
    Trinket(  # Emissary
        name="Chargestone of the Thunder King's Court", item_id="165660", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=True, intellect=False, strength=False, melee=False, ranged=False, source="World Quest"
    ),
    Trinket(  # Emissary
        name="Ritual Feather of Unng Ak", item_id="165665", min_itemlevel=340, max_itemlevel=TITANFORGE_CAP,
        max_itemlevel_drop=370, agility=False, intellect=False, strength=True, melee=False, ranged=False, source="World Quest"
    ),

    # Trinket(
    #     name="", item_id="", min_itemlevel=WORLD_QUEST_ITEMLEVEL, max_itemlevel=TITANFORGE_CAP,
    #     max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=False, melee=False, ranged=False
    # ),
]


def is_melee(wow_class, wow_spec):
    """True if spec is melee spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if role of the spec is 'melee'.
    """

    return get_role(wow_class, wow_spec) == "melee"


def is_ranged(wow_class, wow_spec):
    """True if spec is a ranged spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if role of the spec is 'ranged'.
    """

    return get_role(wow_class, wow_spec) == "ranged"


def get_mask_for_spec(wow_class, wow_spec):
    """Mask to get appropriate Trinkets.

    Arguments:
      wow_class {str} -- world of warcraft class name
      wow_spec {str} -- world of warcraft spec name

    Returns:
      tuple(main_stat_agi{bool}, main_stat_int{bool}, main_stat_str{bool}, melee{bool}, ranged{bool} ) -- Returns a bool tuple mask to match the True's with Trinket
    """

    melee = is_melee(wow_class, wow_spec)
    ranged = is_ranged(wow_class, wow_spec)
    main_stat = get_main_stat(wow_class, wow_spec)
    main_stat_agi = main_stat == "agi"
    main_stat_int = main_stat == "int"
    main_stat_str = main_stat == "str"

    return (main_stat_agi, main_stat_int, main_stat_str, melee, ranged)


def _compare_trinket_lists():
    import pkg_resources

    path = "equippable-items.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    # compare from wow data to local list
    print("Searching through equippable-items.json:")
    missing = 0
    for item in loaded_items:
        if item["inventoryType"] == 12 and item["itemLevel"] >= EXPANSION_START_ITEMLEVEL:
            found = False
            for trinket in __trinket_list:
                if trinket.get_name() == item["name"]:
                    found = True

            if not found:
                missing += 1
                print(
                    f"  {item['name']} not found in local list! id: {item['id']}")
    if missing:
        print(f"{missing} trinkets are missing.\n")

    print("Searching through local trinkets:")
    for trinket in __trinket_list:
        found = False

        for item in loaded_items:
            if int(trinket.get_id()) == int(item["id"]):
                found = True

        if not found:
            print(
                f"  {trinket.get_name()} not found in equippable-items.json! id: {trinket.get_id()}")


def get_trinkets_for_spec(wow_class: str, wow_spec: str) -> list:
    """New function to return all available trinkets for a spec

    Arguments:
      wow_class {str} -- name of the wow class
      wow_spec {str} -- name of the wow spec

    Returns:
      list[Trinket] -- List of all Trinkets
    """

    agility, intellect, strength, melee, ranged = get_mask_for_spec(
        wow_class, wow_spec
    )
    return_list = []
    for trinket in __trinket_list:
        if melee and trinket.melee:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel,
                trinket.max_itemlevel, trinket.max_itemlevel_drop
            ))
        elif ranged and trinket.ranged:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel,
                trinket.max_itemlevel, trinket.max_itemlevel_drop
            ))
        elif agility and trinket.agility:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel,
                trinket.max_itemlevel, trinket.max_itemlevel_drop
            ))
        elif intellect and trinket.intellect:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel,
                trinket.max_itemlevel, trinket.max_itemlevel_drop
            ))
        elif strength and trinket.strength:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel,
                trinket.max_itemlevel, trinket.max_itemlevel_drop
            ))
    return return_list

def get_race_translation(race:str ) -> dict:
    """Return the translation dict for a race.

    Arguments:
        race {str} -- wow race

    Returns:
        dict -- [description]
    """

    return __race_translations[race.lower().replace(" ", "_")]

def get_trinket_list() -> list:
    """Get a full trinket list for the ongoing expansion from equippable-items.json.

    Returns:
        list -- item list
    """

    import pkg_resources

    path = "equippable-items.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    item_list: list = []

    for item in loaded_items:
        if item["inventoryType"] == 12 and item["itemLevel"] >= 280:
            item_list.append(item)

    return item_list


def get_trinket_translation(trinket_name) -> dict:
    """Returns the translation dict for a trinket

    Arguments:
        trinket_name {[type]} -- [description]

    Returns:
        dict -- [description]
    """

    import pkg_resources

    path = "trinket_translations.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    try:
        return loaded_items[trinket_name]
    except Exception as e:
        raise LookupError("Translation not found for {}. {}".format(trinket_name, e))


def get_talent_blueprint(wow_class: str, wow_spec: str) -> str:
    """Returns a talent blueprint for the wow_class. 0 means non-dps relevant talents. 1 means dps relevant talent.

    Arguments:
        wow_class {string} -- [description]

    Keyword Arguments:
        wow_spec {str} -- [description] (default: {""})

    Returns:
        string -- 7 digits decsribing possible talent combinations. 0...non dps talent, 1...dps-talent
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["talents"]


def get_azerite_item_translation(item_name) -> dict:
    """Returns the translation dict for a trinket

    Arguments:
        trinket_name {[type]} -- [description]

    Returns:
        dict -- [description]
    """

    import pkg_resources

    path = "azerite_item_translations.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    try:
        return loaded_items[item_name]
    except Exception as e:
        raise LookupError("Translation not found for {}. {}".format(item_name, e))



def get_item_translation(item_name: str = "", item_id: int = None, item_list: list = None) -> dict:
    """Get the translation dictionary for an item. If item_list is provided, the lookup time is quicker.

    Keyword Arguments:
        item_name {str} -- English name of the Item (default: {""})
        item_id {int} -- Item ID (default: {None})
        item_list {list} -- item_list, can be generated with get_trinket_list() (default: {None})

    Raises:
        LookupError -- If no translation is found in data

    Returns:
        dict -- {language_shorthand: translation}
    """

    if item_list:
        loaded_items = item_list

    else:
        import pkg_resources

        path = "equippable-items.json"

        with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

            loaded_items = json.load(f, encoding="UTF-8")

    for item in loaded_items:
        if item_name and item_name == item["name"]:
            return item["names"]
        elif item_id and int(item_id) == item["id"]:
            return item["names"]

    raise LookupError("Translation not found for {}{}".format(item_name, item_id))

def get_trait_translation_dict():
    """Return the dict of all azerite trait translations.

    Returns:
        dict -- {Name:{language:translation}}
    """

    import pkg_resources

    path = "azerite_trait_translations.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_translations = json.load(f, encoding="UTF-8")

    return loaded_translations


def get_trait_translation(trait_name: str = "", translation_dict: dict = None) -> dict:
    """Return the translation dict of one trait. Providing the translation_dict speeds up the process.

    Keyword Arguments:
        trait_name {str} -- [description] (default: {""})
        translation_dict {dict} -- [description] (default: {None})

    Raises:
        LookupError -- [description]

    Returns:
        dict -- [description]
    """


    if translation_dict:
        loaded_translations = translation_dict
    else:
        import pkg_resources

        path = "azerite_trait_translations.json"

        with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

            loaded_translations = json.load(f, encoding="UTF-8")

    try:
        return loaded_translations[trait_name]
    except Exception:
        for name in loaded_translations:
            if name in trait_name:
                try:
                    return loaded_translations[name]
                except Exception:
                    raise LookupError("Translation not found for {}".format(trait_name))


def get_second_trinket_for_spec(wow_class, wow_spec):
    """Returns a vers stat stick for the spec.

    Arguments:
        wow_class {[type]} -- [description]
        wow_spec {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    main_stat = get_main_stat(wow_class, wow_spec)
    if main_stat == "agi":
        # "Stat Stick (Versatility)", "142506,bonus_id=607"
        return ',id={}'.format("142506,bonus_id=607")
    if main_stat == "int":
        # "Stat Stick (Versatility)", "142507,bonus_id=607"
        return ',id={}'.format("142507,bonus_id=607")
    if main_stat == "str":
        # "Stat Stick (Versatility)", "142508,bonus_id=607"
        return ',id={}'.format("142508,bonus_id=607")


def get_trinket_id(trinket_name):
    """Return the trinket id as string. Function can handly extended names like 'Pancakes Specialtext' and will still return the ID of 'Pancakes' in this case.

    Arguments:
      trinket_name {str} -- trinket name

    Returns:
      str -- item ID as string
    """

    for trinket in __trinket_list:
        # ordered like this to allows look ups of extended names like "Norgannons + 15" to yield an ID
        if trinket.name in trinket_name:
            return trinket.item_id


def get_trinket(name: str ="", item_id: str ="") -> Trinket:
    """Return Trinket of matching name or item_id. One must be provided. Else None will be returned.

    Keyword Arguments:
      name {str} -- name of the trinket (default: {""})
      item_id {str} -- id of the trinket (default: {""})

    Returns:
      Trinket or None -- Instance of Trinket class
    """

    if name or item_id:
        for trinket in __trinket_list:
            if trinket.name == name or trinket.item_id == item_id:
                return trinket
    return None


def get_azerite_traits(wow_class: str, wow_spec: str) -> dict:
    """Get all azerite traits for the given wow class and spec.

    Arguments:
        wow_class {str} -- [description]
        wow_spec {str} -- [description]

    Raises:
        e -- [description]

    Returns:
        dict -- Dict{spell_id: str : Dict{description: str : str, max_itemlevel: str : int, max_stack: str : int, min_itemlevel: str : int, name: str : str, spell_id: str : str, trait_id: str : str}}
    """

    import pkg_resources

    path = "trait_list.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        traits = json.load(f, encoding="UTF-8")

    try:
        return traits[wow_class.title()][wow_spec.title()]
    except Exception as e:
        raise e


def get_azerite_items(wow_class: str, wow_spec: str) -> dict:
    """Return a dictionary of all azerite items for the given spec. Dictionary is organized by item slot. Items have all available traits for them, too.

    REQUIRED: 'equippable-items-live.json' and 'azerite-power-sets-live.json'
    https://www.raidbots.com/static/data/live/azerite-power-sets.json
    https://www.raidbots.com/static/data/live/equippable-items.json

    "head": [item, item, ...],
    "shoulders": [item, item, ...],
    "chest": [item, item, ...]

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      dictionary -- all available azerite items for the given spec
    """

    import pkg_resources

    path = "equippable-items.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    items: dict = {
        "head": [],
        "shoulders": [],
        "chest": []
    }
    item_type = {
        1: "head",
        3: "shoulders",
        5: "chest",  # ???
        20: "chest"  # ???
    }

    for item in loaded_items:
        if "azeritePowerSetId" in item:

            try:
                items[item_type[item["inventoryType"]]].append(item)
            except Exception:
                pass

    # enrich dict with azerite traits
    path = "azerite-power-sets.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:
        azerite_traits = json.load(f, encoding="UTF-8")

    for slot in items:
        for i in range(len(items[slot])):
            item = items[slot][i]
            try:
                items[slot][i]["azeriteTraits"] = azerite_traits[str(
                    items[slot][i]["azeritePowerSetId"])]
            except Exception:  # as e:
                # logger.error(e)
                # logger.error("slot: {}".format(slot))
                # logger.error("item: {}".format(item))
                # logger.error("item data: {}".format(items[slot][i]))
                # logger.error("azeritePowerSetId: {}".format(items[slot][i]["azeritePowerSetId"]))
                # logger.error(trait_dict[str(items[slot][i]["azeritePowerSetId"])])
                pass

    # create a new itemlist with only items for the wow spec/class
    response: dict = {}
    class_id = get_class_id(wow_class)
    spec_id = get_spec_id(wow_class, wow_spec)  # unused...for now

    for slot in items:
        # create slot in new dict
        if not slot in response:
            response[slot] = []

        for item in items[slot]:
            new_trait_list = []

            for trait in item["azeriteTraits"]:
                if trait["classId"] == class_id and (trait["specUsable"] == [] or spec_id in trait["specUsable"]):
                    new_trait_list.append(trait)

            item["azeriteTraits"] = new_trait_list

            if item["azeriteTraits"]:
                # add item only to the response if it has traits for the givesn class/spec
                response[slot].append(item)

    return response


def get_azerite_tiers(wow_class: str, wow_spec: str, trait_id: str) -> int:
    """Get the tier number of an azerite trait.

    Arguments:
        wow_class {str} -- [description]
        wow_spec {str} -- [description]
        trait_id {str} -- [description]

    Returns:
        int -- [description]
    """

    traits = get_azerite_traits(wow_class, wow_spec)

    return traits[trait_id]["tiers"]


def get_all_trinkets():
    """Get a list of all known trinket names.

    Returns:
      list[trinket_name{str}] -- List of all trinket names.
    """

    all_trinkets = []
    for trinket in __trinket_list:
        all_trinkets.append(trinket.name)
    return all_trinkets


def get_talent_dict(wow_class: str, wow_spec: str, ptr: bool = False)->dict:
    """Return the dict of all talents available to this spec. Structur: row -> column -> name, spell_id

    Arguments:
        wow_class {str} -- [description]
        wow_spec {str} -- [description]

    Returns:
        dict -- row -> column -> name, spell_id
    """
    import pkg_resources

    file_name = "talent_list.json"
    if ptr:
        file_name = "talent_list_ptr.json"

    with open(pkg_resources.resource_filename(__name__, file_name), 'r', encoding="UTF-8") as f:
        talents = json.load(f, encoding="UTF-8")

    return talents[wow_class.title()][wow_spec.title()]

def __generate_talent_combinations(blueprint, wow_class, wow_spec):
    """Generate all talent combinations matching blueprint. You're an enduser? Use get_talent_combinations(...).

    Arguments:
      blueprint {str} -- [description]
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      list[talent_combination{str}] -- [description]
    """

    if not ("x" in blueprint or "-" in blueprint):
        return [blueprint]
    data_talents = get_dps_talents(wow_class, wow_spec)
    pattern = ""

    for i in range(0, 7):
        if (blueprint[i] == "-" or blueprint[i] == "x") and data_talents[i] == "0":
            pattern += "0"
        else:
            pattern += blueprint[i]

    combinations = []
    for first in range(4):
        for second in range(4):
            for third in range(4):
                for forth in range(4):
                    for fivth in range(4):
                        for sixth in range(4):
                            for seventh in range(4):
                                combination = str(first) + str(second) + str(third) + str(
                                    forth
                                ) + str(fivth) + str(sixth) + str(seventh)
                                add_it = True

                                # check whether the generated talent combination fits the wanted blueprint
                                for i in range(7):
                                    if (not (pattern[i] == "-" or pattern[i] == "x")
                                        ) and not combination[i] == pattern[i]:
                                        add_it = False
                                    if combination[i] == "0" and (
                                        pattern[i] == "-" or pattern[i] == "x"
                                    ):
                                        add_it = False
                                if add_it:
                                    combinations += [combination]

    return combinations


def is_talent_combination(talent_combination):
    """Check the talent_combination for valid format.

    Arguments:
      talent_combination {str} -- [description]

    Returns:
      bool -- True, if the format matches the required format of get_talent_combinations
    """

    if talent_combination == None:
        return False
    if not type(talent_combination) is str:
        return False
    if talent_combination == "":
        return True
    if len(talent_combination) == 7:
        for letter in talent_combination:
            if not (
                letter == "0" or letter == "1" or letter == "2" or letter == "3" or
                letter == "-" or letter == "x"
            ):
                return False
        return True
    elif len(talent_combination) == 2:
        for letter in talent_combination:
            if not (
                letter == "0" or letter == "1" or letter == "2" or letter == "3"
            ):
                return False
        return True
    # Would've been for talent combinations that set certain rows to a value without declaring anything else.
    # Like 42 would set the forth row to the second talent. 4253 would set 4. row to 2 and 5. to 3
    # elif len(talent_combination) % 2 == 0:
    #  for i in range(0, len(talent_combination)):
    #    if (i + 1) % 2 == 1 and not int(talent_combination[i]) in range(1,8):
    #      return False
    #    elif not int(talent_combination[i]) in range(0,4):
    #      return False
    #  return True
    else:
        return False


def get_talent_combinations(wow_class, wow_spec, user_input=""):
    """Get a list of all valid dps talent combinations for a wow_class and wow_spec. If user_input is given the provided mask is used for this genertion and pruning of the talent combination list.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Keyword Arguments:
      user_input {str} -- Mask to determine whether a combination is valid or not. Class inherent masks are used in addition to the user input. Input can either be empty, of len 2 or len 7. len two is understood as a mask for the last two valid dps rows. len seven is understood as a mask for all talent rows. Write 'x' or '-' as a placeholder. Example: '201xx03' will generate 9 talent combinations if both x are dps talents. (default: {""})

    Returns:
      list[talent_combination{str}] -- List of all valied talent combinations for a class.
    """

    combinations = []

    if user_input == "" or user_input == None:
        combinations = __generate_talent_combinations(
            "xxxxxxx", wow_class, wow_spec
        )

    elif len(user_input) == 2:
        combinations = __generate_talent_combinations(
            "xxxxx" + user_input, wow_class, wow_spec
        )

    elif len(user_input) == 7:
        combinations = __generate_talent_combinations(
            user_input, wow_class, wow_spec
        )

    else:
        # something unexpected occured
        return None

    return combinations


def get_classes():
    """Get a list of all wow classes.

    Returns:
      list[wow_class_name{str}] -- List of all wow class names.
    """

    classes = []
    for wow_class in __class_data:
        classes.append(wow_class)
    return classes


def get_classes_specs():
    """Get a list of all wow classes and wow specs.

    Returns:
      List[Tuple(String, String)] -- List of all wow_class and wow_spec combinations
    """

    class_list = get_classes()
    full_list = []
    for wow_class in class_list:
        for spec in get_specs(wow_class):
            full_list.append((wow_class, spec))
    return full_list


def get_races() -> list:
    """Get a list of all wow race names.

    Returns:
      list[wow_race_name{str}] -- List of all wow race names
    """

    races: list = []
    for faction in __races.keys():
        for race in __races[faction].keys():
            if not race in races:
                races.append(race)
    return races


def get_races_for_class(wow_class: str) -> list:
    """Get a list of all available races to the given wow_class.

    Arguments:
      wow_class {str} -- wow class name

    Returns:
      list[wow_race_name{str}] -- List of all available races to the given wow_class.
    """

    race_list: list = []
    for faction in __races.keys():
        for race in __races[faction].keys():
            # additionally prevent double races like pandaren
            if str(wow_class).lower() in __races[faction][race
                                                          ] and not race in race_list:
                race_list.append(race)
    return race_list


def get_role(wow_class: str, wow_spec: str) -> str:
    """Get the role of the given wow class and wow spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      str -- role ('ranged'/'melee')
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["role"] # type: ignore


def get_class_id(wow_class: str) -> int:
    """Get the wow ID of the given class.

    Arguments:
      wow_class {str} -- [description]

    Returns:
      int -- wow_class_id
    """

    return __class_data[wow_class.title()]["id"] # type: ignore


def get_spec_id(wow_class: str, wow_spec: str) -> int:
    """Get the ID of a given spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      int -- wow_spec_id
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["id"] # type: ignore


def get_main_stat(wow_class, wow_spec):
    """Get the main stat of a class and spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      str -- main stat (agi / int / str)
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["stat"]


def get_dps_talents(wow_class, wow_spec):
    """Return the dps talent mask for a spec. DPS talents are represented by a '1', non-DPS talent are represented by a '0' (zero).

    Arguments:
      wow_class {str} -- [description]

    Keyword Arguments:
      wow_spec {str} -- wow spec, usually not needed as of Legion. Specs of one class share the same utility rows, not necessarily the talents there,though (default: {""})

    Returns:
      str -- talent mask, e.g. '1011101'
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["talents"]


def get_specs(wow_class):
    """Get a list of spec names for a given wow class.

    Arguments:
      wow_class {str} -- [description]

    Returns:
      list[wow_spec{str}] -- List of all available wow specs of the wow_class.
    """

    spec_collection = []
    for spec in __class_data[wow_class.title()]["specs"]:
        spec_collection.append(spec)
    return spec_collection


def is_class(wow_class):
    """True, if wow_class is class of WoW.

    Arguments:
      wow_class {str} -- [description]

    Returns:
      boold -- True if wow_class is class of WoW.
    """

    for base_class in get_classes():
        if wow_class.lower() == base_class.lower():
            return True
    return False


def is_race(race):
    """True, if race is a wow race.

    Arguments:
      race {str} -- [description]

    Returns:
      bool -- True, if race is a wow race.
    """

    if race in get_races():
        return True
    return False


def is_spec(wow_spec):
    """True, if wow_spec is a spec in WoW.

    Arguments:
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if wow_spec is a spec in WoW.
    """

    spec_list = []
    classes = get_classes()
    for wow_class in classes:
        specs = get_specs(wow_class)
        for spec in specs:
            spec_list.append(spec)
    for spec in spec_list:
        if wow_spec.lower() == spec.lower():
            return True
    return False


def is_class_spec(wow_class, wow_spec):
    """True, if wow_spec and wow_class match.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if wow_class and wow_spec match.
    """

    if is_class(wow_class):
        if is_spec(wow_spec):
            for spec in get_specs(wow_class):
                if wow_spec.lower() == spec.lower():
                    return True
    return False


def is_dps_talent_combination(talent_combination, wow_class):
    """Determines whether a given talent combination is a valid talent combination of the wow_class.

    Arguments:
      talent_combination {str} -- [description]
      wow_class {str} -- [description]

    Returns:
      bool -- True, if all dps talent rows have a talent selected and all utility rows have no talent selected.
    """

    for i in range(0, 7):
        if talent_combination[i] == "0" and __class_data[wow_class]["talents"
                                                                    ][i] == "1":
            return False
        elif not talent_combination[i] == "0" and __class_data[wow_class][
            "talents"
        ][i] == "0":
            return False
    return True
