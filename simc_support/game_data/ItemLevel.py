import typing
from simc_support.game_data.Source import Source
from simc_support.game_data.Season import Season
from simc_support.game_data.Instance import RaidTier


def _prof_range(start: int) -> typing.List[int]:
    return list(range(start, start + 11, 2))


_explorer = [376, 379, 382, 385, 389, 392, 395, 398]
_adventurer = [389, 392, 395, 398, 402, 405, 408, 411]
_veteran = [402, 405, 408, 411, 415, 418, 421, 424]
_champion = [415, 418, 421, 424, 428, 431, 434, 437]
_hero = [428, 431, 434, 437, 441]
_mythic = [441, 444, 447, 450]


def _season_2_upgrade_range(upgrade_level: int) -> typing.List[int]:
    if upgrade_level < 1:
        raise ValueError("Upgrade level start at 1.")

    options = (_veteran, _champion, _hero)
    ilevels: typing.List[int] = []
    for option in options:
        ilevels = ilevels + option[upgrade_level - 1 :]

    # add mythic
    ilevels.append(_mythic[upgrade_level - 1])

    # make ilevels unique
    ilevels = list(set(ilevels))

    # ensure ilevels are ordered
    ilevels = sorted(ilevels)

    return ilevels


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
        Season.SEASON_2: [424],
    },  # split into aspirant and gladiator
    Source.LOW_PVP: {Season.SEASON_1: [408], Season.SEASON_2: [437]},
    Source.HIGH_PVP: {
        Season.SEASON_1: [382, 385, 389, 392, 395, 398, 402, 405, 408, 424],
        Season.SEASON_2: [434, 450],
    },
    Source.RARE_MOB: {  # super rares that scale up
        Season.SEASON_1: [379, 382, 385, 389, 392],
        Season.SEASON_2: [],
    },
    Source.WORLD_BOSS: {Season.SEASON_1: [395], Season.SEASON_2: [415]},
    Source.WORLD_DROP: {Season.SEASON_1: [], Season.SEASON_2: []},
    Source.WORLD_QUEST: {
        Season.SEASON_1: [372, 376, 379, 382, 385, 389],
        Season.SEASON_2: [*_adventurer],
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
            {ilevel for ilevel in _veteran + _champion + _hero + _mythic[:-1]}
        ),
    },
    Source.RAID: {
        Season.SEASON_1: {
            RaidTier.LOW: [376, 389, 402, 415],
            RaidTier.MID: [382, 395, 408, 421],
            RaidTier.HIGH: [385, 398, 411, 424],
        },
        Season.SEASON_2: {
            RaidTier.LOW: _season_2_upgrade_range(1),
            RaidTier.MID: _season_2_upgrade_range(2),
            RaidTier.HIGH: _season_2_upgrade_range(3),
            RaidTier.HIGHER: _season_2_upgrade_range(4),
            RaidTier.VERY_RARE: sorted(
                list(set([*_champion[2 - 1 :], *_hero[2 - 1 :], 444, 457]))
            ),
        },
    },
    Source.TIMEWALKING: {
        Season.SEASON_1: [],
        Season.SEASON_2: _champion,
    },
}
"""Source > Season
"""
