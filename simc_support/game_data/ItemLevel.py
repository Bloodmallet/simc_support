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

KORTHIA = [200, 207, 213, 220, 226, 233]

DUNGEON_NORMAL = 184
DUNGEON_HEROIC = 197
DUNGEON_MYTHIC = 210
DUNGEON_MYTHIC_LEVELS = [
    # 187,
    # 190,
    # 194,
    # 197,
    # 200,
    # 203,  # weekly
    # 204,
    # 207,
    210,
    213,
    216,
    220,
    223,
    226,  # + weekly
    229,  # + weekly
    233,  # + weekly
    236,  # + weekly
    239,  # weekly
    242,  # weekly
    246,  # weekly
    249,  # weekly
    252,  # weekly
]
DUNGEON = [DUNGEON_NORMAL] + [DUNGEON_HEROIC] + [DUNGEON_MYTHIC] + DUNGEON_MYTHIC_LEVELS
TAZAVESH = [226, 233]
WORLD_BOSS_CHAINS_OF_DEVASTATION = 233

# raids
CASTLE_NATHRIA = [187, 200, 213, 226]
CASTLE_NATHRIA_ENDBOSSES = list([ilvl + 7 for ilvl in CASTLE_NATHRIA])

SANCTUM_OF_DOMINATION = [213, 226, 239, 252]
SANCTUM_OF_DOMINATION_ENDBOSSES = list([ilvl + 7 for ilvl in SANCTUM_OF_DOMINATION])

UPPER_BOUND = CASTLE_NATHRIA_ENDBOSSES[-1]

PVP_HONOR = [
    # 158,
    # 164,
    # 171,
    177,
    184,
    190,
    197,
    203,  # 9.1
    210,  # 9.1
    216,  # 9.1
]
PVP_CONQUEST = [
    # 200,
    # 207,
    # 213,
    220,
    226,
    233,  # 9.1
    240,  # 9.1
    246,  # 9.1
]
PVP = PVP_HONOR + PVP_CONQUEST


RARE_MOB = {
    155: [
        155,
        164,
    ]
}
