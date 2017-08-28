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
  [ "Astral Alchemist Stone",            "151607", 885, 955  ],
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
      "Subtlety":       { "role": "melee", "stat": "agi" }
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
