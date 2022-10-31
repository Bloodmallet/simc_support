import typing
from simc_support.game_data.Source import Source
from simc_support.game_data.Season import Season
from simc_support.game_data.Instance import RaidTier

# these values are used throughout the code to determine itemlevel "borders" of items
# usually used as a catch up mechanic, drops usually all items from previous content
WORLD_QUEST_ITEMLEVELS = [
    144,
    148,
    161,
    171,
    200,
    213,
]
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
SEASON_4_VALOR_UPGRADES = [
    272,
    275,
    278,
    281,
    285,
    288,
    291,
    294,
    298,
]
TAZAVESH = [226, 233]
WORLD_BOSS_CHAINS_OF_DEVASTATION = 233
WORLD_BOSS_ZERETH_MORTIS = 259

# raids
SEASON_4_RAID = [265, 278, 291, 304]
SEASON_4_RAID_ENDBOSSES = [272, 285, 298, 311]

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

"""Source > Season
"""
ITEM_LEVELS = {
    Source.CALLING: {Season.SEASON_1: []},
    Source.MISSION: {Season.SEASON_1: []},
    Source.PROFESSION: {Season.SEASON_1: []},
    Source.PVP: {Season.SEASON_1: [408, 424]},  # split into aspirant and gladiator
    Source.RARE_MOB: {Season.SEASON_1: []},
    Source.WORLD_BOSS: {Season.SEASON_1: [389]},
    Source.WORLD_DROP: {Season.SEASON_1: []},
    Source.WORLD_QUEST: {Season.SEASON_1: []},
    Source.DUNGEON: {
        Season.SEASON_1: [
            376,
            379,
            382,
            385,
            389,
            392,
            395,
            398,
            402,
            405,
            408,
            411,
            415,
            418,
            421,
        ]
    },
    Source.RAID: {
        Season.SEASON_1: {
            RaidTier.LOW: [376, 389, 402, 415],
            RaidTier.MID: [382, 395, 408, 421],
            RaidTier.HIGH: [385, 398, 411, 424],
        }
    },
}
