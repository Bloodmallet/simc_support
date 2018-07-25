# -*- coding: utf-8 -*-
## Utility file for class specialisations
## Contains wow classes, specs, dps talent rows,
## races, trinkets

import json

# these values are used throughout the code to determine itemlevel "borders" of items
TRADER_TOKEN = 192  # usually used as a catch up mechanic, drops usually all items from previous content
WORLD_QUEST_ITEMLEVEL = 300
DUNGEON_ITEMLEVEL = 310  # standard dungeon itemlevel (normal, max level dungeon)
M_PLUS_ITEMLEVEL = 220  # highest available itemlevel from m+ dungeons. weekly chest is NOT included here
TITANFORGE_CAP = 255  # currently highest itemlevel titanforging cap


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
    legendary=False
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


__class_data = {
  "Death_Knight": {
    "talents": "1101011",
    "id": 6,
    "specs": {
      "Blood": {
        "role": "melee",
        "stat": "str",
        "id": 250,
      },
      "Frost": {
        "role": "melee",
        "stat": "str",
        "id": 251,
      },
      "Unholy": {
        "role": "melee",
        "stat": "str",
        "id": 252,
      }
    }
  },
  "Demon_Hunter": {
    "talents": "1110111",
    "id": 12,
    "specs": {
      "Havoc": {
        "role": "melee",
        "stat": "agi",
        "id": 577,
      },
      "Vengeance": {
        "role": "melee",
        "stat": "agi",
        "id": 581,
      }
    }
  },
  "Druid": {
    "talents": "1000111",
    "id": 11,
    "specs": {
      "Balance": {
        "role": "ranged",
        "stat": "int",
        "id": 102,
      },
      "Feral": {
        "role": "melee",
        "stat": "agi",
        "id": 103,
      },
      "Guardian": {
        "role": "melee",
        "stat": "agi",
        "id": 104,
      }
    }
  },
  "Hunter": {
    "talents": "1101011",
    "id": 3,
    "specs": {
      "Beast_Mastery": {
        "role": "ranged",
        "stat": "agi",
        "id": 253,
      },
      "Marksmanship": {
        "role": "ranged",
        "stat": "agi",
        "id": 254,
      },
      "Survival": {
        "role": "melee",
        "stat": "agi",
        "id": 255,
      }
    }
  },
  "Mage": {
    "talents": "1011011",
    "id": 8,
    "specs": {
      "Arcane": {
        "role": "ranged",
        "stat": "int",
        "id": 62,
      },
      "Fire": {
        "role": "ranged",
        "stat": "int",
        "id": 63,
      },
      "Frost": {
        "role": "ranged",
        "stat": "int",
        "id": 64,
      }
    }
  },
  "Monk": {
    "talents": "1010011",
    "id": 10,
    "specs": {
      "Brewmaster": {
        "role": "melee",
        "stat": "agi",
        "id": 268,
      },
      "Windwalker": {
        "role": "melee",
        "stat": "agi",
        "id": 269,
      }
    }
  },
  "Paladin": {
    "talents": "1101001",
    "id": 2,
    "specs": {
      "Protection": {
        "role": "melee",
        "stat": "str",
        "id": 66,
      },
      "Retribution": {
        "role": "melee",
        "stat": "str",
        "id": 70,
      }
    }
  },
  "Priest": {
    "talents": "1010111",
    "id": 5,
    "specs": {
      "Shadow": {
        "role": "ranged",
        "stat": "int",
        "id": 258,
      }
    }
  },
  "Rogue": {
    "talents": "1110111",
    "id": 4,
    "specs": {
      "Assassination": {
        "role": "melee",
        "stat": "agi",
        "id": 259,
      },
      "Outlaw": {
        "role": "melee",
        "stat": "agi",
        "id": 260,
      },
      "Subtlety": {
        "role": "melee",
        "stat": "agi",
        "id": 261,
      }
    }
  },
  "Shaman": {
    "talents": "1101011",
    "id": 7,
    "specs": {
      "Elemental": {
        "role": "ranged",
        "stat": "int",
        "id": 262,
      },
      "Enhancement": {
        "role": "melee",
        "stat": "agi",
        "id": 263,
      }
    }
  },
  "Warlock": {
    "talents": "1101011",
    "id": 9,
    "specs": {
      "Affliction": {
        "role": "ranged",
        "stat": "int",
        "id": 265,
      },
      "Demonology": {
        "role": "ranged",
        "stat": "int",
        "id": 266,
      },
      "Destruction": {
        "role": "ranged",
        "stat": "int",
        "id": 267,
      }
    }
  },
  "Warrior": {
    "talents": "1010111",
    "id": 1,
    "specs": {
      "Arms": {
        "role": "melee",
        "stat": "str",
        "id": 71,
      },
      "Fury": {
        "role": "melee",
        "stat": "str",
        "id": 72,
      },
      "Protection": {
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
      "death_knight"
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
    #"dark_iron_dwarf": ("shaman")
  },
  "horde": {
    "blood_elf": (
      "warrior", "paladin", "hunter", "rogue", "priest", "mage", "warlock",
      "monk", "death_knight"
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
    #"maghar_orc": ("shaman")
  }
}

# bfa data
__trinket_list = [
  # dungeon trinkets
  Trinket(
    "My'das Talisman", "158319", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Rezan's Gleaming Eye", "158712", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Vessel of Skittering Shadows", "159610", DUNGEON_ITEMLEVEL,
    TITANFORGE_CAP, TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Harlan's Loaded Dice", "155881", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Lustrous Golden Plumage", "159617", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Briny Barnacle", "159619", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Galecaller's Boon", "159614", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Conch of Dark Whispers", "159620", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Dead-Eye Spyglass", "159623", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Hadal's Nautilus", "159622", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Tiny Electromental in a Jar", "158374", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Merektha's Fang", "158367", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Razdunk's Big Red Button", "159611", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Tik'ali's Resonating Heart", "159612", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  # The Underrot
  Trinket(
    "Lingering Sporepods", "159626", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, True, False, False
  ),
  Trinket(
    "Rotcrusted Voodoo Doll", "159624", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Vial of Animated Blood", "159625", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Jes' Howler", "159627", DUNGEON_ITEMLEVEL, TITANFORGE_CAP, TRADER_TOKEN,
    False, False, True, False, False
  ),
  Trinket(
    "Cannonball Hurdler", "159628", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Ignition Mage's Fuse", "159615", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Lady Waycrest's Music Box", "159631", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Balefire Branch", "159630", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Gorecrusted Butcher's Block", "159616", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Perl Diver's Compass", "158162", WORLD_QUEST_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, True, False, False, False
  ),
  Trinket(
    "Zandalari Dinobone Charm", "158155", WORLD_QUEST_ITEMLEVEL,
    TITANFORGE_CAP, TRADER_TOKEN, True, True, True, False, False
  ),
  Trinket(
    "Zandalari Bijou", "158154", WORLD_QUEST_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, True, True, False, False
  ),
  Trinket(
    "Zandalari Loa Figurine", "158153", WORLD_QUEST_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, True, True, False, False
  ),
  Trinket(
    "Cursed Captain's Charm", "161115", WORLD_QUEST_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, True, True, False, False
  ),
  Trinket(
    "Azurethos'Singed Plumage", "161377", 355, TITANFORGE_CAP, TRADER_TOKEN,
    False, True, False, False, False
  ),
  Trinket(
    "Doom's Fury", "161463", 355, TITANFORGE_CAP, TRADER_TOKEN, False, False,
    True, False, False
  ),
  Trinket(
    "Doom's Hatred", "161461", 355, TITANFORGE_CAP, TRADER_TOKEN, False, True,
    False, False, False
  ),
  Trinket(
    "Doom's Wake", "161462", 355, TITANFORGE_CAP, TRADER_TOKEN, True, False,
    False, False, False
  ),
  Trinket(
    "Drust-Runed Icicle", "161380", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    True, False, False, False
  ),
  Trinket(
    "Dunewalker's Survival Kit", "161418", 355, TITANFORGE_CAP, TRADER_TOKEN,
    True, False, False, False, False
  ),
  Trinket(
    "Galecaller's Beak", "161379", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    False, True, False, False
  ),
  Trinket(
    "Hurricane Heart", "161416", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    False, True, False, False
  ),
  Trinket(
    "Knot of Spiritual Fury", "161413", 355, TITANFORGE_CAP, TRADER_TOKEN,
    False, False, True, False, False
  ),
  Trinket(
    "Kraulok's Claw", "161419", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    False, True, False, False
  ),
  Trinket(
    "Permafrost-Encrusted Heart", "161381", 355, TITANFORGE_CAP, TRADER_TOKEN,
    True, False, False, False, False
  ),
  Trinket(
    "Plume of the Seaborne Avian", "161378", 355, TITANFORGE_CAP, TRADER_TOKEN,
    True, False, False, False, False
  ),
  Trinket(
    "Prism of Dark Intensity", "161376", 355, TITANFORGE_CAP, TRADER_TOKEN,
    False, False, True, False, False
  ),
  Trinket(
    "Razorcrest of the Enraged Matriarch", "161415", 355, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Sandscoured Idol", "161417", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    True, False, False, False
  ),
  Trinket(
    "Spiritbound Burl", "161412", 355, TITANFORGE_CAP, TRADER_TOKEN, True,
    False, False, False, False
  ),
  Trinket(
    "Sublimating Iceshard", "161382", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    False, True, False, False
  ),
  Trinket(
    "T'zane's Barkspines", "161411", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    True, False, False, False
  ),
  Trinket(
    "Tear of the Void", "161374", 355, TITANFORGE_CAP, TRADER_TOKEN, False,
    True, False, False, False
  ),
  Trinket(
    "Void Portal Stone", "161375", 355, TITANFORGE_CAP, TRADER_TOKEN, True,
    False, False, False, False
  ),
  Trinket(
    "Wing Bone of the Budding Tempest", "161414", 355, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  # Trinket(
  #   "", "", DUNGEON_ITEMLEVEL, TITANFORGE_CAP, TRADER_TOKEN,
  #   False, False, False, False, False
  # ),
]


# legion data
## Available types:
##   legendary - legendary trinkets for everyone
##   shared    - trinkets for everyone
##   melee     - agi + str (melee + sv hunter)
##   ranged    - int + agi (caster + bm/mm hunter)
##   agi       - pure agi (leather wearer + hunter)
##   int       - pure int (pure caster)
##   str       - pure str (plate wearer)

## legendary trinkets for everyone
##
# {"source": [ [ "name", "id", minitemlevel, maxitemlevel, maxdropitemlevel ], ] }
legendary_trinkets = {}
legendary_trinkets["legendary"] = [
  ["Kil'jaeden's Burning Wish", "144259", 265, 265, 265],
  ["Aman'Thul's Vision", "154172", 280, 280, 280],
]

## Usable by everyone
shared_trinkets = {}
shared_trinkets["dungeon"] = [
  ["Chrono Shard", "137419", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL],
  ["Horn of Valor", "133642", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL],
  ["Toe Knee's Promise", "142164", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL],
]
# shared_trinkets["crafted"] = [
#   ["Infernal Alchemist Stone", "127842", 182, 900, 900],
#   ["Astral Alchemist Stone", "151607", 885, 935, 935],
# ]
shared_trinkets["world"] = [
  ["Unstable Arcanocrystal", "141482", 172, TITANFORGE_CAP, TRADER_TOKEN],
]

## Usable by melee classes (survival hunters)
melee_trinkets = {}
# melee_trinkets["crafted"] = [
#   ["Darkmoon Deck: Dominion", "128705", 815, 900, 900],
# ]
melee_trinkets["dungeon"] = [[
  "Bloodstained Handkerchief", "142159", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Chaos Talisman", "137459", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Eye of Command", "142167", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], [
  "Faulty Countermeasure", "137539", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Gift of Radiance", "133647", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Giant Ornamental Pearl", "137369", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Mark of Dargrul", "137357", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Memento of Angerboda", "133644", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Nightmare Egg Shell", "137312", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Spiked Counterweight", "136715", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Terrorbound Nexus", "137406", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Tiny Oozeling in a Jar", "137439", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Windscar Whetstone", "137486", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL]]
melee_trinkets["emerald_nightmare"] = [[
  "Nature's Call", "139334", 162, TITANFORGE_CAP, TRADER_TOKEN
], ["Ravaged Seed Pod", "139320", 162, TITANFORGE_CAP, TRADER_TOKEN], [
  "Spontaneous Appendages", "139325", 162, TITANFORGE_CAP, TRADER_TOKEN
]]
melee_trinkets["nighthold"] = [
  ["Draught of Souls", "140808", 170, TITANFORGE_CAP, TRADER_TOKEN],
]
melee_trinkets["tomb_of_sargeras"] = [[
  "Infernal Cinders", "147009", 182, TITANFORGE_CAP, 930
], ["Umbral Moonglaives", "147012", 182, TITANFORGE_CAP,
    930], ["Vial of Ceaseless Toxins", "147011", 182, TITANFORGE_CAP,
           930], ["Specter of Betrayal", "151190", 182, TITANFORGE_CAP, 940]]
melee_trinkets["antorus"] = [
  ["Gorshalach's Legacy", "152093", 195, TITANFORGE_CAP, 240],
  ["Seeping Scourgewing", "151964", 195, TITANFORGE_CAP, 240],
]

## Usable by casters and hunters
ranged_trinkets = {}
ranged_trinkets["dungeon"] = [[
  "Aran's Relaxing Ruby", "142157", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Caged Horror", "136716", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Corrupted Starlight", "137301", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], [
  "Deteriorated Construct Core", "142165", 182, TITANFORGE_CAP,
  M_PLUS_ITEMLEVEL
], [
  "Elementium Bomb Squirrel Generator", "137446", 182, TITANFORGE_CAP,
  M_PLUS_ITEMLEVEL
], ["Eye of Skovald", "133641", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Figurehead of the Naglfar", "137329", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Moonlit Prism", "137541", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Mrrgria's Favor", "142160", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], [
  "Naraxas' Spiked Tongue", "137349", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], [
  "Oakheart's Gnarled Root", "137306", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Obelisk of the Void", "137433", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Stormsinger Fulmination Charge", "137367", 182, TITANFORGE_CAP,
  M_PLUS_ITEMLEVEL
]]
ranged_trinkets["emerald_nightmare"] = [[
  "Twisting Wind", "139323", 162, TITANFORGE_CAP, TRADER_TOKEN
], ["Unstable Horrorslime", "138224", 162, TITANFORGE_CAP, TRADER_TOKEN]]
ranged_trinkets["nighthold"] = [[
  "Fury of the Burning Sky", "140801", 170, TITANFORGE_CAP, TRADER_TOKEN
], ["Icon of Rot", "140798", 170, TITANFORGE_CAP, TRADER_TOKEN]]
ranged_trinkets["tomb_of_sargeras"] = [
  ["Spectral Thurible", "147018", 182, TITANFORGE_CAP, 930],
  ["Tarnished Sentinel Medallion", "147017", 182, TITANFORGE_CAP, 930],
  ["Terror From Below", "147016", 182, TITANFORGE_CAP, 930],
  ["Tome of Unraveling Sanity", "147019", 182, TITANFORGE_CAP, 940],
]
ranged_trinkets["antorus"] = [
  ["Prototype Personnel Decimator", "151962", 195, TITANFORGE_CAP, 240],
  ["Terminus Signaling Beacon", "151969", 195, TITANFORGE_CAP, 240],
]

## Usable by lether wearers and hunters
agi_trinkets = {}
agi_trinkets["dungeon"] = [[
  "Splinters of Agronax", "144477", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], [
  "Tempered Egg of Serpentrix", "137373", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], ["Tirathon's Betrayal", "137537", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL], [
  "Void Stalker's Contract", "151307", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
]]
agi_trinkets["emerald_nightmare"] = [[
  "Bloodthirsty Instinct", "139329", 162, TITANFORGE_CAP, TRADER_TOKEN
]]
agi_trinkets["nighthold"] = [[
  "Arcanogolem Digit", "140794", 170, TITANFORGE_CAP, TRADER_TOKEN
], ["Convergence of Fates", "140806", 170, TITANFORGE_CAP, TRADER_TOKEN], [
  "Entwined Elemental Foci", "140796", 170, TITANFORGE_CAP, TRADER_TOKEN
], ["Nightblooming Frond", "140802", 170, TITANFORGE_CAP, TRADER_TOKEN]]
agi_trinkets["pvp"] = [[
  "PVP Insignia of Conquest", "142662", 162, TITANFORGE_CAP, TRADER_TOKEN
], ["PVP Badge of Conquest", "142773", 162, TITANFORGE_CAP, TRADER_TOKEN]]
agi_trinkets["tomb_of_sargeras"] = [[
  "Cradle of Anguish", "147010", 182, TITANFORGE_CAP, 930
], ["Engine of Eradication", "147015", 182, TITANFORGE_CAP, 930]]
agi_trinkets["world"] = [
  ["The Devilsaur's Bite", "140026", 182, TITANFORGE_CAP, TRADER_TOKEN],
  ["Ley Spark", "140027", 182, TITANFORGE_CAP, TRADER_TOKEN],
  ["Six-Feather Fan", "141585", 182, TITANFORGE_CAP, TRADER_TOKEN],
  # 142506 is Eye of Guarm, used as a reference stat stick
  [
    "Stat Stick (Crit)", "142506,bonus_id=603", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Haste)", "142506,bonus_id=604", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Mastery)", "142506,bonus_id=605", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Versatility)", "142506,bonus_id=607", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  ["Thrice-Accursed Compass", "141537", 182, TITANFORGE_CAP, TRADER_TOKEN],
]
agi_trinkets["antorus"] = [
  ["Forgefiend's Fabricator", "151963", 195, TITANFORGE_CAP, 240],
  ["Shadow-Singed Fang", "151968", 195, TITANFORGE_CAP, 240],
  ["Golganneth's Vitality", "154174", 195, 280, 280],
]

## Usable by casters
int_trinkets = {}
# int_trinkets["crafted"] = [
#   ["Darkmoon Deck: Hellfire", "128709", 815, 900, 900],
# ]
int_trinkets["dungeon"] = [
  [
    "Dreadstone of Endless Shadows", "144480", 182, TITANFORGE_CAP,
    M_PLUS_ITEMLEVEL
  ],
  ["Infernal Writ", "137485", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL],
  ["Portable Manacracker", "137398", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL],
  ["Reality Breacher", "151310", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL],
]
int_trinkets["emerald_nightmare"] = [[
  "Bough of Corruption", "139323", 162, TITANFORGE_CAP, TRADER_TOKEN
], ["Swarming Plaguehive", "139321", 162, TITANFORGE_CAP, TRADER_TOKEN], [
  "Twisting Wind", "139323", 162, TITANFORGE_CAP, TRADER_TOKEN
], ["Unstable Horrorslime", "138224", 162, TITANFORGE_CAP, TRADER_TOKEN], [
  "Wriggling Sinew", "139326", 162, TITANFORGE_CAP, TRADER_TOKEN
]]
int_trinkets["nighthold"] = [[
  "Erratic Metronome", "140792", 170, TITANFORGE_CAP, TRADER_TOKEN
], [
  "Pharameres Forbidden Grimoire", "140800", 170, TITANFORGE_CAP, TRADER_TOKEN
], ["Star Gate", "140804", 170, TITANFORGE_CAP, TRADER_TOKEN], [
  "Whispers in the Dark", "140809", 170, TITANFORGE_CAP, TRADER_TOKEN
]]
int_trinkets["pvp"] = [[
  "PVP Insignia of Dominance", "142668", 182, TITANFORGE_CAP, TRADER_TOKEN
], ["PVP Badge of Dominance", "142779", 182, TITANFORGE_CAP, TRADER_TOKEN]]
int_trinkets["tomb_of_sargeras"] = [
  ["Charm of the Rising Tide", "147002", 182, TITANFORGE_CAP, 930],
]
int_trinkets["antorus"] = [
  ["Acrid Catalyst Injector", "151955", 195, TITANFORGE_CAP, 240],
  ["Sheath of Asara", "151971", 195, TITANFORGE_CAP, 240],
  ["Vitality Resonator", "151970", 195, TITANFORGE_CAP, 240],
  ["Norgannon's Prowess", "154177", 195, 280, 280],
]
int_trinkets["world"] = [
  ["Devilsaur Shock-Baton", "140030", 182, TITANFORGE_CAP, TRADER_TOKEN],
  ["Eyasu's Mulligan", "141584", 182, TITANFORGE_CAP, TRADER_TOKEN],
  ["Padawsen's Unlucky Charm", "141536", 182, TITANFORGE_CAP, TRADER_TOKEN],
  # 142507 is Brinewater Slime in a Bottle, used as a reference stat stick
  [
    "Stat Stick (Crit)", "142507,bonus_id=603", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Haste)", "142507,bonus_id=604", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Mastery)", "142507,bonus_id=605", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Versatility)", "142507,bonus_id=607", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ]
]

## Usable by plate wearers
str_trinkets = {}
str_trinkets["dungeon"] = [[
  "Fel-Oiled Infernal Machine", "144482", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
], [
  "Void Stalker's Contract", "151307", 182, TITANFORGE_CAP, M_PLUS_ITEMLEVEL
]]
str_trinkets["emerald_nightmare"] = [
  ["Ursoc's Rending Paw", "139328", 162, TITANFORGE_CAP, TRADER_TOKEN],
]
str_trinkets["nighthold"] = [[
  "Claw of the Crystalline Scorpid", "140790", 170, TITANFORGE_CAP,
  TRADER_TOKEN
], ["Convergence of Fates", "140806", 170, TITANFORGE_CAP, TRADER_TOKEN], [
  "Entwined Elemental Foci", "140796", 170, TITANFORGE_CAP, TRADER_TOKEN
], ["Might of Krosus", "140799", 170, TITANFORGE_CAP, TRADER_TOKEN]]
str_trinkets["pvp"] = [[
  "PVP Insignia of Victory", "142784", 182, TITANFORGE_CAP, TRADER_TOKEN
], ["PVP Badge of Victory", "142669", 182, TITANFORGE_CAP, TRADER_TOKEN]]
str_trinkets["tomb_of_sargeras"] = [[
  "Cradle of Anguish", "147010", 182, TITANFORGE_CAP, 930
], ["Engine of Eradication", "147015", 182, TITANFORGE_CAP, 930]]
str_trinkets["world"] = [
  ["Impact Tremor", "140034", 182, TITANFORGE_CAP, TRADER_TOKEN],
  # 142508 is Chains of the Valorous, used as a reference stat stick
  [
    "Stat Stick (Crit)", "142508,bonus_id=603", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Haste)", "142508,bonus_id=604", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Mastery)", "142508,bonus_id=605", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  [
    "Stat Stick (Versatility)", "142508,bonus_id=607", 182, TITANFORGE_CAP,
    TRADER_TOKEN
  ],
  ["Ettin Fingernail", "141535", 182, TITANFORGE_CAP, TRADER_TOKEN]
]
str_trinkets["antorus"] = [
  ["Forgefiend's Fabricator", "151963", 195, TITANFORGE_CAP, 240],
  ["Khaz'goroths Courage", "154176", 195, 280, 280],
  ["Shadow-Singed Fang", "151968", 195, TITANFORGE_CAP, 240],
]

##
## @brief      Selects the relevant trinket dictionaries for a given spec
##
## @param      role  The specialisation name as string
## @param      stat  The specialisation's main stat (str/int/agi) as a string
##
## @return     A group of trinkets relevant to the role as a dictionary of lists
## @return     A group of trinkets relevant to the main stat as a dictionary of
##             lists
##
def __get_relevant_trinkets(role, stat):
  # Inelegant solution. No good way to do this.
  if role == "ranged":
    role_trinkets = ranged_trinkets
  else:
    role_trinkets = melee_trinkets

  if stat == "int":
    stat_trinkets = int_trinkets
  elif stat == "agi":
    stat_trinkets = agi_trinkets
  else:
    stat_trinkets = str_trinkets
  return (role_trinkets, stat_trinkets)

import copy
##
## @brief      Combines role and stat trinket
##
## @param      role_trinkets  The trinkets relevant to role (ranged/melee) as a
##                            dict of lists
## @param      stat_trinkets  The trinkets relevant to a spec's stat
##                            (int/str/agi) as a dict of lists
## @param      spec_name      Name of the wow spec
##
## @return     A group of trinkets relevant to the spec as a dictionary of lists
##
def __combine_trinket_dicts(role_trinkets, stat_trinkets, spec_name):
  # Populate a new trinkets dict with role trinkets
  trinkets = copy.deepcopy(role_trinkets)

  for source in stat_trinkets:
    if trinkets.get(source) is not None:
      # Append int/str/agi trinkets to existing list in the newly created dict
      trinkets[source] = trinkets[source] + stat_trinkets[source]
    else:
      # Just set the int/str/agi trinket list to the newly created dict's source key
      trinkets[source] = stat_trinkets[source]

  # add shared trinkets from data
  for source in shared_trinkets:
    if trinkets.get(source) is not None:
      trinkets[source] = trinkets[source] + shared_trinkets[source]
    else:
      trinkets[source] = shared_trinkets[source]

  # add legendary from data
  for source in legendary_trinkets:
    if trinkets.get(source) is not None:
      trinkets[source] = trinkets[source] + legendary_trinkets[source]
    else:
      trinkets[source] = legendary_trinkets[source]

    # add tank legendary if a tank spec is choosen
    if spec_name.title(
    ) in ("Blood", "Vengeance", "Brewmaster", "Guardian", "Protection"):
      trinkets["legendary"].append([
        "Archimonde's Hatred Reborn", "144249", 970, 1000, 1000
      ])
      trinkets["legendary"].append([
        "Aggramar's Conviction", "154173", 940, 1000, 1000
      ])
      trinkets["antorus"].append([
        "Diima's Glacial Aegis", "151977", 930, TITANFORGE_CAP, 960
      ])
      trinkets["antorus"].append([
        "Smoldering Titanguard", "151978", 930, TITANFORGE_CAP, 960
      ])
      trinkets["antorus"].append([
        "Riftworld Codex", "151976", 930, TITANFORGE_CAP, 960
      ])
      trinkets["tomb_of_sargeras"].append([
        "Leviathan's Hunger", "147023", 885, TITANFORGE_CAP, 930
      ])
      trinkets["tomb_of_sargeras"].append([
        "Feverish Carapace", "147022", 885, TITANFORGE_CAP, 930
      ])

  return trinkets

##
## @brief      Uses class and spec names to return a dict of relevant trinkets
##
## @param      class_name  The class name as string
## @param      spec_name   The specifier name as string
##
## @return     Relevant trinkets as a dict of lists
##
def get_trinkets_for_spec_legion(class_name, spec_name):
  spec_info = get_role_stat(class_name, spec_name)
  role_trinkets, stat_trinkets = __get_relevant_trinkets(
    spec_info[0], spec_info[1]
  )

  combined_trinkets = __combine_trinket_dicts(
    role_trinkets, stat_trinkets, spec_name
  )

  return combined_trinkets

##
## @brief      Gets the main stat and role
##
## @param      wow_class  The class name as string
## @param      wow_spec   The specifier name as string
##
## @return     List of [main_stat, role]
##
def get_role_stat(wow_class, wow_spec):

  return [
    __class_data[wow_class.title()]["specs"][wow_spec.title()]["role"],
    __class_data[wow_class.title()]["specs"][wow_spec.title()]["stat"]
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
    tuple(melee{bool}, ranged{bool}, main_stat_agi{bool}, main_stat_int{bool}, main_stat_str{bool}) -- Returns a bool tuple mask to match the True's with Trinket
  """

  melee = is_melee(wow_class, wow_spec)
  ranged = is_ranged(wow_class, wow_spec)
  main_stat = get_main_stat(wow_class, wow_spec)
  main_stat_agi = main_stat == "agi"
  main_stat_int = main_stat == "int"
  main_stat_str = main_stat == "str"

  return (melee, ranged, main_stat_agi, main_stat_int, main_stat_str)


def get_trinkets_for_spec(wow_class, wow_spec):
  """New function to return all available trinkets for a spec

  Arguments:
    wow_class {str} -- name of the wow class
    wow_spec {str} -- name of the wow spec

  Returns:
    list[Trinket] -- List of all Trinkets
  """

  # get old trinket list

  temp_list = get_trinkets_for_spec_legion(wow_class, wow_spec)

  return_list = []

  for source in temp_list:
    for trinket_data in temp_list[source]:
      name = trinket_data[0]
      item_id = trinket_data[1]
      min_itemlevel = trinket_data[2]
      max_itemlevel = trinket_data[3]
      max_itemlevel_drop = trinket_data[4]

      return_list.append((name, item_id, min_itemlevel, max_itemlevel, max_itemlevel_drop))



  # melee, ranged, agility, intellect, strength = get_mask_for_spec(
  #   wow_class, wow_spec
  # )
  # return_list = []
  # for trinket in __trinket_list:
  #   if melee and trinket.melee:
  #     return_list.append((
  #       trinket.name, trinket.item_id, trinket.min_itemlevel,
  #       trinket.max_itemlevel, trinket.max_itemlevel_drop
  #     ))
  #   elif ranged and trinket.ranged:
  #     return_list.append((
  #       trinket.name, trinket.item_id, trinket.min_itemlevel,
  #       trinket.max_itemlevel, trinket.max_itemlevel_drop
  #     ))
  #   elif agility and trinket.agility:
  #     return_list.append((
  #       trinket.name, trinket.item_id, trinket.min_itemlevel,
  #       trinket.max_itemlevel, trinket.max_itemlevel_drop
  #     ))
  #   elif intellect and trinket.intellect:
  #     return_list.append((
  #       trinket.name, trinket.item_id, trinket.min_itemlevel,
  #       trinket.max_itemlevel, trinket.max_itemlevel_drop
  #     ))
  #   elif strength and trinket.strength:
  #     return_list.append((
  #       trinket.name, trinket.item_id, trinket.min_itemlevel,
  #       trinket.max_itemlevel, trinket.max_itemlevel_drop
  #     ))
  return return_list


def get_second_trinket_for_spec(wow_class, wow_spec):
  main_stat = get_main_stat(wow_class, wow_spec)
  if main_stat == "agi":
    #return ',id=,ilevel={}'.format(DUNGEON_ITEMLEVEL if DUNGEON_ITEMLEVEL > TRADER_TOKEN else TRADER_TOKEN)
    return ''
  if main_stat == "int":
    #return ',id=,ilevel={}'.format(DUNGEON_ITEMLEVEL if DUNGEON_ITEMLEVEL > TRADER_TOKEN else TRADER_TOKEN)
    return ''
  if main_stat == "str":
    #return ',id=,ilevel={}'.format(DUNGEON_ITEMLEVEL if DUNGEON_ITEMLEVEL > TRADER_TOKEN else TRADER_TOKEN)
    return ''


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


def get_trinket(name="", item_id=""):
  """Return Trinket of matching name or item_id. One must be provided. Else it'll return None.

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


def get_azerite_traits(wow_class, wow_spec):

  import pkg_resources

  path = "trait_list.json"

  f = pkg_resources.ResourceManager().resource_stream(__name__, path)

  traits = json.load(f)

  try:
    return traits[wow_class.title()][wow_spec.title()]
  except Exception as e:
    raise e


def get_all_trinkets():
  """Get a list of all known trinket names.

  Returns:
    list[trinket_name{str}] -- List of all trinket names.
  """

  all_trinkets = []
  for trinket in __trinket_list:
    all_trinkets.append(trinket.name)
  return all_trinkets


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
  data_talents = get_dps_talents(wow_class)
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
  #elif len(talent_combination) % 2 == 0:
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


def get_races():
  """Get a list of all wow race names.

  Returns:
    list[wow_race_name{str}] -- List of all wow race names
  """

  races = []
  for faction in __races.keys():
    for race in __races[faction].keys():
      if not race in races:
        races.append(race)
  return races


def get_races_for_class(wow_class):
  """Get a list of all available races to the given wow_class.

  Arguments:
    wow_class {str} -- wow class name

  Returns:
    list[wow_race_name{str}] -- List of all available races to the given wow_class.
  """

  race_list = []
  for faction in __races.keys():
    for race in __races[faction].keys():
      # additionally prevent double races like pandaren
      if str(wow_class).lower() in __races[faction][race
                                                   ] and not race in race_list:
        race_list.append(race)
  return race_list


def get_role(wow_class, wow_spec):
  """Get the role of the given wow class and wow spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    str -- role ('ranged'/'melee')
  """

  return __class_data[wow_class.title()]["specs"][wow_spec.title()]["role"]


def get_class_id(wow_class: str) -> int:
  """Get the wow ID of the given class.

  Arguments:
    wow_class {str} -- [description]

  Returns:
    int -- wow_class_id
  """

  return __class_data[wow_class.title()]["id"]


def get_spec_id(wow_class: str, wow_spec: str) -> int:
  """Get the ID of a given spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    int -- wow_spec_id
  """

  return __class_data[wow_class.title()]["specs"][wow_spec.title()]["id"]


def get_main_stat(wow_class, wow_spec):
  """Get the main stat of a class and spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    str -- main stat (agi / int / str)
  """

  return __class_data[wow_class.title()]["specs"][wow_spec.title()]["stat"]


def get_dps_talents(wow_class, wow_spec=""):
  """Return the dps talent mask for a spec. DPS talents are represented by a '1', non-DPS talent are represented by a '0' (zero).

  Arguments:
    wow_class {str} -- [description]

  Keyword Arguments:
    wow_spec {str} -- wow spec, usually not needed as of Legion. Specs of one class share the same utility rows, not necessarily the talents there,though (default: {""})

  Returns:
    str -- talent mask, e.g. '1011101'
  """

  return __class_data[wow_class.title()]["talents"]


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
