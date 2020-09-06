# these values are used throughout the code to determine itemlevel "borders" of items
# usually used as a catch up mechanic, drops usually all items from previous content
TRADER_TOKEN = -1
WORLD_QUEST_ITEMLEVELS = [
    144,
]  # guess
# standard dungeon itemlevel (normal, max level dungeon)
DUNGEON_ITEMLEVEL = 157  # 183 is mythic
# highest available itemlevel from m+ dungeons. weekly chest is NOT included here
M_PLUS_ITEMLEVEL = 213
# titanforging is dead, this now reflects the weekly chest
WEEKLY_CHEST = 226

# world related
EMISSARY = 170  # guess

# raids
CASTLE_NATHRIA = [187, 200, 213, 226]
CASTLE_NATHRIA_ENDBOSSES = [ilvl + 7 for ilvl in CASTLE_NATHRIA]

STEP_SIZE = 13

UPPER_BOUND = CASTLE_NATHRIA_ENDBOSSES[-1]
