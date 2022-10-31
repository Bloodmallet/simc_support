import enum
from simc_support.game_data.Instance import Instance
import typing


class Season(enum.Enum):
    SEASON_1 = 1

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

        return seasons
