import enum
from simc_support.game_data.Instance import Instance
import typing


class Season(enum.Enum):
    SEASON_1 = 1
    SEASON_2 = 2
    SEASON_3 = 3

    @staticmethod
    def get_seasons_from_instance(
        instance: typing.Optional[Instance],
    ) -> typing.List["Season"]:
        seasons: typing.List[Season] = []

        if instance is None:
            return seasons

        s1_instances = (
            Instance.ALGETHAR_ACADEMY,
            Instance.COURT_OF_STARS,
            Instance.HALLS_OF_VALOR,
            Instance.RUBY_LIFE_POOLS,
            Instance.SHADOWMOON_BURIAL_GROUNDS,
            Instance.TEMPLE_OF_THE_JADE_SERPENT,
            Instance.THE_AZURE_VAULT,
            Instance.THE_NOKHUD_OFFENSIVE,
            Instance.VAULT_OF_THE_INCARNATES,
        )

        if instance in s1_instances:
            seasons.append(Season.SEASON_1)

        s2_instances = (
            Instance.HALLS_OF_INFUSION,
            Instance.BRACKENHIDE_HOLLOW,
            Instance.ULDAMAN_LEGACY_OF_TYR,
            Instance.NELTHARUS,
            Instance.NELTHARIONS_LAIR,
            Instance.FREEHOLD,
            Instance.THE_UNDERROT,
            Instance.VORTEX_PINNACLE,
            Instance.ABERUS_THE_SHADOWED_CRUCIBLE,
            Instance.DAWN_OF_THE_INFINITE,
        )

        if instance in s2_instances:
            seasons.append(Season.SEASON_2)

        s3_instances = (
            # Instance.DAWN_OF_THE_INFINITE_GALAKRONDS_FALL,
            # Instance.DAWN_OF_THE_INFINITE_MUROZOND_RISE,
            Instance.DAWN_OF_THE_INFINITE,
            Instance.DARKHEART_THICKET,
            Instance.BLACK_ROOCK_HOLD,
            Instance.WAYCREST_MANOR,
            Instance.ATAL_DAZAR,
            Instance.EVERBLOOM_MPLUS,
            # Instance.THRONE_OF_THE_TIDES_MPLUS,
            Instance.THRONE_OF_THE_TIDES,
            Instance.AMIRDRASSIL_THE_DREAMS_HOPE,
        )

        if instance in s3_instances:
            seasons.append(Season.SEASON_3)

        return seasons
