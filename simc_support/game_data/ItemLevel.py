import typing
from simc_support.game_data.Source import Source
from simc_support.game_data.Season import Season
from simc_support.game_data.Instance import InstanceType, RaidTier


def _prof_range(start: int) -> typing.List[int]:
    return list(range(start, start + 11, 2))


_df_s2_explorer = [376, 379, 382, 385, 389, 392, 395, 398]
_df_s2_adventurer = [389, 392, 395, 398, 402, 405, 408, 411]
_df_s2_veteran = [402, 405, 408, 411, 415, 418, 421, 424]
_df_s2_champion = [415, 418, 421, 424, 428, 431, 434, 437]
_df_s2_hero = [428, 431, 434, 437, 441]
_df_s2_mythic = [441, 444, 447, 450]

_df_s3_explorer: typing.List[int] = []
_df_s3_adventurer = [428, 431, 434, 437, 441, 444, 447, 450]
_df_s3_veteran = [441, 444, 447, 450, 454, 457, 460, 463]
_df_s3_champion = [454, 457, 460, 463, 467, 470, 473, 476]
_df_s3_hero = [467, 470, 473, 476, 480, 483]
_df_s3_mythic = [480, 483, 486, 489]

_df_s4_explorer = [454, 457, 460, 463, 467, 470, 473, 476]
_df_s4_adventurer = [467, 470, 473, 476, 480, 483, 486, 489]
_df_s4_veteran = [480, 483, 486, 489, 493, 496, 499, 502]
_df_s4_champion = [493, 496, 499, 502, 506, 509, 512, 515]
_df_s4_hero = [506, 509, 512, 515, 519, 522]
_df_s4_mythic = [519, 522, 525, 528]  # guessed 525 and 528


_tww1_explorer = [558, 561, 564, 567, 571, 574, 577, 580]
_tww1_adventurer = [571, 574, 577, 580, 584, 587, 590, 593]
_tww1_veteran = [584, 587, 590, 593, 597, 600, 603, 606]
_tww1_champion = [597, 600, 603, 606, 610, 613, 616, 619]
_tww1_hero = [610, 613, 616, 619, 623, 626]
_tww1_mythic = [623, 626, 629, 632, 636, 639]


def _df_season_2_upgrade_range(upgrade_level: int) -> typing.List[int]:
    if upgrade_level < 1:
        raise ValueError("Upgrade level start at 1.")

    options = (_df_s2_veteran, _df_s2_champion, _df_s2_hero, _df_s2_mythic[:-1])
    ilevels: typing.List[int] = []
    for option in options:
        ilevels = ilevels + option[upgrade_level - 1 :]

    if upgrade_level == len(_df_s2_mythic):
        ilevels.append(_df_s2_mythic[-1])

    # make ilevels unique
    ilevels = list(set(ilevels))

    # ensure ilevels are ordered
    ilevels = sorted(ilevels)

    return ilevels


def _upgrade_range(
    options: typing.List[typing.List[int]], upgrade_level: int
) -> typing.List[int]:
    if upgrade_level < 1:
        raise ValueError("Upgrade level start at 1.")

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


def _df_season_3_upgrade_range(upgrade_level: int) -> typing.List[int]:
    options = [_df_s3_veteran, _df_s3_champion, _df_s3_hero, _df_s3_mythic]
    return _upgrade_range(options, upgrade_level)


def _df_season_4_upgrade_range(upgrade_level: int) -> typing.List[int]:
    options = [_df_s4_veteran, _df_s4_champion, _df_s4_hero, _df_s4_mythic]
    return _upgrade_range(options, upgrade_level)


def _tww_season_1_upgrade_range(upgrade_level: int) -> typing.List[int]:
    options = [_tww1_veteran, _tww1_champion, _tww1_hero, _tww1_mythic]
    return _upgrade_range(options, upgrade_level)


def _combine_unify(*itemlevels: typing.List[int]) -> typing.List[int]:
    combined_list = []
    for levels in itemlevels:
        combined_list += levels

    combined_list = list(set(combined_list))
    combined_list = sorted(combined_list)
    return combined_list


ITEM_LEVELS = {
    Source.CALLING: {
        Season.DF_SEASON_1: [],
        Season.DF_SEASON_2: _df_s2_veteran,
        Season.DF_SEASON_3: _df_s3_adventurer,
        Season.DF_SEASON_4: _df_s4_champion,
        Season.TWW_SEASON_1: _combine_unify(
            _tww1_explorer,
            _tww1_adventurer,
            _tww1_veteran,
            _tww1_champion,
            _tww1_hero,
        ),
    },
    Source.MISSION: {
        Season.DF_SEASON_1: [],
        Season.DF_SEASON_2: [],
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: [-1],
        Season.TWW_SEASON_1: _combine_unify(
            _tww1_explorer,
            _tww1_adventurer,
            _tww1_veteran,
            _tww1_champion,
            _tww1_hero,
        ),
    },
    Source.PROFESSION: {
        Season.DF_SEASON_1: [
            *_prof_range(306),  # base
            *_prof_range(333),  # Titan Training Matric I
            *_prof_range(346),  # Titan Training Matric II
            *_prof_range(359),  # Titan Training Matric III
            *_prof_range(372),  # Titan Training Matric IV
            *_prof_range(382),  # Epic
            *_prof_range(395),  # Primal Infusion
            *_prof_range(408),  # Concentrated Primal Infusion
        ],
        Season.DF_SEASON_2: list(
            {
                ilevel
                for ilevel in [424, 428, 431, 434, 437]  # Wyrm's
                + [434, 437, 441, 444, 447]  # Aspect's
            }
        ),
        Season.DF_SEASON_3: list(
            {
                ilevel
                for ilevel in _df_s3_veteran
                + _df_s3_champion
                + _df_s3_hero
                + _df_s3_mythic[:-1]
            }
        ),
        Season.DF_SEASON_4: list(
            {
                ilevel
                for ilevel in _df_s4_veteran
                + _df_s4_champion
                + _df_s4_hero
                + _df_s4_mythic[:-2]
            }
        ),
        Season.TWW_SEASON_1: list(
            {
                ilevel
                for ilevel in _tww1_veteran
                + _tww1_champion
                + _tww1_hero
                + _tww1_mythic[:-2]
            }
        ),
    },
    Source.PVP: {
        Season.DF_SEASON_1: [408, 424],
        Season.DF_SEASON_2: [424],
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: [-1],
        Season.TWW_SEASON_1: [-1],
    },  # split into aspirant and gladiator
    Source.LOW_PVP: {
        Season.DF_SEASON_1: [408],
        Season.DF_SEASON_2: [437],
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: [-1],
        Season.TWW_SEASON_1: [-1],
    },
    Source.HIGH_PVP: {
        Season.DF_SEASON_1: [382, 385, 389, 392, 395, 398, 402, 405, 408, 424],
        Season.DF_SEASON_2: [434, 450],
        Season.DF_SEASON_3: [476],
        Season.DF_SEASON_4: [515],
        Season.TWW_SEASON_1: _tww1_champion,
    },
    Source.RARE_MOB: {  # super rares that scale up
        Season.DF_SEASON_1: [379, 382, 385, 389, 392],
        Season.DF_SEASON_2: [],
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: [-1],
        Season.TWW_SEASON_1: _combine_unify(
            _tww1_explorer,
            _tww1_adventurer,
            _tww1_veteran,
            _tww1_champion,
            _tww1_hero,
        ),
    },
    Source.WORLD_BOSS: {
        Season.DF_SEASON_1: [395],
        Season.DF_SEASON_2: [415],
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: [-1],
        Season.TWW_SEASON_1: [-1],
    },
    Source.WORLD_DROP: {
        Season.DF_SEASON_1: [],
        Season.DF_SEASON_2: [],
        Season.DF_SEASON_3: [],
        Season.DF_SEASON_4: [],
        Season.TWW_SEASON_1: [-1],
    },
    Source.WORLD_QUEST: {
        Season.DF_SEASON_1: [372, 376, 379, 382, 385, 389],
        Season.DF_SEASON_2: _df_s2_adventurer,
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: _df_s4_veteran,
        Season.TWW_SEASON_1: _combine_unify(
            _tww1_explorer,
            _tww1_adventurer,
            _tww1_veteran,
            _tww1_champion,
            _tww1_hero,
        ),
    },
    Source.DUNGEON: {
        Season.DF_SEASON_1: [
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
        Season.DF_SEASON_2: list(
            {
                ilevel
                for ilevel in _df_s2_veteran
                + _df_s2_champion
                + _df_s2_hero
                + _df_s2_mythic[:-1]
            }
        ),
        Season.DF_SEASON_3: list(
            {
                ilevel
                for ilevel in _df_s3_veteran
                + _df_s3_champion
                + _df_s3_hero
                + _df_s3_mythic
            }
        ),
        Season.DF_SEASON_4: list(
            {
                ilevel
                for ilevel in _df_s4_veteran
                + _df_s4_champion
                + _df_s4_hero
                + _df_s4_mythic
            }
        ),
        Season.TWW_SEASON_1: list(
            {
                ilevel
                for ilevel in _tww1_veteran + _tww1_champion + _tww1_hero + _tww1_mythic
            }
        ),
    },
    Source.MEGA_DUNGEON: {
        Season.DF_SEASON_1: [],
        Season.DF_SEASON_2: _df_s2_hero[-2:],
        Season.DF_SEASON_3: [-1],
        Season.DF_SEASON_4: _df_s4_champion,
        Season.TWW_SEASON_1: [-1],
    },
    Source.RAID: {
        Season.DF_SEASON_1: {
            RaidTier.LOW: [376, 389, 402, 415],
            RaidTier.MID: [382, 395, 408, 421],
            RaidTier.HIGH: [385, 398, 411, 424],
        },
        Season.DF_SEASON_2: {
            RaidTier.LOW: _df_season_2_upgrade_range(1),
            RaidTier.MID: _df_season_2_upgrade_range(2),
            RaidTier.HIGH: _df_season_2_upgrade_range(3),
            RaidTier.HIGHER: _df_season_2_upgrade_range(4),
            RaidTier.VERY_RARE: sorted(
                list(set([*_df_s2_champion[2 - 1 :], *_df_s2_hero[2 - 1 :], 444, 457]))
            ),
        },
        Season.DF_SEASON_3: {
            RaidTier.LOW: _df_season_3_upgrade_range(1),
            RaidTier.MID: _df_season_3_upgrade_range(2),
            RaidTier.HIGH: _df_season_3_upgrade_range(3),
            RaidTier.HIGHER: _df_season_3_upgrade_range(4),
            RaidTier.VERY_RARE: sorted(
                list(
                    set(
                        [
                            *_df_s3_champion[2 - 1 :],
                            *_df_s3_hero[2 - 1 :],
                            *_df_s3_mythic[2 - 1 :],
                            496,
                        ]
                    )
                )
            ),
        },
        Season.DF_SEASON_4: {
            RaidTier.LOW: _df_season_4_upgrade_range(1),
            RaidTier.MID: _df_season_4_upgrade_range(2),
            RaidTier.HIGH: _df_season_4_upgrade_range(3),
            RaidTier.HIGHER: _df_season_4_upgrade_range(4),
            RaidTier.VERY_RARE: sorted(
                list(
                    set(
                        [
                            *_df_s4_champion[2 - 1 :],
                            *_df_s4_hero[2 - 1 :],
                            *_df_s4_mythic[2 - 1 :],
                            532,
                            535,
                        ]
                    )
                )
            ),
        },
        Season.TWW_SEASON_1: {
            RaidTier.LOW: _tww_season_1_upgrade_range(1),
            RaidTier.MID: _tww_season_1_upgrade_range(2),
            RaidTier.HIGH: _tww_season_1_upgrade_range(3),
            RaidTier.HIGHER: _tww_season_1_upgrade_range(4),
            RaidTier.VERY_RARE: [-1],
        },
    },
    Source.TIMEWALKING: {
        Season.DF_SEASON_1: {
            InstanceType.DUNGEON: [385],
            InstanceType.RAID: [385],
        },
        Season.DF_SEASON_2: {
            InstanceType.DUNGEON: [385],
            InstanceType.RAID: _df_s2_champion,
        },
        Season.DF_SEASON_3: {
            InstanceType.DUNGEON: _df_s3_adventurer,
            InstanceType.RAID: _df_s3_hero,
        },
        Season.DF_SEASON_4: {
            InstanceType.DUNGEON: _df_s4_adventurer,
            InstanceType.RAID: _df_s4_hero,
        },
        Season.TWW_SEASON_1: {
            InstanceType.DUNGEON: [-1],
            InstanceType.RAID: [-1],
        },
    },
    Source.DELVE: {
        Season.TWW_SEASON_1: _combine_unify(
            _tww1_explorer,
            _tww1_adventurer,
            _tww1_veteran,
            _tww1_champion,
            _tww1_hero,
        ),
    },
}
"""Source > Season [ > InstanceType | > RaidTier ]
"""
