import typing

# these values are used throughout the code to determine itemlevel "borders" of items
# usually used as a catch up mechanic, drops usually all items from previous content
TRADER_TOKEN = -1
WORLD_QUEST_ITEMLEVELS = [
    144,
    148,
    161,
    171,
    200,
    213,
]  # guess
CALLINGS = WORLD_QUEST_ITEMLEVELS

KORTHIA = [200, 207, 213, 220, 226, 233]

ZERETH_MORTIS = [
    226,
    242,  # some world quest can drop them at a higher itemlevel
]

DUNGEON_NORMAL = 210
DUNGEON_HEROIC = 223
DUNGEON_MYTHIC = 236
# https://www.wowhead.com/guides/season-3-shadowlands-mythic-plus-updates-item-levels
DUNGEON_MYTHIC_DROPS = [
    236,
    239,
    242,
    246,
    249,
    252,  # + weekly
    255,  # + weekly
    259,  # + weekly
    262,  # + weekly
]
DUNGEON_MYTHIC_LEVELS = [
    236,
    239,
    242,
    246,
    249,
    252,  # + weekly
    255,  # + weekly
    259,  # + weekly
    262,  # + weekly
    265,  # weekly
    268,  # weekly
    272,  # weekly
    275,  # weekly
    278,  # weekly
]
VALOR_UPGRADES: typing.List[int] = [
    236,
    239,
    242,
    246,
    249,
    252,
    255,
    259,
    262,
    265,
    268,
    272,
]
DUNGEON = [DUNGEON_NORMAL] + [DUNGEON_HEROIC] + [DUNGEON_MYTHIC] + DUNGEON_MYTHIC_LEVELS
TAZAVESH = [226, 233]
WORLD_BOSS_CHAINS_OF_DEVASTATION = 233
WORLD_BOSS_ZERETH_MORTIS = 259

# raids
CASTLE_NATHRIA = [187, 200, 213, 226]
CASTLE_NATHRIA_ENDBOSSES = list([ilvl + 7 for ilvl in CASTLE_NATHRIA])

SANCTUM_OF_DOMINATION = [213, 226, 239, 252]
SANCTUM_OF_DOMINATION_ENDBOSSES = list([ilvl + 7 for ilvl in SANCTUM_OF_DOMINATION])

SEPULCHER_OF_THE_FIRST_ONES = [239, 252, 265, 278]
SEPULCHER_OF_THE_FIRST_ONES_ENDBOSSES = list(
    [ilvl + 7 for ilvl in SEPULCHER_OF_THE_FIRST_ONES]
)

UPPER_BOUND = SANCTUM_OF_DOMINATION_ENDBOSSES[-1]

PVP_HONOR = [
    239,
    242,
    246,
    249,
    252,
    255,
    259,
]
PVP_CONQUEST = [
    249,
    252,
    255,
    259,
    262,
    265,
    268,
    272,
    275,
]
PVP = PVP_HONOR + PVP_CONQUEST


RARE_MOB = {
    155: [
        155,
        164,
    ]
}
