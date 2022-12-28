import typing
from simc_support.game_data.Source import Source
from simc_support.game_data.Season import Season
from simc_support.game_data.Instance import RaidTier


def _prof_range(start: int) -> typing.List[int]:
    return list(range(start, start + 11, 2))


ITEM_LEVELS = {
    Source.CALLING: {Season.SEASON_1: []},
    Source.MISSION: {Season.SEASON_1: []},
    Source.PROFESSION: {
        Season.SEASON_1: [
            *_prof_range(306),  # base
            *_prof_range(333),  # Titan Training Matric I
            *_prof_range(346),  # Titan Training Matric II
            *_prof_range(359),  # Titan Training Matric III
            *_prof_range(372),  # Titan Training Matric IV
            *_prof_range(382),  # Epic
            *_prof_range(395),  # Primal Infusion
            *_prof_range(408),  # Concentrated Primal Infusion
        ]
    },
    Source.PVP: {Season.SEASON_1: [408, 424]},  # split into aspirant and gladiator
    Source.LOW_PVP: {Season.SEASON_1: [408]},
    Source.HIGH_PVP: {
        Season.SEASON_1: [382, 385, 389, 392, 395, 398, 402, 405, 408, 424]
    },
    Source.RARE_MOB: {  # super rares that scale up
        Season.SEASON_1: [379, 382, 385, 389, 392]
    },
    Source.WORLD_BOSS: {Season.SEASON_1: [395]},
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
"""Source > Season
"""
