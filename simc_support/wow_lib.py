# -*- coding: utf-8 -*-
## Utility file for class specialisations
## Contains wow classes, specs, dps talent rows,
## races, trinkets

# these values are used throughout the code to determine itemlevel "borders" of items
TRADER_TOKEN = 0  # usually used as a catch up mechanic, drops usually all items from previous content
WORLD_QUEST_ITEMLEVEL = 310
DUNGEON_ITEMLEVEL = 310  # standard dungeon itemlevel (normal, max level dungeon)
M_PLIS_ITEMLEVEL = 340  # highest available itemlevel from m+ dungeons. weekly chest is NOT included here
TITANFORGE_CAP = 355  # currently highest itemlevel titanforging cap


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


class Azerite_Trait(object):
  """Class of Azerite traits. max_stacks reflects on how many items this trait could be.
    """

  def __init__(
    self, name, specs, spell_id, trait_id, min_itemlevel, max_itemlevel,
    max_stack, description
  ):
    super(Azerite_Trait, self).__init__()
    self.name: str = str(name)
    self.specs: list = specs
    self.spell_id: str = str(spell_id)
    self.trait_id: str = str(trait_id)
    self.min_itemlevel: int = int(min_itemlevel)
    self.max_itemlevel: int = int(max_itemlevel)
    self.max_stack: int = int(max_stack)
    self.description: str = str(description)


__class_data = {
  "Death_Knight": {
    "talents": "1110011",
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
      "Vengance": {
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
    "talents": "1001111",
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
    "talents": "1001111",
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
    "nightelf": (
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
    "bloodelf": (
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
  # Trinket(
  #   "", "", DUNGEON_ITEMLEVEL, TITANFORGE_CAP, TRADER_TOKEN,
  #   False, False, False, False, False
  # ),
]

__trait_list = [
  Azerite_Trait(
    "Resounding Protection", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 263962, 15, -1, -1, 1,
    "Every $270568t1 sec, gain an absorb shield for $s1 for $269279d."
  ),
  Azerite_Trait(
    "Azerite Empowered", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 263978, 13, -1, -1, 1, "Increases the item level of this item by 5."
  ),
  Azerite_Trait(
    "Blood Siphon", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 264108, 18, -1, -1, 1,
    "Increases your Mastery by $s1 and your Leech by $s2."
  ),
  Azerite_Trait(
    "Gutripper", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 266937, 31, -1, -1, 1,
    "Your damaging abilities have a chance to deal $s1 Physical damage to the target. Gutripper occurs much more often against targets below $s2% health. "
  ),
  Azerite_Trait(
    "Azerite Fortification", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 268435, 86, -1, -1, 1,
    "When stunned, immobilized, or knocked back, you heal for $s1."
  ),
  Azerite_Trait(
    "Impassive Visage", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 268437, 83, -1, -1, 1,
    "When you take damage, heal for $s1. Cannot occur more than once every $270654proccooldown sec."
  ),
  Azerite_Trait(
    "Bulwark of the Masses", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 268595, 84, -1, -1, 1,
    "When you are surrounded by $s2 or more enemies, gain a shield that absorbs $s1 damage. Cannot occur more than once every $270656d."
  ),
  Azerite_Trait(
    "Gemhide", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 268596, 85, -1, -1, 1,
    "When dealt damage greater than $s3% of your maximum health, gain $s1 Avoidance and $s2 Dodge for $270576d."
  ),
  Azerite_Trait(
    "Vampiric Speed", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 268599, 44, -1, -1, 1,
    "When an enemy you damaged dies, you heal for $s1 and gain $s2 Speed for $269239d."
  ),
  Azerite_Trait(
    "Self Reliance", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 268600, 87, -1, -1, 1,
    "While no enemies are within $s2 yds, you heal for $s1 every $270661t1 sec."
  ),
  Azerite_Trait(
    "Champion of Azeroth", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 270583, 82, -1, -1, 1,
    "Contributing to the death of an enemy of Azeroth heals you for $s1 and grants you $s2 Versatility for $270586d, stacking up to $270586u times."
  ),
  Azerite_Trait(
    "Ablative Shielding", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 271540, 99, -1, -1, 1,
    "Falling below $271542s1% health grants you $s1 Armor for $271543d. Taking further Physical damage reduces the Armor granted. May only occur every $271544d."
  ),
  Azerite_Trait(
    "Deep Cuts", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 272684, 106, -1, -1, 1,
    "Heart Strike deals an additional $s1 damage when hitting $s3 or more targets and heals you for a percentage of the damage done."
  ),
  Azerite_Trait(
    "Icy Citadel", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 272718, 108, -1, -1, 1,
    "Pillar of Frost grants an additional $s1 strength while you are above $s2% health."
  ),
  Azerite_Trait(
    "Festering Doom", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 272738, 109, -1, -1, 1,
    "Death Coil causes your next Festering Strike to deal an additional $s1 damage."
  ),
  Azerite_Trait(
    "Bone Spike Graveyard", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 273088, 140, -1, -1, 1,
    "Casting Death and Decay impales enemies with bone spikes, inflicting $s1 Physical damage and healing you for $s2 per enemy."
  ),
  Azerite_Trait(
    "Latent Chill", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 273093, 141, -1, -1, 1,
    "Frost Strike deals an additional ${$s1+($s1/2)} damage if you have at least $s2 empty runes."
  ),
  Azerite_Trait(
    "Horrid Expulsion", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 273095, 142, -1, -1, 1,
    "When Dark Transformation expires, the unholy energy in your ghoul is expelled, dealing $s1 Shadow damage to all nearby enemies."
  ),
  Azerite_Trait(
    "Meticulous Scheming", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273682, 192, -1, -1, 1,
    "Your spells and abilities have a chance to grant you Meticulous Scheming for $273685d, which transforms into Seize the Moment! after you cast $s3 different spells, granting you $s4 Haste for $273714d seconds."
  ),
  Azerite_Trait(
    "Rezan's Fury", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273790, 157, -1, -1, 1,
    "Your damaging abilities have a chance to call a Child of Rezan to viciously rend your target, dealing $s1 Physical damage and causing them to bleed for ${($273794d/$273794t2)*$s2} damage over $273794d."
  ),
  Azerite_Trait(
    "Blightborne Infusion (Drustvar Power)", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273823, 193, -1, -1, 1,
    "Your spells and abilities have a chance to draw a Wandering Soul from Thros. The Soul grants you some of its power, increasing your Critical Strike by $s1 for $273826d."
  ),
  Azerite_Trait(
    "Secrets of the Deep", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273829, 195, -1, -1, 1,
    "Your spells and abilities have a chance to create a Surging Droplet nearby. Collecting it increases your primary stat by $s1 for $273842d."
  ),
  Azerite_Trait(
    "Filthy Transfusion", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273834, 194, -1, -1, 1,
    "Your damaging abilities have a chance to invoke a tainted swamp beneath the target, siphoning ${$s1*6} health from them over $273836d."
  ),
  Azerite_Trait(
    "Sandstorm", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273853, 196, -1, -1, 1,
    "Your spells and abilities have a chance to summon a cylone of piercing winds. Enemies inside the cyclone take $s1 damage every $t1, and deal $s2 less damage to you."
  ),
  Azerite_Trait(
    "Marrowblood", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 274057, 197, -1, -1, 1,
    "Death Strike heals for an additional $s1 for each remaining charge of Bone Shield."
  ),
  Azerite_Trait(
    "Glacial Contagion", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 274070, 198, -1, -1, 1,
    "Your autoattacks have a chance to apply Glacial Contagion, dealing ${s1*7} Frost damage over 14 sec. Obliterate deals an additional $s2 damage to targets infected with Glacial Contagion."
  ),
  Azerite_Trait(
    "Festermight", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 274081, 199, -1, -1, 1,
    "Bursting a Festering Wound grants you $s1 Strength for 20 sec, stacking. Stacking this effect does not extend its duration."
  ),
  Azerite_Trait(
    "Spellreaper", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 274203, 201, -1, -1, 1,
    "When you successfully dispel an effect with Reap Magic, gain $s1 Absorb for $274289d"
  ),
  Azerite_Trait(
    "Echoing Howl", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 275917, 242, -1, -1, 1,
    "When empowered by Rime, Howling Blast causes a secondary burst of icy wind around you that deals $s1 Frost damage to nearby enemies."
  ),
  Azerite_Trait(
    "Embrace of the Darkfallen", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 275924, 243, -1, -1, 1,
    "When Vampiric Blood expires, your Leech is increased by $s1 for $275926d."
  ),
  Azerite_Trait(
    "Harrowing Decay", [
      ("Death_Knight", "Blood"),
      ("Death_Knight", "Frost"),
      ("Death_Knight", "Unholy"),
    ], 275929, 244, -1, -1, 1,
    "Death Coil infects the target with Harrowing Decay, dealing ${$s1*($275931d/$275931t1)} Shadow damage over $275931d."
  ),
  Azerite_Trait(
    "Elemental Whirl", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 263984, 21, -1, -1, 1,
    "Your damaging abilities have a chance to grant you Elemental Whirl, increasing your Critical Strike, Haste, Mastery, or Versatility by $s1 for $268956d."
  ),
  Azerite_Trait(
    "Heed My Call", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Priest", "Shadow"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 263987, 22, -1, -1, 1,
    "Your damaging abilities have a chance to deal $s1 to your target, and $s2 to enemies within 3 yards of that target."
  ),
  Azerite_Trait(
    "Winds of War", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 267671, 43, -1, -1, 1,
    "Taking damage grants you $s1 Dodge for $269214d, stacking up to $269214u times."
  ),
  Azerite_Trait(
    "Azerite Veins", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 267683, 89, -1, -1, 1,
    "Taking damage has a chance to grant you Azerite Veins, healing you for $s1 every $270674t1 sec. Lasts $270674d or until you are fully healed."
  ),
  Azerite_Trait(
    "Devour", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 272793, 126, -1, -1, 1,
    "Attacking with Demon's Bite 3 times in a row grants you $s1 Mastery for $272794d."
  ),
  Azerite_Trait(
    "Revel in Pain", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 272983, 134, -1, -1, 1,
    "When Fiery Brand expires on your primary target, you gain a shield that absorbs up to $s1 damage for $272987d, based on your damage dealt to them while Fiery Brand was active. "
  ),
  Azerite_Trait(
    "Furious Gaze", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273231, 159, -1, -1, 1,
    "When Eye Beam finishes fully channeling, your Haste is increased by $s1 for $273232d."
  ),
  Azerite_Trait(
    "Infernal Armor", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 273236, 160, -1, -1, 1,
    "Immolation Aura increases your Armor by $s2, and causes melee attackers to take $s1 Fire damage."
  ),
  Azerite_Trait(
    "Soulmonger", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 274344, 202, -1, -1, 1,
    "Consuming a Soul Fragment shields you, granting $s1 Absorb for $274346d"
  ),
  Azerite_Trait(
    "Unbound Chaos", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 275144, 220, -1, -1, 1,
    "Your inner demon slams into nearby enemies at the end of your Fel Rush, dealing $s1 Chaos damage."
  ),
  Azerite_Trait(
    "Rigid Carapace", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 275350, 221, -1, -1, 1,
    "Demon Spikes increases your Armor by $s1 every $275351t2 sec, for $275351d."
  ),
  Azerite_Trait(
    "Seething Power", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 275934, 245, -1, -1, 1,
    "Chaos Strike increases your Agility by $s1 for $275936d. Stacking this effect does not extend its duration."
  ),
  Azerite_Trait(
    "Gaping Maw", [
      ("Demon_Hunter", "Havoc"),
      ("Demon_Hunter", "Vengance"),
    ], 275968, 246, -1, -1, 1,
    "Soul Cleave grants you a shield that absorbs $s1 damage, increased by up to $s2% based on your missing health."
  ),
  Azerite_Trait(
    "Woundbinder", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Priest", "Shadow"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 267880, 19, -1, -1, 1,
    "Your healing effects have a chance to increase your Haste by up to $s1 for $269085d. Healing lower health targets will grant you more Haste."
  ),
  Azerite_Trait(
    "Ephemeral Recovery", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 267886, 105, -1, -1, 1,
    "Casting a healing spell restores ${$s1*($272572d/$272572t1)} mana over $272572d. Stacks up to $272572u times."
  ),
  Azerite_Trait(
    "Heartblood", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 272762, 112, -1, -1, 1,
    "Mangle increases the healing of the next ability to heal you by $s1."
  ),
  Azerite_Trait(
    "Fungal Essence", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 272802, 120, -1, -1, 1,
    "Swiftmend causes your Efflorescence mushroom to burst, healing a nearby injured ally for $s1."
  ),
  Azerite_Trait(
    "Streaking Stars", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 272871, 122, -1, -1, 1,
    "While Celestial Alignment is active, your spells call a Streaking Star, dealing an additional $s1 damage when they are not a repeat of the previous ability."
  ),
  Azerite_Trait(
    "Raking Ferocity", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 273338, 169, -1, -1, 1,
    "Rake increases next damage of Ferocious Bite by $s1."
  ),
  Azerite_Trait(
    "Masterful Instincts", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 273344, 171, -1, -1, 1,
    "Increases your Mastery by $s1 and Armor by $s2 for $273349d after Survival Instincts expires."
  ),
  Azerite_Trait(
    "Coordinated Restoration", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 273353, 172, -1, -1, 1,
    "When Lifebloom expires, if the target has Rejuvenation and Regrowth it heals for $s1. "
  ),
  Azerite_Trait(
    "Power of the Moon", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 273367, 173, -1, -1, 1,
    "If 3 or more targets are suffering Moonfire, Lunar Strike deals an additional $s1. "
  ),
  Azerite_Trait(
    "Sunblaze", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 274397, 200, -1, -1, 1,
    "Solar Wrath increases the damage of your next Starsurge by $s1."
  ),
  Azerite_Trait(
    "Shredding Fury", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 274424, 209, -1, -1, 1,
    "After your Tiger's Fury, your next four Shreds are increased by $s1."
  ),
  Azerite_Trait(
    "Solitary Rejuvenation", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 274432, 210, -1, -1, 1,
    "If Rejuvenation is your only Heal over Time effect on the target, increase the healing of Rejuvenation by $s1. "
  ),
  Azerite_Trait(
    "Reawakening", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 274813, 219, -1, -1, 1,
    "When you resurrect an ally with Rebirth, they absorb $s1 damage over $274814d."
  ),
  Azerite_Trait(
    "Twisted Claws", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 275906, 241, -1, -1, 1,
    "Thrash's direct damage has a $275908h% chance to grant you $s1 Agility for $275909d, stacking up to $275909u times."
  ),
  Azerite_Trait(
    "Iron Jaws", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 276021, 247, -1, -1, 1,
    "Ferocious Bite has a $s2% chance per combo point to increase the base damage of your next Maim by $s1."
  ),
  Azerite_Trait(
    "Dawning Sun", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 276152, 250, -1, -1, 1,
    "Lunar Strike increases the damage of your Solar Wrath by $s1 for $276154d."
  ),
  Azerite_Trait(
    "Craggy Bark", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 276155, 251, -1, -1, 1,
    "Barkskin reduces melee attacks against you by $s1 damage."
  ),
  Azerite_Trait(
    "Rampant Growth", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 278515, 362, -1, -1, 1,
    "Regrowth heals for ${$s1*($8936d/$8936t2)} more over its duration, and its healing over time effect also applies to the target of your Lifebloom."
  ),
  Azerite_Trait(
    "Blood Mist", [
      ("Druid", "Balance"),
      ("Druid", "Feral"),
      ("Druid", "Guardian"),
    ], 279524, 111, -1, -1, 1,
    "Rake deals ${$s2*5} additional damage over its duration, and has a chance to grant you Berserk for $279526d. Cannot occur while $?s102543[Incarnation: King of the Jungle][Berserk] is active."
  ),
  Azerite_Trait(
    "Arrowstorm", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 263814, 27, -1, -1, 1,
    "Increases the damage of Aimed Shot by $s1 and has a $s2% chance to reset  the cooldown of your Rapid Fire."
  ),
  Azerite_Trait(
    "Vigorous Wings", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 263818, 29, -1, -1, 1,
    "Increases the duration of Aspect of the Eagle by $s1 sec and causes your Mongoose Bites to deal an additional $s2 damage when they critically strike."
  ),
  Azerite_Trait(
    "Aspect of the Cheetah", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 263829, 16, -1, -1, 1,
    "Adds an additional $s1% speed to the initial 3 seconds of Aspect of the Cheetah."
  ),
  Azerite_Trait(
    "Rotting Jaws", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 264195, 35, -1, -1, 1,
    "Kill Command has a chance to deal $s1 to ${$s1*5} additional damage and grants you 6 Focus over 3 sec."
  ),
  Azerite_Trait(
    "In The Rhythm", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 264198, 36, -1, -1, 1,
    "When Rapid Fire finishes fully channeling, your Haste is increased by $s1 for $272733d."
  ),
  Azerite_Trait(
    "Embrace of the Sands", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 264600, 40, -1, -1, 1,
    "Critical strikes by your abilities have a chance to create a localized Sandstorm, damaging enemies and healing allies within 10 yards for ${$s1*4} every 2 sec for 6 sec."
  ),
  Azerite_Trait(
    "Overwhelming Power", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 266180, 30, -1, -1, 1,
    "Your damaging abilities have a chance to grant you 25 applications of Overwhelming Power. Each stack of Overwhelming Power grants $s1 Haste. An application of Overwhelming Power is removed every 1 sec or whenever you take damage."
  ),
  Azerite_Trait(
    "Longstrider", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 268594, 14, -1, -1, 1,
    "Increases your movement speed by $s1% of your highest secondary rating, up to $s2%."
  ),
  Azerite_Trait(
    "Serrated Jaws", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 272717, 107, -1, -1, 1,
    "Kill Command has a $s3% chance to deal an additional $s1 damage and grant your Pet $s2 Focus."
  ),
  Azerite_Trait(
    "Wildfire Cluster", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 272742, 110, -1, -1, 1,
    "Wildfire Bomb drops a small cluster of bombs around the target, each exploding for $s1 damage."
  ),
  Azerite_Trait(
    "Haze of Rage", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 273262, 161, -1, -1, 1,
    "Bestial Wrath increases your Agility by $s1 for $273264d."
  ),
  Azerite_Trait(
    "Arcane Flurry", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 273265, 162, -1, -1, 1,
    "Arcane Shot increases the damage of Arcane Shot by $s1 for $273267d, stacking up to $273267u times."
  ),
  Azerite_Trait(
    "Latent Poison", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 273283, 163, -1, -1, 1,
    "Serpent Sting damage applies Latent Poison, stacking up to $273286u times. Your $?s259387[Mongoose Bite][Raptor Strike] consumes all applications of Latent Poison to deal $s1 Nature damage per stack."
  ),
  Azerite_Trait(
    "Shellshock", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 274355, 203, -1, -1, 1,
    "Each second Aspect of the Turtle is active, heal for $s1"
  ),
  Azerite_Trait(
    "Dance of Death", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 274441, 211, -1, -1, 1,
    "Dire Frenzy has a chance equal to your critical strike chance to grant you $s1 Agility for its duration."
  ),
  Azerite_Trait(
    "Unerring Vision", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 274444, 212, -1, -1, 1,
    "While Trueshot is active you gain $s1 Critical Strike rating every sec, stacking up to 10 times."
  ),
  Azerite_Trait(
    "Venomous Fangs", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 274590, 213, -1, -1, 1,
    "Your pet's Basic Attack deals $s1 additional damage to enemies suffering from your Serpent Sting."
  ),
  Azerite_Trait(
    "Cobra's Bite", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 277634, 366, -1, -1, 1,
    "Cobra Shot deals ${$s1*($277916d/$277916t1)} Nature damage over $277916d."
  ),
  Azerite_Trait(
    "Steady Aim", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 277651, 368, -1, -1, 1,
    "Steady Shot increases the damage of your next Aimed Shot against the target by $s1, stacking up to $277959u times."
  ),
  Azerite_Trait(
    "Blur of Talons", [
      ("Hunter", "Beast_Mastery"),
      ("Hunter", "Marksmanship"),
      ("Hunter", "Survival"),
    ], 277653, 371, -1, -1, 1,
    "During Coordinated Assault, $?s259387[Mongoose Bite][Raptor Strike] increases your Agility by $s1 and your Speed by $s2 for $277969d. Stacks up to $277969u times."
  ),
  Azerite_Trait(
    "Arcane Pummeling", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 270669, 88, -1, -1, 1,
    "Each wave of Arcane Missiles deals $s1 more damage than the previous one."
  ),
  Azerite_Trait(
    "Arcane Annihilation", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 272927, 127, -1, -1, 1,
    "Arcane Blast deals an additional $s1 damage while you have $s2 Arcane Charges."
  ),
  Azerite_Trait(
    "Flames of Alacrity", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 272932, 128, -1, -1, 1,
    "Enhanced Pyrotechnics grants an additional $s1 Haste. "
  ),
  Azerite_Trait(
    "Packed Ice", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 272968, 132, -1, -1, 1,
    "Ice Lance deals an additional $s1 damage to enemies recently damaged by your Frozen Orb."
  ),
  Azerite_Trait(
    "Brain Storm", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 273326, 167, -1, -1, 1,
    "While channeling Evocation, your Intellect is increased by $s1 every $273329t1 sec. Lasts $273330d."
  ),
  Azerite_Trait(
    "Preheat", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 273331, 168, -1, -1, 1,
    "Scorch increases the damage the target takes from your Fire Blast by $s1 for $273333d."
  ),
  Azerite_Trait(
    "Winter's Reach", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 273346, 170, -1, -1, 1,
    "Consuming Brain Freeze has a $s2% chance to make your next non-instant Flurry cast within $273347d deal an additional $s1 damage per hit."
  ),
  Azerite_Trait(
    "Eldritch Warding", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 274379, 205, -1, -1, 1,
    "Your Ice Barrier, Blazing Barrier, and Prismatic Barrier absorb $s1 additional damage."
  ),
  Azerite_Trait(
    "Arcane Pressure", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 274594, 214, -1, -1, 1,
    "Arcane Barrage deals an additional $s1 damage per Arcane Charge against targets below $s2% health."
  ),
  Azerite_Trait(
    "Blaster Master", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 274596, 215, -1, -1, 1,
    "Fire Blast increases your Mastery by $s1 for 3 sec."
  ),
  Azerite_Trait(
    "Orbital Precision", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 275509, 225, -1, -1, 1,
    "Each Frostbolt you cast while Frozen Orb is active grants you $s1 Intellect for 10 sec."
  ),
  Azerite_Trait(
    "Trailing Embers", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 277656, 376, -1, -1, 1,
    "Pyroblast burns enemies between you and the target for ${$s1*(1+$277703d/$277703t1)} Fire damage over $277703d."
  ),
  Azerite_Trait(
    "Tunnel of Ice", [
      ("Mage", "Arcane"),
      ("Mage", "Fire"),
      ("Mage", "Frost"),
    ], 277663, 379, -1, -1, 1,
    "Frostbolt increases the damage of Frostbolt by $s1, stacking up to $277904u times. This effect is reset if you cast Frostbolt at a different enemy."
  ),
  Azerite_Trait(
    "Invigorating Brew", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 269621, 76, -1, -1, 1,
    "Vivify does an additional $s1 healing when empowered by Thunder Focus Tea."
  ),
  Azerite_Trait(
    "Boiling Brew", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 272792, 116, -1, -1, 1,
    "Keg Smash deals an additional $s1 damage against targets burning from your Breath of Fire, and heals you for $s2% of the damage dealt to those targets."
  ),
  Azerite_Trait(
    "Iron Fists", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 272804, 117, -1, -1, 1,
    "Fists of Fury grants you $s1 Critical Strike for $272806d when it hits at least $s2 enemies."
  ),
  Azerite_Trait(
    "Sunrise Technique", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 273291, 184, -1, -1, 1,
    "Attacking a target with Rising Sun Kick causes your damaging melee abilities to deal $s1 additional Physical damage to that target for $273298d."
  ),
  Azerite_Trait(
    "Overflowing Mists", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 273328, 185, -1, -1, 1,
    "Your Enveloping Mists heal the target for $s1 each time they take damage."
  ),
  Azerite_Trait(
    "Staggering Strikes", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 273464, 186, -1, -1, 1,
    "When you Blackout Strike, your Stagger is reduced by $s1."
  ),
  Azerite_Trait(
    "Strength of Spirit", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 274762, 218, -1, -1, 1,
    "While $?c3[Touch of Karma][Fortifying Brew] is active, heal for $s1 every second."
  ),
  Azerite_Trait(
    "Fit to Burst", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 275892, 238, -1, -1, 1,
    "Drinking Purifying Brew while at Heavy Stagger causes your next $275893u melee abilities to heal you for $s1."
  ),
  Azerite_Trait(
    "Misty Peaks", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 275975, 248, -1, -1, 1,
    "When your Renewing Mists jumps, you have a 10% chance to gain $s1 Haste for 8 seconds."
  ),
  Azerite_Trait(
    "Niuzao's Blessing", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 277665, 382, -1, -1, 1,
    "Expel Harm restores ${$s1*($278535d/$278535t1)} health over $278535d for each Healing Sphere consumed."
  ),
  Azerite_Trait(
    "Burst of Life", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 277667, 385, -1, -1, 1,
    "When Life Cocoon expires, it releases a burst of mist that restores $s1 health split among the target and nearby allies."
  ),
  Azerite_Trait(
    "Swift Roundhouse", [
      ("Monk", "Brewmaster"),
      ("Monk", "Windwalker"),
    ], 277669, 388, -1, -1, 1,
    "Blackout Kick increases the damage of your next Rising Sun Kick by $s1, stacking up to $278710u times."
  ),
  Azerite_Trait(
    "Lifespeed", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 267665, 20, -1, -1, 1,
    "Increases your Haste by $s1 and your Avoidance by $s2."
  ),
  Azerite_Trait(
    "Concentrated Mending", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 267882, 103, -1, -1, 1,
    "Your healing effects have a chance to grant the target ${$s1*2} additional healing every $272260t1 sec for $272260d. This effect doubles every $272260t1 sec. "
  ),
  Azerite_Trait(
    "Bracing Chill", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Priest", "Shadow"),
    ], 267884, 104, -1, -1, 1,
    "Your heals have a chance to apply Bracing Chill. Healing a target with Bracing Chill will heal for an additional $s1 and move Bracing Chill to a nearby ally (up to $272276u times)."
  ),
  Azerite_Trait(
    "Synergistic Growth", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
      ("Priest", "Shadow"),
    ], 267892, 102, -1, -1, 1,
    "Casting $?a137009[Wild Growth]?a137022[Essence Font]?a137030[Prayer of Healing or Power Word: Radiance]?a137026[Light of Dawn]?a137038[Chain Heal][your multi-target healing spell] grants you $s1 Mastery for $272090d sec. This cannot occur more than once every $272089proccooldown sec."
  ),
  Azerite_Trait(
    "Upwelling", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 271557, 101, -1, -1, 1,
    "Taking damage has a chance to create an upwelling of Azerite beneath your feet, increasing your Health by $s1 and your Armor by $s2 while you stand within it. Lasts $271560d."
  ),
  Azerite_Trait(
    "Avenger's Might", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 272898, 125, -1, -1, 1,
    "While Avenging Wrath is active, your Mastery is increased by $s1."
  ),
  Azerite_Trait(
    "Bulwark of Light", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 272976, 133, -1, -1, 1,
    "Avenger's Shield grants you a shield, absorbing $s1 damage for $272979d."
  ),
  Azerite_Trait(
    "Martyr's Breath", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273027, 139, -1, -1, 1,
    "Light of the Martyr has a chance to cause your Blessing of Sacrifice to additionally heal the target for $s1. This effect can stack up to 10 times."
  ),
  Azerite_Trait(
    "Inspiring Beacon", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273130, 143, -1, -1, 1,
    "Flash of Light on your Beacon of Light target is increased by $s1."
  ),
  Azerite_Trait(
    "Rejuvenating Grace", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273131, 144, -1, -1, 1,
    "Your Holy Light critical strikes refund $s1 mana during Avenging Wrath."
  ),
  Azerite_Trait(
    "Fortifying Auras", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273134, 145, -1, -1, 1,
    "Aura Mastery also grants your allies $s1 Max Health for its duration."
  ),
  Azerite_Trait(
    "Critical Flash", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273136, 146, -1, -1, 1,
    "Flash of Light grants you $s1 Critical Strike for 6 seconds if it heals a target below 50% health."
  ),
  Azerite_Trait(
    "Righteous Flames", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273140, 148, -1, -1, 1,
    "When Shield of the Righteous expires, gain $s1 block and deal $s2 Holy damage to all attackers for 4 seconds."
  ),
  Azerite_Trait(
    "Healing Hammer", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273142, 149, -1, -1, 1,
    "Hammer of the Righteous heals you for X if your health is below 20%."
  ),
  Azerite_Trait(
    "Healthy Judgment", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273146, 152, -1, -1, 1,
    "Judgment's damage is increased by up to $s1, based on the difference between your health percentage and the target's."
  ),
  Azerite_Trait(
    "Deferred Sentence", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273147, 153, -1, -1, 1,
    "Crusader Strike has a 3% chance to Condemn your target, dealing X Holy damage after 7 seconds."
  ),
  Azerite_Trait(
    "Weeping Aura", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273149, 155, -1, -1, 1,
    "Your spells and abilities have a chance to draw a Wandering Soul from Thros. The Soul grants you a shield that absorbs $s1 damage for 14 sec. When the shield is consumed or expires, the Soul releases a wave of dark energy dealing $s2 Shadow damage to all enemies within 8 yds."
  ),
  Azerite_Trait(
    "Ruinous Bolt", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273150, 156, -1, -1, 1,
    "Your spells and abilities have a chance to draw a Wandering Soul from Thros. The Soul will launch blasts of dark energy at your enemies, dealing $s1 Shadow damage over 14 sec. When the Soul departs, it heals you for $s2% of the damage it dealt."
  ),
  Azerite_Trait(
    "Rezan's Command", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273154, 158, -1, -1, 1,
    "Being attacked by an enemy of the Loa has a chance to call a Child of Rezan to grant you a blessing, healing you for $s1 and increasing your primary stat by $s2 for 1 min."
  ),
  Azerite_Trait(
    "Expurgation", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273473, 187, -1, -1, 1,
    "Your Blade of Justice critical hits cause the target to burn for an additional $s1 Holy damage every $273481t1 sec over $273481d."
  ),
  Azerite_Trait(
    "Warmth of the Light", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273513, 188, -1, -1, 1,
    "Your Flash of Light heals for an additional $s1 when cast on a target affected by your Beacon of Light."
  ),
  Azerite_Trait(
    "Dauntless Divinity", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 273553, 189, -1, -1, 1,
    "When Guardian of Ancient Kings expires, your Shield Block Value is increased by $s1 for $273349d "
  ),
  Azerite_Trait(
    "Stalwart Protector", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 274388, 206, -1, -1, 1,
    "When you cast Divine Shield, grant $s1 absorb for $274395d to nearby allies."
  ),
  Azerite_Trait(
    "Divine Revelations", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 275463, 233, -1, -1, 1,
    "Healing an ally with Holy Light while empowered by Infusion of Light refunds $s1 mana."
  ),
  Azerite_Trait(
    "Inner Light", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 275477, 234, -1, -1, 1,
    "When Shield of the Righteous expires, gain $s1 Block and deal $s2 Holy damage to all attackers for $275481d."
  ),
  Azerite_Trait(
    "Indomitable Justice", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 275496, 235, -1, -1, 1,
    "Judgment deals additional damage when your health exceeds the target's health, up to $s1 damage."
  ),
  Azerite_Trait(
    "Radiant Incandescence", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 277674, 452, -1, -1, 1,
    "Your Holy Shock criticals deal an additional $s1 damage, or an additional $s2 healing, over $278147d."
  ),
  Azerite_Trait(
    "Judicious Defense", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 277675, 454, -1, -1, 1,
    "Your Judgment critical strikes reduce the damage of the target's melee attacks against you by $s1 for $278574d."
  ),
  Azerite_Trait(
    "Divine Right", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 277678, 453, -1, -1, 1,
    "When Divine Storm damages an enemy who is below $s2% health, your Strength is increased by $s1 for $278523d."
  ),
  Azerite_Trait(
    "Soaring Shield", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 278605, 150, -1, -1, 1,
    "Avenger's Shield now strikes $s2 $Lenemy:enemies; and grants $s1 Mastery per enemy struck for $d."
  ),
  Azerite_Trait(
    "Relentless Inquisitor", [
      ("Paladin", "Protection"),
      ("Paladin", "Retribution"),
    ], 278617, 154, -1, -1, 1,
    "Spending Holy Power grants you $s1 haste for $279204d per Holy Power spent, stacking up to $279204u times. "
  ),
  Azerite_Trait(
    "On My Way", [
      ("Priest", "Shadow"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 267879, 38, -1, -1, 1,
    "Increases your Versatility by $s1 and your Speed by $s2."
  ),
  Azerite_Trait(
    "Savior", [
      ("Priest", "Shadow"),
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 267883, 42, -1, -1, 1,
    "Your heals on targets below $s2% health have a chance to heal for an additional $s1."
  ),
  Azerite_Trait(
    "Moment of Repose", [
      ("Priest", "Shadow"),
    ], 272775, 113, -1, -1, 1,
    "Pain Suppression applies Atonement to the target and instantly heals them for $s1."
  ),
  Azerite_Trait(
    "Permeating Glow", [
      ("Priest", "Shadow"),
    ], 272780, 114, -1, -1, 1,
    "Flash Heal increases the healing of your Flash Heals on that ally by $s1 for $272783d."
  ),
  Azerite_Trait(
    "Searing Dialogue", [
      ("Priest", "Shadow"),
    ], 272788, 115, -1, -1, 1,
    "Mind Sear deals an additional $s1 damage to enemies suffering from your Shadow Word: Pain."
  ),
  Azerite_Trait(
    "Weal and Woe", [
      ("Priest", "Shadow"),
    ], 273307, 164, -1, -1, 1,
    "Healing an ally with Penance increases the damage of your next Smite by $s1. Damaging an enemy with Penance increase the absorption of your next Power Word: Shield by $s2."
  ),
  Azerite_Trait(
    "Blessed Sanctuary", [
      ("Priest", "Shadow"),
    ], 273313, 165, -1, -1, 1,
    "Echo of Light from Holy Word: Sanctify heals for an additional ${$s1*2}."
  ),
  Azerite_Trait(
    "Thought Harvester", [
      ("Priest", "Shadow"),
    ], 273319, 166, -1, -1, 1,
    "Casting Vampiric Touch increases the damage of your next $?s205351[Shadow Word: Void][Mind Blast] by $s1."
  ),
  Azerite_Trait(
    "Sanctum", [
      ("Priest", "Shadow"),
    ], 274366, 204, -1, -1, 1,
    "When you cast Fade, absorb $s1 Magic damage for $274369d."
  ),
  Azerite_Trait(
    "Depth of the Shadows", [
      ("Priest", "Shadow"),
    ], 275541, 227, -1, -1, 1,
    "Each time Shadow Word: Pain deals damage, the healing of your next Shadow Mend is increased by $s1, up to a maximum of ${$s1*30}."
  ),
  Azerite_Trait(
    "Prayerful Litany", [
      ("Priest", "Shadow"),
    ], 275602, 228, -1, -1, 1,
    "Prayer of Healing restores an additional $s1 health to the most injured ally it affects."
  ),
  Azerite_Trait(
    "Eye of the Void", [
      ("Priest", "Shadow"),
    ], 275722, 236, -1, -1, 1,
    "Void Bolt increases the damage of Mind Blast by $s1 for $275726d, stacking up to 6 times."
  ),
  Azerite_Trait(
    "Gift of Forgiveness", [
      ("Priest", "Shadow"),
    ], 277680, 397, -1, -1, 1,
    "Smite deals an additional $s1 damage if you have at least $s2 Atonements active."
  ),
  Azerite_Trait(
    "Everlasting Light", [
      ("Priest", "Shadow"),
    ], 277681, 400, -1, -1, 1,
    "Heal restores up to $s1 additional health, based on your missing mana."
  ),
  Azerite_Trait(
    "Spiteful Apparitions", [
      ("Priest", "Shadow"),
    ], 277682, 403, -1, -1, 1,
    "Shadowy Apparitions deal an additional $s1 damage to enemies suffering from your Vampiric Touch."
  ),
  Azerite_Trait(
    "Sharpened Blades", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 272911, 124, -1, -1, 1,
    "Your autoattacks increase the damage of your next Shuriken Toss by $s, stacking up to $272916u times."
  ),
  Azerite_Trait(
    "Deadshot", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 272935, 129, -1, -1, 1,
    "Between the Eyes increases the damage of your next Pistol Shot by $s1."
  ),
  Azerite_Trait(
    "Double Dose", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 273007, 136, -1, -1, 1,
    "When Mutilate applies Lethal Poison with both daggers, it poisons the target for an additional $s1 damage."
  ),
  Azerite_Trait(
    "Night's Vengeance", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 273418, 175, -1, -1, 1,
    "Nightblade increases the damage of your next Eviscerate within 8 sec by $s1. "
  ),
  Azerite_Trait(
    "Storm of Steel", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 273452, 180, -1, -1, 1,
    "Extra strikes from Sinister Strike increase the damage of your next Dispatch by $s1."
  ),
  Azerite_Trait(
    "Twist the Knife", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 273488, 181, -1, -1, 1,
    "Envenom deals an additional $s1 damage to targets with Garrote."
  ),
  Azerite_Trait(
    "Footpad", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 274692, 217, -1, -1, 1,
    "Allies within $s2 yds while your Sprint is active gain $s1 Speed."
  ),
  Azerite_Trait(
    "Snake Eyes", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 275846, 239, -1, -1, 1,
    "For each combo point spent on Roll the Bones, it causes your next Sinister Strike to deal $s1 additional damage."
  ),
  Azerite_Trait(
    "Blade In The Shadows", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 275896, 240, -1, -1, 1,
    "When you Shadowstrike and reach 4 or more Combo Points, deal $s1 additional damage."
  ),
  Azerite_Trait(
    "Poisoned Wire", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 276072, 249, -1, -1, 1,
    "Garrote increases the critical strike rating of your next Mutilate by $s1. "
  ),
  Azerite_Trait(
    "Perforate", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 277673, 445, -1, -1, 1,
    "Backstabbing an enemy from behind increases the damage of Backstab by $s1 for $277720d, stacking up to $s2 times."
  ),
  Azerite_Trait(
    "Brigand's Blitz", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 277676, 446, -1, -1, 1,
    "Adrenaline Rush increases your Haste by $s1 every sec, stacking up to $277724U times. Lasts ${2*$277725d} seconds."
  ),
  Azerite_Trait(
    "Scent of Blood", [
      ("Rogue", "Assassination"),
      ("Rogue", "Outlaw"),
      ("Rogue", "Subtlety"),
    ], 277679, 406, -1, -1, 1,
    "Rupture increases your Agility by $s1. You may gain this benefit for each enemy suffering from your Rupture."
  ),
  Azerite_Trait(
    "Astral Shift", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 263786, 17, -1, -1, 1,
    "Increases the damage reduction of Astral Shift by an additional $s1%. "
  ),
  Azerite_Trait(
    "Ancestral Reach", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 263790, 25, -1, -1, 1,
    "Increases the healing of Chain Heal by $s1 and causes it to bounce an additional time."
  ),
  Azerite_Trait(
    "Storm's Eye", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 263795, 23, -1, -1, 1,
    "Increases the critical strike chance of Crash Lightning by $s1 and increases the radius of Crash Lightning by $s2."
  ),
  Azerite_Trait(
    "Flames of the Forefathers", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 264113, 32, -1, -1, 1,
    "Increases the damage of Lava Burst by $s1 and causes it to grant an additional $s2 Maelstrom."
  ),
  Azerite_Trait(
    "Volcanic Lightning", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 272978, 135, -1, -1, 1,
    "Lava Bursts on a target that has been struck by your Lightning in the last 4 sec deal an additional $s1 damage. "
  ),
  Azerite_Trait(
    "Soothing Waters", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 272989, 138, -1, -1, 1,
    "Your Chain Heal heals its primary target for an additional $s1 healing."
  ),
  Azerite_Trait(
    "Primal Primer", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 272992, 137, -1, -1, 1,
    "Melee attacks with Flametongue active increase the damage the target takes from your next Lava Lash by $s1, stacking up to 10 times."
  ),
  Azerite_Trait(
    "Lava Shock", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 273448, 178, -1, -1, 1,
    "Flame Shock damage increases the damage of your next Earth Shock by $s1, stacking up to $273453u times."
  ),
  Azerite_Trait(
    "Strength of Earth", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 273461, 179, -1, -1, 1,
    "Rockbiter causes your next melee ability, other than Rockbiter, to deal an additional $s1 Nature damage."
  ),
  Azerite_Trait(
    "Ebb and Flow", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 273597, 191, -1, -1, 1,
    "Healing Tide Totem restores up to $s1 additional health each pulse, based on how close your allies are to the totem. Maximum benefit for allies within $s2 yds of the totem."
  ),
  Azerite_Trait(
    "Serene Spirit", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 274412, 207, -1, -1, 1,
    "When you cast Astral Shift and when Astral Shift ends, heal for $s1."
  ),
  Azerite_Trait(
    "Echo of the Elementals", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 275381, 222, -1, -1, 1,
    "When your $?s192249[Storm Elemental][Fire Elemental] expires, it leaves behind a $?s192249[Spark Elemental][Ember Elemental] to continue attacking your enemies for $275385d."
  ),
  Azerite_Trait(
    "Lightning Conduit", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 275388, 223, -1, -1, 1,
    "Stormstrike makes the target as a Lightning Conduit for $275391d. Stormstrike deals $s1 Nature damage to all enemies you've marked as Conduits."
  ),
  Azerite_Trait(
    "Swelling Stream", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 275488, 224, -1, -1, 1,
    "Every $275495t1 sec a wave of water flows from your Healing Stream Totem to an injured ally, restoring $s1 health to allies in its wake."
  ),
  Azerite_Trait(
    "Overflowing Waters", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 277658, 449, -1, -1, 1,
    "Your Healing Rain is $s2 yd larger, and casting Healing Rain instantly restores $s1 health to allies within its area."
  ),
  Azerite_Trait(
    "Ancestral Harmony", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 277666, 447, -1, -1, 1,
    "When you cast $?<s2825>[Bloodlust][Heroism], your Mastery increases by $s1 every second, stacking up to $277943u times."
  ),
  Azerite_Trait(
    "Synapse Shock", [
      ("Shaman", "Elemental"),
      ("Shaman", "Enhancement"),
    ], 277671, 448, -1, -1, 1,
    "Lightning Bolt and Chain Lightning increase your $?c2[Agility][Intellect] by $s1 per target hit for $277960d, stacking up to $277960u times."
  ),
  Azerite_Trait(
    "Wracking Brilliance", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 272891, 123, -1, -1, 1,
    "Every other Soul Shard your Agony generates also increases your Intellect by $s1 for $272893d."
  ),
  Azerite_Trait(
    "Shadow's Bite", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 272944, 130, -1, -1, 1,
    "When your summoned Dreadstalkers fade away, they increase the damage of your Shadow Bolt by $s1 for $272945d."
  ),
  Azerite_Trait(
    "Heavy Rain", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 272955, 131, -1, -1, 1,
    "When your Rain of Fire damages 3 or more targets, gain $s1 Haste for $272957d."
  ),
  Azerite_Trait(
    "Erratic Omen", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 273504, 182, -1, -1, 1,
    "When your spells strike a target due to Havoc, they have a $s2% chance to deal an additional $s1 Chaos damage."
  ),
  Azerite_Trait(
    "Inevitable Demise", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 273521, 183, -1, -1, 1,
    "Damaging an enemy with Corruption increases the damage of your next Drain Life by $s1. This effect stacks up to 100 times."
  ),
  Azerite_Trait(
    "Umbral Blaze", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 273523, 190, -1, -1, 1,
    "Your Hand of Guldan has a $s2% chance to burn its target for $s1 additional Shadowflame damage every $273526t1 sec for $273526d."
  ),
  Azerite_Trait(
    "Lifeblood", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 274418, 208, -1, -1, 1,
    "When you use a Healthstone, gain $s1 Leech for $274420d"
  ),
  Azerite_Trait(
    "Cascading Calamity", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 275372, 230, -1, -1, 1,
    "Casting Unstable Affliction on a target affected by your Unstable Affliction increases your Haste by $s1 for $275378d"
  ),
  Azerite_Trait(
    "Explosive Potential", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 275395, 231, -1, -1, 1,
    "When your Implosion consumes 3 or more Imps, gain $s1 Haste for $275398d."
  ),
  Azerite_Trait(
    "Flashpoint", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 275425, 232, -1, -1, 1,
    "When your Immolate deals periodic damage to a target above 80% health, gain $s1 Haste for $275429d."
  ),
  Azerite_Trait(
    "Deathbloom", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 275974, 442, -1, -1, 1,
    "If your Seed of Corruption detonates early, it deals $s1 additional damage."
  ),
  Azerite_Trait(
    "Crashing Chaos", [
      ("Warlock", "Affliction"),
      ("Warlock", "Demonology"),
      ("Warlock", "Destruction"),
    ], 276007, 443, -1, -1, 1,
    "When you gain Demonic Core, the damage of your next Demonbolt is increased by $s1"
  ),
  Azerite_Trait(
    "Deafening Crash", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 272824, 118, -1, -1, 1,
    "Thunder Clap deals an additional $s2 damage and extends the duration of your Demoralizing Shout on affected enemies by ${$s1/1000} sec."
  ),
  Azerite_Trait(
    "Trample the Weak", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 272836, 119, -1, -1, 1,
    "Rampaging an enemy whose health percentage is lower than yours increases your Versatility by $s1 for $272838d."
  ),
  Azerite_Trait(
    "Executioner's Precision", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 272866, 121, -1, -1, 1,
    "Execute increases the damage of your next Mortal Strike against the target by $s1, stacking up to $272870u times."
  ),
  Azerite_Trait(
    "Gathering Storm", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 273409, 174, -1, -1, 1,
    "While $?s152277[Ravager is active][Bladestorming], every $273414t1 sec you gain $s2 Speed and $?s152277[Ravager's][Bladestorm's] damage increases by $s1. Lasts $273415d."
  ),
  Azerite_Trait(
    "Bloodcraze", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 273420, 176, -1, -1, 1,
    "When Bloodthirst does not critically strike, it increases your Haste by $s1 for $273428d."
  ),
  Azerite_Trait(
    "Breach", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 274563, 216, -1, -1, 1,
    "When you damage an enemy with Heroic Leap, gain $s1 Leech for $274571d."
  ),
  Azerite_Trait(
    "Test of Might", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 275529, 226, -1, -1, 1,
    "When $?s262161[Warbreaker][Colossus Smash] expires, your Strength is increased by $s1 for every $s2 Rage you spent during $?s262161[Warbreaker][Colossus Smash]. Lasts $275540d."
  ),
  Azerite_Trait(
    "Pulverizing Blows", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 275632, 229, -1, -1, 1,
    "Raging Blow causes every strike of your next Rampage to deal an additional $s1 damage. Stacks up to $275672u times."
  ),
  Azerite_Trait(
    "Reinforced Plating", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 275860, 237, -1, -1, 1,
    "Blocking an attack increases your Strength by $s1 for $275867d, stacking up to $275867u times."
  ),
  Azerite_Trait(
    "Brace for Impact", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 277636, 450, -1, -1, 1,
    "Using Shield Slam increases your Block by $s1 and the damage of your Shield Slam by $s2 for $278124d. Multiple applications of this effect may overlap."
  ),
  Azerite_Trait(
    "Infinite Fury", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 277638, 451, -1, -1, 1,
    "When Recklessness expires, your Critical Strike is increased by $s1 for $278134d. Your auto attacks will refresh the duration of this effect."
  ),
  Azerite_Trait(
    "Seismic Wave", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 277639, 433, -1, -1, 1,
    "Overpower causes a seismic wave that deals $s1 Physical damage to enemies in a $s2 yd line."
  ),
  Azerite_Trait(
    "Bloodsport", [
      ("Warrior", "Arms"),
      ("Warrior", "Fury"),
      ("Warrior", "Protection"),
    ], 279172, 177, -1, -1, 1,
    "Ignore Pain prevents $s3 additional damage, and grants you $s2 Leech for $279194d."
  ),
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

  melee, ranged, agility, intellect, strength = get_mask_for_spec(
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
