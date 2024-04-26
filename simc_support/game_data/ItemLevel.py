import typing
from simc_support.game_data.Source import Source
from simc_support.game_data.Season import Season
from simc_support.game_data.Instance import InstanceType, RaidTier


def _prof_range(start: int) -> typing.List[int]:
    return list(range(start, start + 11, 2))


_s2_explorer = [376, 379, 382, 385, 389, 392, 395, 398]
_s2_adventurer = [389, 392, 395, 398, 402, 405, 408, 411]
_s2_veteran = [402, 405, 408, 411, 415, 418, 421, 424]
_s2_champion = [415, 418, 421, 424, 428, 431, 434, 437]
_s2_hero = [428, 431, 434, 437, 441]
_s2_mythic = [441, 444, 447, 450]

_s3_explorer: typing.List[int] = []
_s3_adventurer = [428, 431, 434, 437, 441, 444, 447, 450]
_s3_veteran = [441, 444, 447, 450, 454, 457, 460, 463]
_s3_champion = [454, 457, 460, 463, 467, 470, 473, 476]
_s3_hero = [467, 470, 473, 476, 480, 483]
_s3_mythic = [480, 483, 486, 489]

_s4_explorer = [454, 457, 460, 463, 467, 470, 473, 476]
_s4_adventurer = [467, 470, 473, 476, 480, 483, 486, 489]
_s4_veteran = [480, 483, 486, 489, 493, 496, 499, 502]
_s4_champion = [493, 496, 499, 502, 506, 509, 512, 515]
_s4_hero = [506, 509, 512, 515, 519, 522]
_s4_mythic = [519, 522, 525, 528]  # guessed 525 and 528


def _season_2_upgrade_range(upgrade_level: int) -> typing.List[int]:
    if upgrade_level < 1:
        raise ValueError("Upgrade level start at 1.")

    options = (_s2_veteran, _s2_champion, _s2_hero, _s2_mythic[:-1])
    ilevels: typing.List[int] = []
    for option in options:
        ilevels = ilevels + option[upgrade_level - 1 :]

    if upgrade_level == len(_s2_mythic):
        ilevels.append(_s2_mythic[-1])

    # make ilevels unique
    ilevels = list(set(ilevels))

    # ensure ilevels are ordered
    ilevels = sorted(ilevels)

    return ilevels


def _season_3_upgrade_range(upgrade_level: int) -> typing.List[int]:
    if upgrade_level < 1:
        raise ValueError("Upgrade level start at 1.")

    options = (_s3_veteran, _s3_champion, _s3_hero, _s3_mythic)
    ilevels: typing.List[int] = []
    for option in options:
        ilevels = ilevels + option[upgrade_level - 1 :]

    # if upgrade_level == len(_s3_mythic):
    #     ilevels.append(_s3_mythic[-1])

    # make ilevels unique
    ilevels = list(set(ilevels))

    # ensure ilevels are ordered
    ilevels = sorted(ilevels)

    return ilevels


def _season_4_upgrade_range(upgrade_level: int) -> typing.List[int]:
    if upgrade_level < 1:
        raise ValueError("Upgrade level start at 1.")

    options = (_s4_veteran, _s4_champion, _s4_hero, _s4_mythic)
    ilevels: typing.List[int] = []
    for option in options:
        ilevels = ilevels + option[upgrade_level - 1 :]

    # if upgrade_level == len(_s3_mythic):
    #     ilevels.append(_s3_mythic[-1])

    # make ilevels unique
    ilevels = list(set(ilevels))

    # ensure ilevels are ordered
    ilevels = sorted(ilevels)

    return ilevels


ITEM_LEVELS = {
    Source.CALLING: {
        Season.SEASON_1: [],
        Season.SEASON_2: _s2_veteran,
        Season.SEASON_3: _s3_adventurer,
        Season.SEASON_4: _s4_adventurer,
    },
    Source.MISSION: {
        Season.SEASON_1: [],
        Season.SEASON_2: [],
        Season.SEASON_3: [-1],
        Season.SEASON_4: [-1],
    },
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
        Season.SEASON_3: list(
            {
                ilevel
                for ilevel in _s3_veteran + _s3_champion + _s3_hero + _s3_mythic[:-1]
            }
        ),
        Season.SEASON_4: list(
            {
                ilevel
                for ilevel in _s4_veteran + _s4_champion + _s4_hero + _s4_mythic[:-2]
            }
        ),
    },
    Source.PVP: {
        Season.SEASON_1: [408, 424],
        Season.SEASON_2: [424],
        Season.SEASON_3: [-1],
        Season.SEASON_4: [-1],
    },  # split into aspirant and gladiator
    Source.LOW_PVP: {
        Season.SEASON_1: [408],
        Season.SEASON_2: [437],
        Season.SEASON_3: [-1],
        Season.SEASON_4: [-1],
    },
    Source.HIGH_PVP: {
        Season.SEASON_1: [382, 385, 389, 392, 395, 398, 402, 405, 408, 424],
        Season.SEASON_2: [434, 450],
        Season.SEASON_3: [476],
        Season.SEASON_4: [515],
    },
    Source.RARE_MOB: {  # super rares that scale up
        Season.SEASON_1: [379, 382, 385, 389, 392],
        Season.SEASON_2: [],
        Season.SEASON_3: [-1],
        Season.SEASON_4: [-1],
    },
    Source.WORLD_BOSS: {
        Season.SEASON_1: [395],
        Season.SEASON_2: [415],
        Season.SEASON_3: [-1],
        Season.SEASON_4: [-1],
    },
    Source.WORLD_DROP: {
        Season.SEASON_1: [],
        Season.SEASON_2: [],
        Season.SEASON_3: [],
        Season.SEASON_4: [],
    },
    Source.WORLD_QUEST: {
        Season.SEASON_1: [372, 376, 379, 382, 385, 389],
        Season.SEASON_2: _s2_adventurer,
        Season.SEASON_3: [-1],
        Season.SEASON_4: _s4_veteran,
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
            {
                ilevel
                for ilevel in _s2_veteran + _s2_champion + _s2_hero + _s2_mythic[:-1]
            }
        ),
        Season.SEASON_3: list(
            {ilevel for ilevel in _s3_veteran + _s3_champion + _s3_hero + _s3_mythic}
        ),
        Season.SEASON_4: list(
            {ilevel for ilevel in _s4_veteran + _s4_champion + _s4_hero + _s4_mythic}
        ),
    },
    Source.MEGA_DUNGEON: {
        Season.SEASON_1: [],
        Season.SEASON_2: _s2_hero[-2:],
        Season.SEASON_3: [-1],
        Season.SEASON_4: _s4_champion,
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
                list(set([*_s2_champion[2 - 1 :], *_s2_hero[2 - 1 :], 444, 457]))
            ),
        },
        Season.SEASON_3: {
            RaidTier.LOW: _season_3_upgrade_range(1),
            RaidTier.MID: _season_3_upgrade_range(2),
            RaidTier.HIGH: _season_3_upgrade_range(3),
            RaidTier.HIGHER: _season_3_upgrade_range(4),
            RaidTier.VERY_RARE: sorted(
                list(
                    set(
                        [
                            *_s3_champion[2 - 1 :],
                            *_s3_hero[2 - 1 :],
                            *_s3_mythic[2 - 1 :],
                            496,
                        ]
                    )
                )
            ),
        },
        Season.SEASON_4: {
            RaidTier.LOW: _season_4_upgrade_range(1),
            RaidTier.MID: _season_4_upgrade_range(2),
            RaidTier.HIGH: _season_4_upgrade_range(3),
            RaidTier.HIGHER: _season_4_upgrade_range(4),
            RaidTier.VERY_RARE: sorted(
                list(
                    set(
                        [
                            *_s4_champion[2 - 1 :],
                            *_s4_hero[2 - 1 :],
                            *_s4_mythic[2 - 1 :],
                            532,
                            535,
                        ]
                    )
                )
            ),
        },
    },
    Source.TIMEWALKING: {
        Season.SEASON_1: {
            InstanceType.DUNGEON: [385],
            InstanceType.RAID: [385],
        },
        Season.SEASON_2: {
            InstanceType.DUNGEON: [385],
            InstanceType.RAID: _s2_champion,
        },
        Season.SEASON_3: {
            InstanceType.DUNGEON: _s3_adventurer,
            InstanceType.RAID: _s3_hero,
        },
        Season.SEASON_4: {
            InstanceType.DUNGEON: _s4_adventurer,
            InstanceType.RAID: _s4_hero,
        },
    },
}
"""Source > Season [ > InstanceType | > RaidTier ]
"""
