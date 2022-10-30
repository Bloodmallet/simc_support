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
