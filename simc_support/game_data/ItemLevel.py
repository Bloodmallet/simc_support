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
    246,
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
SEASON_4_DUNGEON = [
    262,
    265,
    268,
    272,
    275,
    278,  # + weekly
    281,  # + weekly
    285,  # + weekly
    288,  # + weekly
    291,  # weekly
    294,  # weekly
    298,  # weekly
    301,  # weekly
    304,  # weekly
]
TAZAVESH = [226, 233]
WORLD_BOSS_CHAINS_OF_DEVASTATION = 233
WORLD_BOSS_ZERETH_MORTIS = 259

# raids
SEASON_4_RAID = [265, 278, 291, 304]
SEASON_4_RAID_ENDBOSSES = [272, 285, 297, 311]

CASTLE_NATHRIA = SEASON_4_RAID
CASTLE_NATHRIA_ENDBOSSES = SEASON_4_RAID_ENDBOSSES

SANCTUM_OF_DOMINATION = SEASON_4_RAID
SANCTUM_OF_DOMINATION_ENDBOSSES = SEASON_4_RAID_ENDBOSSES

SEPULCHER_OF_THE_FIRST_ONES = SEASON_4_RAID
SEPULCHER_OF_THE_FIRST_ONES_ENDBOSSES = SEASON_4_RAID_ENDBOSSES

PVP_HONOR = [
    229,
    236,
    242,
    249,
    255,
    262,
    268,
]
PVP_CONQUEST = [
    275,
    278,
    281,
    285,
    288,
    291,
    294,
    298,
    301,
]
PVP = PVP_HONOR + PVP_CONQUEST


RARE_MOB = {
    155: [
        155,
        164,
    ]
}
