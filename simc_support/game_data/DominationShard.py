from enum import Enum
import json
import pkg_resources
import typing

from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data.Language import _get_translations
from simc_support.game_data.Language import Translation


class ShardType(Enum):
    BLOOD = "blood"
    FROST = "frost"
    UNHOLY = "unholy"

    @staticmethod
    def get_shard_type(school: int) -> "ShardType":
        mapping = {
            16: ShardType.FROST,
            32: ShardType.UNHOLY,
            64: ShardType.BLOOD,
        }
        return mapping[school]


class DominationShard(SimcObject):
    def __init__(
        self,
        *args,
        gem_id: int,
        spell_id: int,
        school: int,
        translations: Translation,
        **kwargs,
    ):
        """Domination Socket of the second Raid of Shadowlands

        Args:
            gem_id (int): id of the gem
            school (int): int of the spell-school
            translations (Translation): name of the item in all languages
        """
        super().__init__(translations.US, *args, **kwargs)
        self.translations = translations
        self.name: str = self.translations.US
        self.gem_id: int = int(gem_id)
        self.spell_id: int = int(spell_id)
        self.school: int = int(school)
        self.school_type = ShardType.get_shard_type(self.school)


def _load_domination_shards() -> typing.List[DominationShard]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "domination_shards.json"))
    ) as f:
        loaded_domination_shards = json.load(f)

    domination_shards = []
    for shard in loaded_domination_shards:
        domination_shards.append(
            DominationShard(
                gem_id=shard["id"],
                spell_id=shard["id_property_1"],
                school=shard["school"],
                translations=_get_translations(shard),
            )
        )
    return domination_shards


DOMINATION_SHARDS: typing.List[DominationShard] = _load_domination_shards()
