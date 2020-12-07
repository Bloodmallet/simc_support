# these values are used throughout the code to determine itemlevel "borders" of items
# usually used as a catch up mechanic, drops usually all items from previous content
TRADER_TOKEN = -1
WORLD_QUEST_ITEMLEVELS = [
    144,
    148,
    161,
    171,
    200,
]  # guess
CALLINGS = WORLD_QUEST_ITEMLEVELS

DUNGEON_NORMAL = 158
DUNGEON_HEROIC = 171
DUNGEON_MYTHIC = 184
DUNGEON_MYTHIC_LEVELS = [
    187,
    190,
    194,
    197,
    200,
    203,  # weekly
    204,
    207,
    210,
    213,  # weekly
    216,  # weekly
    220,  # weekly
    223,  # weekly
    226,  # weekly
]
DUNGEON = [DUNGEON_NORMAL] + [DUNGEON_HEROIC] + [DUNGEON_MYTHIC] + DUNGEON_MYTHIC_LEVELS

# raids
CASTLE_NATHRIA = [187, 200, 213, 226]
CASTLE_NATHRIA_ENDBOSSES = list([ilvl + 7 for ilvl in CASTLE_NATHRIA])

UPPER_BOUND = CASTLE_NATHRIA_ENDBOSSES[-1]

PVP_HONOR = [
    158,
    164,
    171,
    177,
    184,
    190,
    197,
]
PVP_CONQUEST = [
    200,
    207,
    213,
    220,
    226,
]
PVP = PVP_HONOR + PVP_CONQUEST


RARE_MOB = {
    155: [
        155,
        164,
    ]
}
