import typing
from simc_support.game_data.Source import Source
from simc_support.game_data.Season import Season
from simc_support.game_data.Instance import RaidTier


def _prof_range(start: int) -> typing.List[int]:
    return list(range(start, start + 11, 2))


_explorer = [376, 379, 382, 385, 389, 392, 395, 398]
_adventurer = [389, 392, 395, 398, 402405, 408, 411]
_veteran = [402, 405, 408, 411, 415, 418, 421, 424]
_champion = [415, 418, 421, 424, 428, 431, 434, 437]
_hero = [428, 431, 434, 437, 441]
_mythic = [441, 444, 447, 450]


def _season_2_upgrade_range(start: int) -> typing.List[int]:
    options = (_explorer, _adventurer, _veteran, _champion, _hero, _mythic)
    for option in options:
        if start in option[:4]:
            return option[option.index(start) :]
    return []


ITEM_LEVELS = {
    Source.CALLING: {Season.SEASON_1: [], Season.SEASON_2: []},
    Source.MISSION: {Season.SEASON_1: [], Season.SEASON_2: []},
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
        ],
        Season.SEASON_2: list(
            {
                ilevel
                for ilevel in [424, 428, 431, 434, 437]  # Wyrm's
                + [434, 437, 441, 444, 447]  # Aspect's
            }
        ),
    },
    Source.PVP: {
        Season.SEASON_1: [408, 424],
        Season.SEASON_2: [],
    },  # split into aspirant and gladiator
    Source.LOW_PVP: {Season.SEASON_1: [408], Season.SEASON_2: []},
    Source.HIGH_PVP: {
        Season.SEASON_1: [382, 385, 389, 392, 395, 398, 402, 405, 408, 424],
        Season.SEASON_2: [],
    },
    Source.RARE_MOB: {  # super rares that scale up
        Season.SEASON_1: [379, 382, 385, 389, 392],
        Season.SEASON_2: [],
    },
    Source.WORLD_BOSS: {Season.SEASON_1: [395], Season.SEASON_2: [415]},
    Source.WORLD_DROP: {Season.SEASON_1: [], Season.SEASON_2: []},
    Source.WORLD_QUEST: {
        Season.SEASON_1: [372, 376, 379, 382, 385, 389],
        Season.SEASON_2: [],
    },
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
        ],
        Season.SEASON_2: list(
            {ilevel for ilevel in _veteran + _champion + _hero + _mythic}
        ),
    },
    Source.RAID: {
        Season.SEASON_1: {
            RaidTier.LOW: [376, 389, 402, 415],
            RaidTier.MID: [382, 395, 408, 421],
            RaidTier.HIGH: [385, 398, 411, 424],
        },
        Season.SEASON_2: {
            RaidTier.LOW: list(
                {ilevel for ilevel in _veteran + _champion + _hero + _mythic}
            )
        },
    },
}
"""Source > Season
"""
