# -*- coding: utf-8 -*-
## Utility file for class specialisations
## Contains wow classes, specs, dps talent rows,
## races, trinkets

from collections import defaultdict

## Available types:
##   legendary - legendary trinkets for everyone
##   shared    - trinkets for everyone
##   melee     - agi + str (melee + sv hunter)
##   ranged    - int + agi (caster + bm/mm hunter)
##   agi       - pure agi (lether wearer + hunter)
##   int       - pure int (pure caster)
##   str       - pure str (plate wearer)


## legendary trinkets for everyone
legendary_trinkets = {}
legendary_trinkets["legendary"] = [
  [ "Kil'jaeden's Burning Wish",         "144259", 970, 1200 ],
]


## Usable by everyone
shared_trinkets = {}
shared_trinkets["dungeon"] = [
  [ "Chrono Shard",                      "137419", 840, 1200 ],
  [ "Horn of Valor",                     "133642", 805, 1200 ],
  [ "Toe Knee's Promise",                "142164", 855, 1200 ],
]
shared_trinkets["crafted"] = [
  [ "Infernal Alchemist Stone",          "127842", 815, 900  ],
  [ "Astral Alchemist Stone",            "151607", 885, 935  ],
]
shared_trinkets["world"] = [
  [ "Unstable Arcanocrystal",           "141482", 860, 1200 ],
]


## Usable by melee classes (survival hunters)
melee_trinkets = {}
melee_trinkets["crafted"] = [
  [ "Darkmoon Deck: Dominion",           "128705", 815, 900  ],
]
melee_trinkets["dungeon"] = [
  [ "Bloodstained Handkerchief",         "142159", 855, 1200 ],
  [ "Chaos Talisman",                    "137459", 805, 1200 ],
  [ "Eye of Command",                    "142167", 860, 1200 ],
  [ "Faulty Countermeasure",             "137539", 805, 1200 ],
  [ "Gift of Radiance",                  "133647", 805, 1200 ],
  [ "Giant Ornamental Pearl",            "137369", 805, 1200 ],
  [ "Mark of Dargrul",                   "137357", 805, 1200 ],
  [ "Memento of Angerboda",              "133644", 805, 1200 ],
  [ "Nightmare Egg Shell",               "137312", 805, 1200 ],
  [ "Spiked Counterweight",              "136715", 805, 1200 ],
  [ "Terrorbound Nexus",                 "137406", 840, 1200 ],
  [ "Tiny Oozeling in a Jar",            "137439", 805, 1200 ],
  [ "Windscar Whetstone",                "137486", 840, 1200 ]
]
melee_trinkets["emerald_nightmare"] = [
  [ "Nature's Call",                     "139334", 835, 1200 ],
  [ "Ravaged Seed Pod",                  "139320", 835, 1200 ],
  [ "Spontaneous Appendages",            "139325", 835, 1200 ]
]
melee_trinkets["nighthold"] = [
  [ "Draught of Souls",                  "140808", 865, 1200 ],
]
melee_trinkets["tomb_of_sargeras"] = [
  [ "Infernal Cinders",                  "147009", 885, 1200 ],
  [ "Umbral Moonglaives",                "147012", 890, 1200 ],
  [ "Vial of Ceaseless Toxins",          "147011", 890, 1200 ],
  [ "Specter of Betrayal",               "151190", 895, 1200 ]
]
melee_trinkets["world"] = [
  [ "The Devilsaur's Bite",              "140026", 805, 1200 ],
]


## Usable by casters and hunters
ranged_trinkets = {}
ranged_trinkets["dungeon"] = [
  [ "Aran's Relaxing Ruby",               "142157", 860, 1200 ],
  [ "Caged Horror",                       "136716", 840, 1200 ],
  [ "Corrupted Starlight",                "137301", 840, 1200 ],
  [ "Deteriorated Construct Core",        "142165", 860, 1200 ],
  [ "Elementium Bomb Squirrel Generator", "137446", 840, 1200 ],
  [ "Eye of Skovald",                     "133641", 840, 1200 ],
  [ "Figurehead of the Naglfar",          "137329", 840, 1200 ],
  [ "Moonlit Prism",                      "137541", 840, 1200 ],
  [ "Mrrgria's Favor",                    "142160", 855, 1200 ],
  [ "Naraxas' Spiked Tongue",             "137349", 840, 1200 ],
  [ "Oakheart's Gnarled Root",            "137306", 840, 1200 ],
  [ "Obelisk of the Void",                "137433", 840, 1200 ],
  [ "Stormsinger Fulmination Charge",     "137367", 840, 1200 ]
]
ranged_trinkets["emerald_nightmare"] = [  
  [ "Twisting Wind",                     "139323", 835, 1200 ],
  [ "Unstable Horrorslime",              "138224", 835, 1200 ]
]
ranged_trinkets["nighthold"] = [  
  [ "Fury of the Burning Sky",           "140801", 860, 1200 ],
  [ "Icon of Rot",                       "140798", 860, 1200 ] 
]
ranged_trinkets["tomb_of_sargeras"] = [
  [ "Spectral Thurible",                 "147018", 890, 1200 ],
  [ "Tarnished Sentinel Medallion",      "147017", 890, 1200 ],
  [ "Terror From Below",                 "147016", 890, 1200 ],
  [ "Tome of Unraveling Sanity",         "147019", 895, 1200 ]
]


## Usable by lether wearers and hunters
agi_trinkets = {}
agi_trinkets["dungeon"] = [
  [ "Splinters of Agronax",              "144477", 845, 1200 ],
  [ "Tempered Egg of Serpentrix",        "137373", 805, 1200 ],
  [ "Tirathon's Betrayal",               "137537", 805, 1200 ],
  [ "Void Stalker's Contract",           "151307", 845, 1200 ]
]
agi_trinkets["emerald_nightmare"] = [
  [ "Bloodthirsty Instinct",             "139329", 835, 1200 ]
]
agi_trinkets["nighthold"] = [
  [ "Arcanogolem Digit",                 "140794", 855, 1200 ],
  [ "Convergence of Fates",              "140806", 860, 1200 ],
  [ "Entwined Elemental Foci",           "140796", 860, 1200 ],
  [ "Nightblooming Frond",               "140802", 860, 1200 ]
]
agi_trinkets["pvp"] = [
  [ "PVP Insignia of Conquest",          "142662", 840, 1200 ],
  [ "PVP Badge of Conquest",             "142773", 840, 1200 ]
]
agi_trinkets["tomb_of_sargeras"] = [
  [ "Cradle of Anguish",                 "147010", 885, 1200 ],
  [ "Engine of Eradication",             "147015", 890, 1200 ]
]
agi_trinkets["world"] = [
  [ "Ley Spark",                         "140027", 805, 1200 ],
  [ "Six-Feather Fan",                   "141585", 810, 1200 ],
    # 142506 is Eye of Guarm, used as a reference stat stick
  [ "Stat Stick (Crit)",                 "142506,bonus_id=603", 865, 1200 ],
  [ "Stat Stick (Haste)",                "142506,bonus_id=604", 865, 1200 ],
  [ "Stat Stick (Mastery)",              "142506,bonus_id=605", 865, 1200 ],
  [ "Stat Stick (Versatility)",          "142506,bonus_id=607", 865, 1200 ],
  [ "Thrice-Accursed Compass",           "141537",              860, 1200 ]
]


## Usable by casters
int_trinkets = {}
int_trinkets["crafted"] = [
  [ "Darkmoon Deck: Hellfire",           "128709", 815, 900 ],
]
int_trinkets["dungeon"] = [
  [ "Dreadstone of Endless Shadows",     "144480", 845, 1200 ],
  [ "Infernal Writ",                     "137485", 840, 1200 ], 
  [ "Portable Manacracker",              "137398", 840, 1200 ],
  [ "Reality Breacher",                  "151310", 845, 1200 ],
]
int_trinkets["emerald_nightmare"] = [
  [ "Bough of Corruption",               "139323", 835, 1200 ],
  [ "Swarming Plaguehive",               "139321", 835, 1200 ],
  [ "Twisting Wind",                     "139323", 835, 1200 ],
  [ "Unstable Horrorslime",              "138224", 835, 1200 ],
  [ "Wriggling Sinew",                   "139326", 835, 1200 ]
]
int_trinkets["nighthold"] = [
  [ "Erratic Metronome",                 "140792", 855, 1200 ],
  [ "Pharameres Forbidden Grimoire",     "140800", 860, 1200 ],
  [ "Star Gate",                         "140804", 860, 1200 ],
  [ "Whispers in the Dark",              "140809", 865, 1200 ]
]
int_trinkets["pvp"] = [ 
  [ "PVP Insignia of Dominance",         "142668", 840, 1200 ],
  [ "PVP Badge of Dominance",            "142779", 840, 1200 ]
]
int_trinkets["tomb_of_sargeras"] = [
  [ "Charm of the Rising Tide",          "147002", 885, 1200 ],
]
int_trinkets["world"] = [
  [ "Devilsaur Shock-Baton",             "140030", 840, 1200 ],
  [ "Eyasu's Mulligan",                  "141584", 810, 1200 ],
  [ "Padawsen's Unlucky Charm",          "141536", 860, 1200 ],
  # 142507 is Brinewater Slime in a Bottle, used as a reference stat stick
  [ "Stat Stick (Crit)",                 "142507,bonus_id=603", 865, 1200 ],
  [ "Stat Stick (Haste)",                "142507,bonus_id=604", 865, 1200 ],
  [ "Stat Stick (Mastery)",              "142507,bonus_id=605", 865, 1200 ],
  [ "Stat Stick (Versatility)",          "142507,bonus_id=607", 865, 1200 ]
]


## Usable by plate wearers
str_trinkets = {}
str_trinkets["dungeon"] = [
  [ "Fel-Oiled Infernal Machine",        "144482", 845, 1200 ],
  [ "Void Stalker's Contract",           "151307", 845, 1200 ]
]
str_trinkets["emerald_nightmare"] = [
  [ "Ursoc's Rending Paw",               "139328", 835, 1200 ],
]
str_trinkets["nighthold"] = [
  [ "Claw of the Crystalline Scorpid",   "140790", 855, 1200 ],
  [ "Convergence of Fates",              "140806", 860, 1200 ],
  [ "Entwined Elemental Foci",           "140796", 860, 1200 ],
  [ "Might of Krosus",                   "140799", 860, 1200 ]
]
str_trinkets["pvp"] = [
  [ "PVP Insignia of Victory",           "142784", 840, 1200 ],
  [ "PVP Badge of Victory",              "142669", 840, 1200 ]
]
str_trinkets["tomb_of_sargeras"] = [
  [ "Cradle of Anguish",                 "147010", 885, 1200 ],
  [ "Engine of Eradication",             "147015", 890, 1200 ]
]
str_trinkets["world"] = [
  # 142508 is Chains of the Valorous, used as a reference stat stick
  [ "Stat Stick (Crit)",                 "142508,bonus_id=603", 865, 1200 ],
  [ "Stat Stick (Haste)",                "142508,bonus_id=604", 865, 1200 ],
  [ "Stat Stick (Mastery)",              "142508,bonus_id=605", 865, 1200 ],
  [ "Stat Stick (Versatility)",          "142508,bonus_id=607", 865, 1200 ],
  [ "Ettin Fingernail",                  "141535",              860, 1200 ]
]


__crucible_general_data = [
  {
    "id": "1779",
    "spell": {
      "id": "",
      "name": "Chaotic Darkness"
    }
  },
  {
    "id": "1781",
    "spell": {
      "id": "",
      "name": "Dark Sorrows"
    }
  },
  {
    "id": "1783",
    "spell": {
      "id": "",
      "name": "Infusion of Light"
    }
  },
  {
    "id": "1770",
    "spell": {
      "id": "",
      "name": "Light Speed"
    }
  },
  {
    "id": "1771",
    "spell": {
      "id": "",
      "name": "Master of Shadows"
    }
  },
  {
    "id": "1774",
    "spell": {
      "id": "",
      "name": "Murderous Intent"
    }
  },
  {
    "id": "1782",
    "spell": {
      "id": "",
      "name": "Secure in the Light"
    }
  },
  {
    "id": "1778",
    "spell": {
      "id": "",
      "name": "Shadowbind"
    }
  },
  {
    "id": "1777",
    "spell": {
      "id": "",
      "name": "Shocklight"
    }
  },
  {
    "id": "1780",
    "spell": {
      "id": "",
      "name": "Torment the Weak"
    }
  },
  {
    "id": "1739",
    "spell": {
      "id": "",
      "name": "+5 itemlevel"
    }
  }
]

__crucible_spec_data = {
  "Death_Knight": {
    "Blood":  [
      {
        "id": "275",
        "spell": {
          "id": "192457",
          "name": "Veinrender"
        }
      },
      {
        "id": "278",
        "spell": {
          "id": "192464",
          "name": "All-Consuming Rot"
        }
      },
      {
        "id": "276",
        "spell": {
          "id": "192460",
          "name": "Coagulopathy"
        }
      },
      {
        "id": "280",
        "spell": {
          "id": "192538",
          "name": "Bonebreaker"
        }
      },
      {
        "id": "279",
        "spell": {
          "id": "192514",
          "name": "Dance of Darkness"
        }
      }
    ],
    "Frost":  [
      {
        "id": "117",
        "spell": {
          "id": "189164",
          "name": "Dead of Winter"
        }
      },
      {
        "id": "109",
        "spell": {
          "id": "189086",
          "name": "Blast Radius"
        }
      },
      {
        "id": "114",
        "spell": {
          "id": "189147",
          "name": "Bad to the Bone"
        }
      },
      {
        "id": "110",
        "spell": {
          "id": "189092",
          "name": "Ambidexterity"
        }
      },
      {
        "id": "111",
        "spell": {
          "id": "189097",
          "name": "Over-Powered"
        }
      },
      {
        "id": "108",
        "spell": {
          "id": "189080",
          "name": "Cold as Ice"
        }
      },
      {
        "id": "113",
        "spell": {
          "id": "189144",
          "name": "Nothing but the Boots"
        }
      },
      {
        "id": "1485",
        "spell": {
          "id": "238043",
          "name": "Runefrost"
        }
      }
    ],
    "Unholy": [
      {
        "id": "264",
        "spell": {
          "id": "239107",
          "name": "Runic Tattoos"
        }
      },
      {
        "id": "158",
        "spell": {
          "id": "191485",
          "name": "Plaguebearer"
        }
      },
      {
        "id": "266",
        "spell": {
          "id": "191488",
          "name": "The Darkest Crusade"
        }
      },
      {
        "id": "157",
        "spell": {
          "id": "191442",
          "name": "Rotten Touch"
        }
      },
      {
        "id": "1119",
        "spell": {
          "id": "208598",
          "name": "Eternal Agony"
        }
      },
      {
        "id": "156",
        "spell": {
          "id": "191419",
          "name": "Deadliest Coil"
        }
      },
      {
        "id": "265",
        "spell": {
          "id": "191494",
          "name": "Scourge the Unbeliever"
        }
      },
      {
        "id": "1489",
        "spell": {
          "id": "238044",
          "name": "Lash of Shadows"
        }
      }
    ]
  },
  "Demon_Hunter": {
    "Havoc":    [ 
      {
        "id": "1003",
        "spell": {
          "id": "201457",
          "name": "Sharpened Glaives"
        }
      },
      {
        "id": "1002",
        "spell": {
          "id": "201456",
          "name": "Chaos Vision"
        }
      },
      {
        "id": "1006",
        "spell": {
          "id": "201460",
          "name": "Unleashed Demons"
        }
      },
      {
        "id": "1001",
        "spell": {
          "id": "201455",
          "name": "Critical Chaos"
        }
      },
      {
        "id": "1008",
        "spell": {
          "id": "201464",
          "name": "Overwhelming Power"
        }
      },
      {
        "id": "1000",
        "spell": {
          "id": "201454",
          "name": "Contained Fury"
        }
      },
      {
        "id": "1004",
        "spell": {
          "id": "201458",
          "name": "Demon Rage"
        }
      },
      {
        "id": "1493",
        "spell": {
          "id": "238045",
          "name": "Wide Eyes"
        }
      }
    ],
    "Vengance": [ 
      {
        "id": "1229",
        "spell": {
          "id": "207375",
          "name": "Infernal Force"
        }
      },
      {
        "id": "1101",
        "spell": {
          "id": "207352",
          "name": "Honed Warblades"
        }
      },
      {
        "id": "1231",
        "spell": {
          "id": "212817",
          "name": "Fiery Demise"
        }
      },
      {
        "id": "1100",
        "spell": {
          "id": "207347",
          "name": "Aura of Pain"
        }
      },
      {
        "id": "1497",
        "spell": {
          "id": "238046",
          "name": "Lingering Ordeal"
        }
      }
    ]
  },
  "Druid": {
    "Balance":  [ 
      {
        "id": "1039",
        "spell": {
          "id": "202433",
          "name": "Scythe of the Stars"
        }
      },
      {
        "id": "1038",
        "spell": {
          "id": "202426",
          "name": "Solar Stabbing"
        }
      },
      {
        "id": "1041",
        "spell": {
          "id": "202466",
          "name": "Sunfire Burns"
        }
      },
      {
        "id": "1037",
        "spell": {
          "id": "202386",
          "name": "Twilight Glow"
        }
      },
      {
        "id": "1042",
        "spell": {
          "id": "202464",
          "name": "Empowerment"
        }
      },
      {
        "id": "1036",
        "spell": {
          "id": "202384",
          "name": "Dark Side of the Moon"
        }
      },
      {
        "id": "1040",
        "spell": {
          "id": "202445",
          "name": "Falling Star"
        }
      },
      {
        "id": "1501",
        "spell": {
          "id": "238047",
          "name": "Light of the Evening Star"
        }
      }
    ],
    "Feral":    [ 
      {
        "id": "1164",
        "spell": {
          "id": "210579",
          "name": "Ashamane's Energy"
        }
      },
      {
        "id": "1163",
        "spell": {
          "id": "210575",
          "name": "Powerful Bite"
        }
      },
      {
        "id": "1168",
        "spell": {
          "id": "210637",
          "name": "Sharpened Claws"
        }
      },
      {
        "id": "1162",
        "spell": {
          "id": "210571",
          "name": "Feral Power"
        }
      },
      {
        "id": "1167",
        "spell": {
          "id": "210631",
          "name": "Feral Instinct"
        }
      },
      {
        "id": "1161",
        "spell": {
          "id": "210570",
          "name": "Razor Fangs"
        }
      },
      {
        "id": "1166",
        "spell": {
          "id": "210593",
          "name": "Tear the Flesh"
        }
      },
      {
        "id": "1505",
        "spell": {
          "id": "238048",
          "name": "Thrashing Claws"
        }
      }
    ],
    "Guardian": [ 
      {
        "id": "955",
        "spell": {
          "id": "208762",
          "name": "Mauler"
        }
      },
      {
        "id": "949",
        "spell": {
          "id": "200399",
          "name": "Ursoc's Endurance"
        }
      },
      {
        "id": "952",
        "spell": {
          "id": "200409",
          "name": "Jagged Claws"
        }
      },
      {
        "id": "956",
        "spell": {
          "id": "200440",
          "name": "Vicious Bites"
        }
      }
    ]
  },
  "Hunter": {
    "Beast_Mastery": [ 
      {
        "id": "872",
        "spell": {
          "id": "197139",
          "name": "Focus of the Titans"
        }
      },
      {
        "id": "870",
        "spell": {
          "id": "197080",
          "name": "Pack Leader"
        }
      },
      {
        "id": "875",
        "spell": {
          "id": "197162",
          "name": "Jaws of Thunder"
        }
      },
      {
        "id": "869",
        "spell": {
          "id": "197047",
          "name": "Furious Swipes"
        }
      },
      {
        "id": "1095",
        "spell": {
          "id": "206910",
          "name": "Unleash the Beast"
        }
      },
      {
        "id": "868",
        "spell": {
          "id": "197038",
          "name": "Wilderness Expert"
        }
      },
      {
        "id": "873",
        "spell": {
          "id": "197140",
          "name": "Spitting Cobras"
        }
      },
      {
        "id": "1517",
        "spell": {
          "id": "238051",
          "name": "Slithering Serpents"
        }
      }
    ],
    "Marksmanship":  [ 
      {
        "id": "315",
        "spell": {
          "id": "190467",
          "name": "Called Shot"
        }
      },
      {
        "id": "314",
        "spell": {
          "id": "190462",
          "name": "Quick Shot"
        }
      },
      {
        "id": "319",
        "spell": {
          "id": "190529",
          "name": "Marked for Death"
        }
      },
      {
        "id": "313",
        "spell": {
          "id": "190457",
          "name": "Windrunner's Guidance"
        }
      },
      {
        "id": "320",
        "spell": {
          "id": "190567",
          "name": "Gust of Wind"
        }
      },
      {
        "id": "312",
        "spell": {
          "id": "190449",
          "name": "Deadly Aim"
        }
      },
      {
        "id": "318",
        "spell": {
          "id": "190520",
          "name": "Precision"
        }
      },
      {
        "id": "1521",
        "spell": {
          "id": "238052",
          "name": "Unerring Arrows"
        }
      }
    ],
    "Survival":      [ 
      {
        "id": "1073",
        "spell": {
          "id": "203638",
          "name": "Raptor's Cry"
        }
      },
      {
        "id": "1072",
        "spell": {
          "id": "203578",
          "name": "Lacerating Talons"
        }
      },
      {
        "id": "1075",
        "spell": {
          "id": "203670",
          "name": "Explosive Force"
        }
      },
      {
        "id": "1071",
        "spell": {
          "id": "203577",
          "name": "My Beloved Monster"
        }
      },
      {
        "id": "1076",
        "spell": {
          "id": "203673",
          "name": "Hellcarver"
        }
      },
      {
        "id": "1070",
        "spell": {
          "id": "203566",
          "name": "Sharpened Fang"
        }
      },
      {
        "id": "1074",
        "spell": {
          "id": "203669",
          "name": "Fluffy, Go"
        }
      },
      {
        "id": "1525",
        "spell": {
          "id": "238053",
          "name": "Jaws of the Mongoose"
        }
      }
    ]
  },
  "Mage": {
    "Arcane": [ 
      {
        "id": "82",
        "spell": {
          "id": "187264",
          "name": "Aegwynn's Imperative"
        }
      },
      {
        "id": "75",
        "spell": {
          "id": "187321",
          "name": "Aegwynn's Wrath"
        }
      },
      {
        "id": "81",
        "spell": {
          "id": "187276",
          "name": "Ethereal Sensitivity"
        }
      },
      {
        "id": "74",
        "spell": {
          "id": "187258",
          "name": "Blasting Rod"
        }
      },
      {
        "id": "79",
        "spell": {
          "id": "187287",
          "name": "Aegwynn's Fury"
        }
      },
      {
        "id": "72",
        "spell": {
          "id": "187304",
          "name": "Torrential Barrage"
        }
      },
      {
        "id": "77",
        "spell": {
          "id": "187313",
          "name": "Arcane Purification"
        }
      },
      {
        "id": "1529",
        "spell": {
          "id": "238054",
          "name": "Aegwynn's Intensity"
        }
      }
    ],
    "Fire":   [ 
      {
        "id": "753",
        "spell": {
          "id": "210182",
          "name": "Blue Flame Special"
        }
      },
      {
        "id": "752",
        "spell": {
          "id": "194312",
          "name": "Burning Gaze"
        }
      },
      {
        "id": "755",
        "spell": {
          "id": "194314",
          "name": "Everburning Consumption"
        }
      },
      {
        "id": "750",
        "spell": {
          "id": "194234",
          "name": "Reignition Overdrive"
        }
      },
      {
        "id": "751",
        "spell": {
          "id": "194239",
          "name": "Pyroclasmic Paranoia"
        }
      },
      {
        "id": "749",
        "spell": {
          "id": "194224",
          "name": "Fire at Will"
        }
      },
      {
        "id": "754",
        "spell": {
          "id": "194313",
          "name": "Great Balls of Fire"
        }
      },
      {
        "id": "1533",
        "spell": {
          "id": "238055",
          "name": "Pre-Ignited"
        }
      }
    ],
    "Frost":  [ 
      {
        "id": "787",
        "spell": {
          "id": "195323",
          "name": "Orbital Strike"
        }
      },
      {
        "id": "786",
        "spell": {
          "id": "195322",
          "name": "Let It Go"
        }
      },
      {
        "id": "789",
        "spell": {
          "id": "195351",
          "name": "Clarity of Thought"
        }
      },
      {
        "id": "785",
        "spell": {
          "id": "195317",
          "name": "Ice Age"
        }
      },
      {
        "id": "790",
        "spell": {
          "id": "195352",
          "name": "The Storm Rages"
        }
      },
      {
        "id": "784",
        "spell": {
          "id": "195315",
          "name": "Icy Caress"
        }
      },
      {
        "id": "788",
        "spell": {
          "id": "195345",
          "name": "Frozen Veins"
        }
      },
      {
        "id": "1537",
        "spell": {
          "id": "238056",
          "name": "Obsidian Lance"
        }
      }
    ]
  },
  "Monk": {
    "Brewmaster": [ 
      {
        "id": "1279",
        "spell": {
          "id": "239305",
          "name": "Hot Blooded"
        }
      },
      {
        "id": "1284",
        "spell": {
          "id": "213136",
          "name": "Gifted Student"
        }
      },
      {
        "id": "1278",
        "spell": {
          "id": "213051",
          "name": "Obsidian Fists"
        }
      },
      {
        "id": "1286",
        "spell": {
          "id": "213116",
          "name": "Face Palm"
        }
      },
      {
        "id": "1541",
        "spell": {
          "id": "238057",
          "name": "Draught of Darkness"
        }
      }
    ],
    "Windwalker": [ 
      {
        "id": "822",
        "spell": {
          "id": "195266",
          "name": "Death Art"
        }
      },
      {
        "id": "821",
        "spell": {
          "id": "218607",
          "name": "Tiger Claws"
        }
      },
      {
        "id": "825",
        "spell": {
          "id": "195291",
          "name": "Fists of the Wind"
        }
      },
      {
        "id": "820",
        "spell": {
          "id": "195263",
          "name": "Rising Winds"
        }
      },
      {
        "id": "1094",
        "spell": {
          "id": "195267",
          "name": "Strength of Xuen"
        }
      },
      {
        "id": "800",
        "spell": {
          "id": "195243",
          "name": "Inner Peace"
        }
      },
      {
        "id": "824",
        "spell": {
          "id": "195269",
          "name": "Power of a Thousand Cranes"
        }
      },
      {
        "id": "1549",
        "spell": {
          "id": "238059",
          "name": "Split Personality"
        }
      }
    ]
  },
  "Paladin": {
    "Protection":  [ 
      {
        "id": "1124",
        "spell": {
          "id": "239294",
          "name": "Righteous Crusader"
        }
      },
      {
        "id": "1126",
        "spell": {
          "id": "209218",
          "name": "Consecration in Flame"
        }
      },
      {
        "id": "1122",
        "spell": {
          "id": "209217",
          "name": "Stern Judgment"
        }
      },
      {
        "id": "1121",
        "spell": {
          "id": "209229",
          "name": "Hammer Time"
        }
      }
    ],
    "Retribution": [ 
      {
        "id": "53",
        "spell": {
          "id": "186945",
          "name": "Wrath of the Ashbringer"
        }
      },
      {
        "id": "43",
        "spell": {
          "id": "184843",
          "name": "Righteous Blade"
        }
      },
      {
        "id": "51",
        "spell": {
          "id": "185368",
          "name": "Might of the Templar"
        }
      },
      {
        "id": "42",
        "spell": {
          "id": "184759",
          "name": "Sharpened Edge"
        }
      },
      {
        "id": "52",
        "spell": {
          "id": "186944",
          "name": "Protector of the Ashen Blade"
        }
      },
      {
        "id": "41",
        "spell": {
          "id": "186941",
          "name": "Highlord's Judgment"
        }
      },
      {
        "id": "50",
        "spell": {
          "id": "186927",
          "name": "Deliver the Justice"
        }
      },
      {
        "id": "1561",
        "spell": {
          "id": "238062",
          "name": "Righteous Verdict"
        }
      }
    ]
  },
  "Priest": {
    "Shadow": [ 
      {
        "id": "774",
        "spell": {
          "id": "193645",
          "name": "Death's Embrace"
        }
      },
      {
        "id": "773",
        "spell": {
          "id": "193644",
          "name": "To the Pain"
        }
      },
      {
        "id": "778",
        "spell": {
          "id": "194016",
          "name": "Void Corruption"
        }
      },
      {
        "id": "772",
        "spell": {
          "id": "193643",
          "name": "Mind Shattering"
        }
      },
      {
        "id": "776",
        "spell": {
          "id": "194002",
          "name": "Creeping Shadows"
        }
      },
      {
        "id": "767",
        "spell": {
          "id": "194093",
          "name": "Unleash the Shadows"
        }
      },
      {
        "id": "777",
        "spell": {
          "id": "194007",
          "name": "Touch of Darkness"
        }
      },
      {
        "id": "1573",
        "spell": {
          "id": "238065",
          "name": "Fiending Dark"
        }
      }
    ]
  },
  "Rogue": {
    "Assassination": [ 
      {
        "id": "327",
        "spell": {
          "id": "192326",
          "name": "Balanced Blades"
        }
      },
      {
        "id": "325",
        "spell": {
          "id": "192318",
          "name": "Master Alchemist"
        }
      },
      {
        "id": "330",
        "spell": {
          "id": "192349",
          "name": "Master Assassin"
        }
      },
      {
        "id": "324",
        "spell": {
          "id": "192315",
          "name": "Serrated Edge"
        }
      },
      {
        "id": "331",
        "spell": {
          "id": "192376",
          "name": "Poison Knives"
        }
      },
      {
        "id": "323",
        "spell": {
          "id": "192310",
          "name": "Toxic Blades"
        }
      },
      {
        "id": "328",
        "spell": {
          "id": "192329",
          "name": "Gushing Wound"
        }
      },
      {
        "id": "1577",
        "spell": {
          "id": "238066",
          "name": "Strangler"
        }
      }
    ],
    "Outlaw":        [ 
      {
        "id": "1063",
        "spell": {
          "id": "202522",
          "name": "Gunslinger"
        }
      },
      {
        "id": "1061",
        "spell": {
          "id": "202514",
          "name": "Fate's Thirst"
        }
      },
      {
        "id": "1065",
        "spell": {
          "id": "202530",
          "name": "Fortune Strikes"
        }
      },
      {
        "id": "1060",
        "spell": {
          "id": "202507",
          "name": "Blade Dancer"
        }
      },
      {
        "id": "1067",
        "spell": {
          "id": "202907",
          "name": "Fortune's Boon"
        }
      },
      {
        "id": "1059",
        "spell": {
          "id": "216230",
          "name": "Black Powder"
        }
      },
      {
        "id": "1064",
        "spell": {
          "id": "202524",
          "name": "Fatebringer"
        }
      },
      {
        "id": "1062",
        "spell": {
          "id": "202521",
          "name": "Fortune's Strike"
        }
      },
      {
        "id": "1581",
        "spell": {
          "id": "238067",
          "name": "Sabermetrics"
        }
      }
    ],
    "Subtlety":      [ 
      {
        "id": "855",
        "spell": {
          "id": "197235",
          "name": "Precision Strike"
        }
      },
      {
        "id": "854",
        "spell": {
          "id": "197234",
          "name": "Gutripper"
        }
      },
      {
        "id": "857",
        "spell": {
          "id": "197386",
          "name": "Soul Shadows"
        }
      },
      {
        "id": "853",
        "spell": {
          "id": "197233",
          "name": "Demon's Kiss"
        }
      },
      {
        "id": "858",
        "spell": {
          "id": "197239",
          "name": "Energetic Stabbing"
        }
      },
      {
        "id": "852",
        "spell": {
          "id": "197231",
          "name": "The Quiet Knife"
        }
      },
      {
        "id": "856",
        "spell": {
          "id": "197369",
          "name": "Fortune's Bite"
        }
      },
      {
        "id": "1585",
        "spell": {
          "id": "238068",
          "name": "Weak Point"
        }
      }
    ]
  },
  "Shaman": {
    "Elemental":   [
      {
        "id": "301",
        "spell": {
          "id": "191740",
          "name": "Firestorm"
        }
      },
      {
        "id": "300",
        "spell": {
          "id": "191504",
          "name": "Lava Imbued"
        }
      },
      {
        "id": "304",
        "spell": {
          "id": "191577",
          "name": "Electric Discharge"
        }
      },
      {
        "id": "299",
        "spell": {
          "id": "191499",
          "name": "The Ground Trembles"
        }
      },
      {
        "id": "306",
        "spell": {
          "id": "191598",
          "name": "Earthen Attunement"
        }
      },
      {
        "id": "298",
        "spell": {
          "id": "191493",
          "name": "Call the Thunder"
        }
      },
      {
        "id": "303",
        "spell": {
          "id": "191572",
          "name": "Molten Blast"
        }
      },
      {
        "id": "1589",
        "spell": {
          "id": "238069",
          "name": "Elemental Destabilization"
        }
      }
    ],
    "Enhancement": [ 
      {
        "id": "910",
        "spell": {
          "id": "198292",
          "name": "Wind Strikes"
        }
      },
      {
        "id": "908",
        "spell": {
          "id": "198247",
          "name": "Wind Surge"
        }
      },
      {
        "id": "913",
        "spell": {
          "id": "198349",
          "name": "Gathering of the Maelstrom"
        }
      },
      {
        "id": "906",
        "spell": {
          "id": "198236",
          "name": "Forged in Lava"
        }
      },
      {
        "id": "907",
        "spell": {
          "id": "198238",
          "name": "Spirit of the Maelstrom"
        }
      },
      {
        "id": "905",
        "spell": {
          "id": "215381",
          "name": "Weapons of the Elements"
        }
      },
      {
        "id": "912",
        "spell": {
          "id": "198299",
          "name": "Gathering Storms"
        }
      },
      {
        "id": "1593",
        "spell": {
          "id": "238070",
          "name": "Crashing Hammer"
        }
      }
    ]
  },
  "Warlock": {
    "Affliction":  [
      {
        "id": "918",
        "spell": {
          "id": "199152",
          "name": "Inherently Unstable"
        }
      },
      {
        "id": "917",
        "spell": {
          "id": "199120",
          "name": "Drained to a Husk"
        }
      },
      {
        "id": "920",
        "spell": {
          "id": "199158",
          "name": "Perdition"
        }
      },
      {
        "id": "916",
        "spell": {
          "id": "199112",
          "name": "Hideous Corruption"
        }
      },
      {
        "id": "921",
        "spell": {
          "id": "199163",
          "name": "Shadowy Incantations"
        }
      },
      {
        "id": "915",
        "spell": {
          "id": "199111",
          "name": "Inimitable Agony"
        }
      },
      {
        "id": "919",
        "spell": {
          "id": "199153",
          "name": "Seeds of Doom"
        }
      },
      {
        "id": "1601",
        "spell": {
          "id": "238072",
          "name": "Winnowing"
        }
      }
    ],
    "Demonology":  [ 
      {
        "id": "1174",
        "spell": {
          "id": "211123",
          "name": "Sharpened Dreadfangs"
        }
      },
      {
        "id": "1173",
        "spell": {
          "id": "211106",
          "name": "The Doom of Azeroth"
        }
      },
      {
        "id": "1176",
        "spell": {
          "id": "211119",
          "name": "Infernal Furnace"
        }
      },
      {
        "id": "1172",
        "spell": {
          "id": "211126",
          "name": "Legionwrath"
        }
      },
      {
        "id": "1177",
        "spell": {
          "id": "211099",
          "name": "Maw of Shadows"
        }
      },
      {
        "id": "1171",
        "spell": {
          "id": "211108",
          "name": "Summoner's Prowess"
        }
      },
      {
        "id": "1175",
        "spell": {
          "id": "211105",
          "name": "Dirty Hands"
        }
      },
      {
        "id": "1605",
        "spell": {
          "id": "238073",
          "name": "Left Hand of Darkness"
        }
      }
    ],
    "Destruction": [ 
      {
        "id": "807",
        "spell": {
          "id": "196227",
          "name": "Residual Flames"
        }
      },
      {
        "id": "806",
        "spell": {
          "id": "196222",
          "name": "Fire and the Flames"
        }
      },
      {
        "id": "809",
        "spell": {
          "id": "196432",
          "name": "Burning Hunger"
        }
      },
      {
        "id": "805",
        "spell": {
          "id": "196217",
          "name": "Chaotic Instability"
        }
      },
      {
        "id": "810",
        "spell": {
          "id": "196258",
          "name": "Fire From the Sky"
        }
      },
      {
        "id": "804",
        "spell": {
          "id": "196211",
          "name": "Master of Disaster"
        }
      },
      {
        "id": "808",
        "spell": {
          "id": "196236",
          "name": "Soulsnatcher"
        }
      },
      {
        "id": "811",
        "spell": {
          "id": "196301",
          "name": "Devourer of Life"
        }
      },
      {
        "id": "1609",
        "spell": {
          "id": "238074",
          "name": "Flames of Sargeras"
        }
      }
    ]
  },
  "Warrior": {
    "Arms":       [ 
      {
        "id": "1146",
        "spell": {
          "id": "216274",
          "name": "Many Will Fall"
        }
      },
      {
        "id": "1145",
        "spell": {
          "id": "209472",
          "name": "Crushing Blows"
        }
      },
      {
        "id": "1149",
        "spell": {
          "id": "248579",
          "name": "Precise Strikes"
        }
      },
      {
        "id": "1144",
        "spell": {
          "id": "209462",
          "name": "One Against Many"
        }
      },
      {
        "id": "1150",
        "spell": {
          "id": "209494",
          "name": "Exploit the Weakness"
        }
      },
      {
        "id": "1143",
        "spell": {
          "id": "209459",
          "name": "Unending Rage"
        }
      },
      {
        "id": "1147",
        "spell": {
          "id": "209481",
          "name": "Deathblow"
        }
      },
      {
        "id": "1613",
        "spell": {
          "id": "238075",
          "name": "Storm of Swords"
        }
      }
    ],
    "Fury":       [ 
      {
        "id": "991",
        "spell": {
          "id": "200853",
          "name": "Unstoppable"
        }
      },
      {
        "id": "990",
        "spell": {
          "id": "200849",
          "name": "Wrath and Fury"
        }
      },
      {
        "id": "995",
        "spell": {
          "id": "200860",
          "name": "Unrivaled Strength"
        }
      },
      {
        "id": "989",
        "spell": {
          "id": "216273",
          "name": "Wild Slashes"
        }
      },
      {
        "id": "996",
        "spell": {
          "id": "200861",
          "name": "Raging Berserker"
        }
      },
      {
        "id": "988",
        "spell": {
          "id": "200846",
          "name": "Deathdealer"
        }
      },
      {
        "id": "992",
        "spell": {
          "id": "200856",
          "name": "Uncontrolled Rage"
        }
      },
      {
        "id": "1617",
        "spell": {
          "id": "238076",
          "name": "Pulse of Battle"
        }
      }
    ],
    "Protection": [ 
      {
        "id": "101",
        "spell": {
          "id": "203227",
          "name": "Intolerance"
        }
      },
      {
        "id": "96",
        "spell": {
          "id": "216272",
          "name": "Rage of the Fallen"
        }
      },
      {
        "id": "102",
        "spell": {
          "id": "188639",
          "name": "Shatter the Bones"
        }
      },
      {
        "id": "106",
        "spell": {
          "id": "188644",
          "name": "Thunder Crash"
        }
      }
    ]
  }
}

__classes_data = {
  "Death_Knight": {
    "talents": "1110011",
    "specs": {
      "Blood":  { "role": "melee", "stat": "str" },
      "Frost":  { "role": "melee", "stat": "str" },
      "Unholy": { "role": "melee", "stat": "str" }
    }
  },
  "Demon_Hunter": {
    "talents": "1110111",
    "specs": {
      "Havoc":    { "role": "melee", "stat": "agi" },
      "Vengance": { "role": "melee", "stat": "agi" }
    }
  },
  "Druid": {
    "talents": "1000111",
    "specs": { 
      "Balance":  { "role": "ranged", "stat": "int" },
      "Feral":    { "role": "melee",  "stat": "agi" },
      "Guardian": { "role": "melee",  "stat": "agi" }
    }
  },
  "Hunter": {
    "talents": "1101011",
    "specs": {
      "Beast_Mastery": { "role": "ranged", "stat": "agi" },
      "Marksmanship":  { "role": "ranged", "stat": "agi" },
      "Survival":      { "role": "melee",  "stat": "agi" }
    }
  },
  "Mage": {
    "talents": "1011011",
    "specs": {
      "Arcane": { "role": "ranged", "stat": "int" },
      "Fire":   { "role": "ranged", "stat": "int" },
      "Frost":  { "role": "ranged", "stat": "int" }
    }
  },
  "Monk": {
    "talents": "1010011",
    "specs": {
      "Brewmaster": { "role": "melee", "stat": "agi" },
      "Windwalker": { "role": "melee", "stat": "agi" }
    }
  },
  "Paladin": {
    "talents": "1101001",
    "specs": {
      "Protection":  { "role": "melee", "stat": "str" },
      "Retribution": { "role": "melee", "stat": "str" }
    }
  },
  "Priest": {
    "talents": "1001111",
    "specs": {
      "Shadow": { "role": "ranged", "stat": "int" }
    }
  },
  "Rogue": {
    "talents": "1110111",
    "specs": {
      "Assassination": { "role": "melee", "stat": "agi" },
      "Outlaw":        { "role": "melee", "stat": "agi" },
      "Subtlety":      { "role": "melee", "stat": "agi" }
    }
  },
  "Shaman": {
    "talents": "1001111",
    "specs": {
      "Elemental":   { "role": "ranged", "stat": "int" },
      "Enhancement": { "role": "melee",  "stat": "agi" }
    }
  },
  "Warlock": {
    "talents": "1101011",
    "specs": {
      "Affliction":  { "role": "ranged", "stat": "int" },
      "Demonology":  { "role": "ranged", "stat": "int" },
      "Destruction": { "role": "ranged", "stat": "int" }
    }
  },
  "Warrior": {
    "talents": "1010111",
    "specs": {
      "Arms":       { "role": "melee", "stat": "str" },
      "Fury":       { "role": "melee", "stat": "str" },
      "Protection": { "role": "melee", "stat": "str" }
    }
  }
}

__races = {
  "alliance": {
    "draenei":  (),
    "dwarf":    (),
    "gnome":    (),
    "human":    (),
    "nightelf": (),
    "pandaren": (),
    "worgen":   ()
  },
  "horde": {
    "bloodelf": (),
    "goblin":   (),
    "orc":      (),
    "pandaren": (),
    "tauren":   (),
    "troll":    (),
    "undead":   ()
  }
}



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


##
## @brief      Combines role and stat trinket
##
## @param      role_trinkets  The trinkets relevant to role (ranged/melee) as a
##                            dict of lists
## @param      stat_trinkets  The trinkets relevant to a spec's stat
##                            (int/str/agi) as a dict of lists
##
## @return     A group of trinkets relevant to the spec as a dictionary of lists
##
def __combine_trinket_dicts(role_trinkets, stat_trinkets):  
  # Populate a new trinkets dict with role trinkets
  trinkets = role_trinkets

  for source in stat_trinkets:
    if trinkets.get(source) is not None:
      # Append int/str/agi trinkets to existing list in the newly created dict
      trinkets[source] = trinkets[source] + stat_trinkets[source]
    else:
      # Just set the int/str/agi trinket list to the newly created dict's source key  
      trinkets[source] = stat_trinkets[source]
  for source in shared_trinkets:
    if trinkets.get(source) is not None:
      trinkets[source] = trinkets[source] + shared_trinkets[source]
    else:
      trinkets[source] = shared_trinkets[source]
  for source in legendary_trinkets:
    if trinkets.get(source) is not None:
      trinkets[source] = trinkets[source] + legendary_trinkets[source]
    else:
      trinkets[source] = legendary_trinkets[source]
  return trinkets



##
## @brief      Generates all possible talent combinations for simc depending on
##             blueprint and wow_lib.get_dps_talents
##
## @param      blueprint  The blueprint
##
## @return     List of all possible talent combinations
##
def __generate_talent_combinations( blueprint, wow_class, wow_spec ):
  if not ( "x" in blueprint or "-" in blueprint ):
    return [blueprint]
  data_talents = get_dps_talents( wow_class )
  pattern = ""

  for i in range( 0, 7 ):
    if ( blueprint[i] == "-" or blueprint[i] == "x" ) and data_talents[i] == "0":
      pattern += "0"
    else:
      pattern += blueprint[i]

  combinations = []
  for first in range( 4 ):
    for second in range( 4 ):
      for third in range( 4 ):
        for forth in range( 4 ):
          for fivth in range( 4 ):
            for sixth in range( 4 ):
              for seventh in range( 4 ):
                combination = str( first ) + str( second ) + str( third ) + str( forth ) + str( fivth ) + str( sixth ) + str( seventh )
                add_it = True

                # check whether the generated talent combination fits the wanted blueprint
                for i in range( 7 ):
                  if ( not ( pattern[i] == "-" or pattern[i] == "x" ) ) and not combination[i] == pattern[i]:
                    add_it = False
                  if combination[i] == "0" and ( pattern[i] == "-" or pattern[i] == "x" ):
                    add_it = False
                if add_it:
                  combinations += [combination]
  return combinations


##
## @brief      Determines if talent input from user is in a valid format.
##
## @param      talent_combination  The talent combination
##
## @return     True if talent input is valid, False otherwise.
##
def is_talent_combination( talent_combination ):
  if talent_combination == None:
    return False
  if not type( talent_combination ) is str:
    return False
  if talent_combination == "":
    return True
  if len( talent_combination ) == 7:
    for letter in talent_combination:
      if not ( letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "-" or letter == "x" ):
        return False
    return True
  elif len( talent_combination ) == 2:
    for letter in talent_combination:
      if not ( letter == "0" or letter == "1" or letter == "2" or letter == "3" ):
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


##
## @brief      Gets the crucible traits.
##
## @param      wow_class  The wow class
## @param      wow_spec   The wow specifier
##
## @return     The crucible traits list.
##
def get_crucible_traits(wow_class, wow_spec):
  crucible_list = __crucible_general_data
  # add all spec specific traits to the list
  for trait in __crucible_spec_data[wow_class][wow_spec]:
    crucible_list.append(trait)

  return crucible_list


##
## @brief      Gets the crucible spec traits.
##
## @param      wow_class  The wow class
## @param      wow_spec   The wow specifier
##
## @return     The crucible specifier traits.
##
def get_crucible_spec_traits( wow_class, wow_spec ):
  return __crucible_spec_data[wow_class][wow_spec]


##
## @brief      Gets the crucible light shadow traits.
##
## @return     The crucible light shadow traits.
##
def get_crucible_light_shadow_traits():
  return __crucible_general_data


##
## @brief      Gets the possible talent combinations based on user_input. Either
##             all possible combinations or just a collection of those that fit
##             user_input.
##
## @param      user_input  The user input for talents
## @param      wow_class   The wow class
## @param      wow_spec    The wow spec
##
## @return     The possible talent combinations as a list.
##
def get_talent_combinations( wow_class, wow_spec, user_input = "" ):
  combination = []

  if user_input == "" or user_input == None:
    combinations = __generate_talent_combinations( "xxxxxxx", wow_class, wow_spec )

  elif len( user_input ) == 2:
    combinations = __generate_talent_combinations( "xxxxx" + user_input, wow_class, wow_spec )

  elif len( user_input ) == 7:
    combinations = __generate_talent_combinations( user_input, wow_class, wow_spec )

  else:
    sys.exit( "Something went wrong when generating talent combinations. Please recheck your user_input and settings" )

  return combinations


##
## @brief      Function to test a trinket group for data
##
## @param      trinket_group  The trinket group
##
## @return     True
##
def __test_trinkets(trinket_group):
  for location in trinket_group:
    print("  Location: " + location)
    for trinket in trinket_group[location]:
      print("    Name:\t\t" + trinket[0])
      print("    ID:\t\t\t" + trinket[1])
      print("    Min-iLevel:\t" + str(trinket[2]))
      print("    Max-iLevel:\t" + str(trinket[3]))
      print("")
  return True


##
## @brief      Gets the wow classes.
##
## @return     The classes list.
##
def get_classes():
  classes = []
  for wow_class in __classes_data:
    classes.append(wow_class)
  return classes


##
## @brief      Gets the races.
##
## @return     The races lists.
##
def get_races():
  races = []
  for faction in __races:
    for race in __races[faction]:
      races.append(race)
  return races


##
## @brief      Gets the role from class and spec.
##
## @param      wow_class  The class name as string
## @param      wow_spec   The specifier name as string
##
## @return     The role as string.
##
def get_role(wow_class, wow_spec):
  return __classes_data[wow_class.title()]["specs"][wow_spec.title()]["role"]


##
## @brief      Gets the main stat like agi, str or int.
##
## @param      wow_class  The class name as string
## @param      wow_spec   The specifier name as string
##
## @return     The main stat as string.
##
def get_stat(wow_class, wow_spec):
  return __classes_data[wow_class.title()]["specs"][wow_spec.title()]["stat"]


##
## @brief      Gets the dps talents. 0-no dps row, 1-dps row
##
## @param      wow_class  The class name
## @param      wow_spec   For people who think spec is important...it isn't
##
## @return     The dps talents as string.
##
def get_dps_talents(wow_class, wow_spec=""):
  return __classes_data[wow_class.title()]["talents"]


##
## @brief      Gets the specs of a class.
##
## @param      wow_class  The class name
##
## @return     The specs as a list.
##
def get_specs(wow_class):
  spec_collection = []
  for spec in __classes_data[wow_class.title()]["specs"]:
    spec_collection.append(spec)
  return spec_collection


##
## @brief      Determines if class is a wow class.
##
## @param      wow_class  The class name
##
## @return     True if class, False otherwise.
##
def is_class(wow_class):
  for base_class in get_classes():
    if wow_class.lower() == base_class.lower():
      return True
  return False


##
## @brief      Determines if race.
##
## @param      race  The race
##
## @return     True if race, False otherwise.
##
def is_race(race):
  if race in get_races():
    return True
  return False


##
## @brief      Determines if specis of class.
##
## @param      wow_spec   The specifier name
##
## @return     True if spec exists in wow, False otherwise.
##
def is_spec( wow_spec ):
  spec_list = []
  classes = get_classes()
  for wow_class in classes:
    specs = get_specs( wow_class )
    for spec in specs:
      spec_list.append( spec )
  for spec in spec_list:
    if wow_spec.lower() == spec.lower():
      return True
  return False


##
#-------------------------------------------------------------------------------------
# Higher functions
#-------------------------------------------------------------------------------------
##


##
## @brief      Gets the role and main stat.
##
## @param      wow_class  The class name as string
## @param      wow_spec   The specifier name as string
##
## @return     [role s, main_stat s]
##
def get_role_stat(wow_class, wow_spec):
  return [get_role(wow_class, wow_spec), get_stat(wow_class, wow_spec)]


##
## @brief      Gets the role, main_stat and dps_talent_rows.
##
## @param      wow_class  The wow class
## @param      wow_spec   The wow specifier
##
## @return     [role s, main_stat s, dps_talents s]
##
def get_spec_info(wow_class, wow_spec):
  return [
    get_role(wow_class, wow_spec), 
    get_stat(wow_class, wow_spec), 
    get_dps_talents(wow_class)
  ]


##
## @brief      Gets the main stat and role
##
## @param      wow_class  The class name as string
## @param      wow_spec   The specifier name as string
##
## @return     List of [main_stat, role]
##
def get_stat_role(wow_class, wow_spec):
  return [
    get_stat(wow_class, wow_spec),
    get_role(wow_class, wow_spec)
  ]


##
## @brief      Determines if class and spec are correct and fit each other.
##
## @param      wow_class  The wow class
## @param      wow_spec   The wow specifier
##
## @return     True if class specifier, False otherwise.
##
def is_class_spec(wow_class, wow_spec):
  if is_class(wow_class):
    if is_spec(wow_spec):
      for spec in get_specs(wow_class):
        if wow_spec.lower() == spec.lower():
          return True
  return False


##
## @brief      Determines if dps talent combination fits data.
##
## @param      talent_combination  The talent combination
## @param      wow_class           The wow class
##
## @return     True if dps talent combination fits, False otherwise.
##
def is_dps_talent_combination(talent_combination, wow_class):
  for i in range(0, 7):
    if talent_combination[i] == "0" and __classes_data[wow_class]["talents"][i] == "1":
      return False
    elif not talent_combination[i] == "0" and __classes_data[wow_class]["talents"][i] == "0":
      return False
  return True


##
## @brief      Simple data check
##
## @return     True if data doesn't have obvious flaws, False otherwise.
##
def __validity_check():
  for wow_class in __classes_data:
    for spec in get_specs(wow_class):
      if (get_role(wow_class, wow_spec) == "ranged" and get_stat(wow_class, wow_spec) == "str") or (get_role(wow_class, wow_spec) == "melee" and get_stat(wow_class, wow_spec) == "int"):
        return False
  return True

##
## @brief      Uses class and spec names to return a dict of relevant trinkets
##
## @param      class_name  The class name as string
## @param      spec_name   The specifier name as string
##
## @return     Relevant trinkets as a dict of lists
##
def get_trinkets_for_spec(class_name, spec_name):
  spec_info = get_role_stat(class_name, spec_name)
  role_trinkets, stat_trinkets = __get_relevant_trinkets(spec_info[0], spec_info[1])
  combined_trinkets = __combine_trinket_dicts(role_trinkets, stat_trinkets)
  return combined_trinkets





if __name__ == '__main__':
  print("Selftest")
  print("Testing Legendary trinkets.")
  __test_trinkets(legendary_trinkets)
  print("Done")
  print("Testing Shared Trinkets.")
  __test_trinkets(shared_trinkets)
  print("Done")
  print("Testing Melee Trinkets.")
  __test_trinkets(melee_trinkets)
  print("Done")
  print("Testing Ranged Trinkets.")
  __test_trinkets(ranged_trinkets)
  print("Done")
  print("Testing Agi Trinkets.")
  __test_trinkets(agi_trinkets)
  print("Done")
  print("Testing Int Trinkets.")
  __test_trinkets(int_trinkets)
  print("Done")
  print("Testing Str Trinkets.")
  __test_trinkets(str_trinkets)
  print("Done")
  print("Testing spec validity.")
  if __validity_check():
    print("Data looks clean.")
  else:
    print("Data seems to be incorrect.")
