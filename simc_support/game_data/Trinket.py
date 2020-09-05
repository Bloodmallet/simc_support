import json
import pkg_resources
import typing

from simc_support.game_data.ItemLevel import CASTLE_NATHRIA
from simc_support.game_data.Language import Translation
from simc_support.game_data.Language import EmptyTranslation
from simc_support.game_data.Role import Role
from simc_support.game_data.Source import Source
from simc_support.game_data.Stat import Stat
from simc_support.game_data.WowSpec import WowSpec


class Trinket(object):
    def __init__(
        self,
        *,
        item_id: str,
        itemlevels: typing.List[int],
        role: Role,
        stats: typing.Union[typing.List[Stat], typing.Tuple[Stat]],
        translations: Translation,
        source: str = None,
        on_use: bool = False,
        bonus_ids: typing.Union[typing.List[int], typing.Tuple[int]] = (),
    ):
        """Creates a Trinket instance

        Args:
            item_id (str): Item ID
            itemlevels (typing.List[int]): item is available at all these itemlevels
            stats (typing.Union[typing.List[Stat], typing.Tuple[Stat]]): primary stats
            translations (Translation): name of the item in all languages
            legendary (bool, optional): Flag to determine legendaries. Defaults to False.
            source (str, optional): Drop source. Defaults to None.
            on_use (bool, optional): Is the trinket on use? Defaults to False.
        """
        super(Trinket, self).__init__()
        self.translations = translations
        self.name: str = self.translations.US
        self.item_id: str = str(item_id)
        self.itemlevels: list = sorted(itemlevels)
        self.min_itemlevel: int = self.itemlevels[0]
        self.max_itemlevel: int = self.itemlevels[-1]

        if isinstance(stats, list) or isinstance(stats, tuple):
            for element in stats:
                if element not in Stat:
                    raise TypeError("One or more provided stats are unknown.")
        else:
            raise TypeError(f"stats: Expected list or tuple. Got {type(stats)}")
        if isinstance(stats, list) or isinstance(stats, tuple):
            self.stats = tuple(stats)

        self.role = role

        if not isinstance(source, Source):
            raise ValueError(f"Unknown source '{source}'.")
        self.source = source

        self.on_use: bool = bool(on_use)

        if isinstance(bonus_ids, list) or isinstance(bonus_ids, tuple):
            for bonus in bonus_ids:
                if not isinstance(bonus, int):
                    raise TypeError("One or more provided bonus IDs was not an INT.")
        else:
            raise TypeError(f"bonus_id: Expected list or tuple. Got {type(bonus_ids)}")
        if isinstance(bonus_ids, list) or isinstance(bonus_ids, tuple):
            self.bonus_ids = tuple(bonus_ids)


def _load_trinkets() -> typing.List[Trinket]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "trinkets.json"))
    ) as f:
        loaded_trinkets = json.load(f)

    def _get_translations(item: dict) -> Translation:
        keys = [
            "en_US",
            "ko_KR",
            "fr_FR",
            "de_DE",
            "zh_CN",
            "es_ES",
            "ru_RU",
            "it_IT",
            "pt_PT",
        ]
        d = {}
        for key in keys:
            d[key.split("_")[1]] = item[f"name_{key}"]

        d["BR"] = d["PT"]
        d.pop("PT")

        return Translation(translations=d)

    def _get_stats(item: dict) -> typing.List[Stat]:
        """Get primary stats from items stat_type information.
        TODO: Can be extended using ItemEffect.id_specialization.
        TODO: what to do with trinkets without primary stats?

        Args:
            item (dict): [description]

        Returns:
            typing.List[Stat]: [description]
        """
        stats = []
        translation = {3: Stat.AGILITY, 4: Stat.STRENGTH, 5: Stat.INTELLECT}
        for i in range(1, 11):
            if item[f"stat_type_{i}"] in translation:
                stats.append(translation[item[f"stat_type_{i}"]])
            elif item[f"stat_type_{i}"] == 71:
                stats.append(Stat.AGILITY)
                stats.append(Stat.STRENGTH)
                stats.append(Stat.INTELLECT)
            elif item[f"stat_type_{i}"] == 72:
                stats.append(Stat.AGILITY)
                stats.append(Stat.STRENGTH)
            elif item[f"stat_type_{i}"] == 73:
                stats.append(Stat.AGILITY)
                stats.append(Stat.INTELLECT)
            elif item[f"stat_type_{i}"] == 74:
                stats.append(Stat.STRENGTH)
                stats.append(Stat.INTELLECT)
        return stats

    trinkets = []
    for trinket in loaded_trinkets:
        trinkets.append(
            Trinket(
                item_id=trinket["id"],
                itemlevels=[trinket["ilevel"]],
                role=None,  # TODO
                stats=_get_stats(trinket),
                translations=_get_translations(trinket),
                source=Source.UNKNOWN,
                on_use=trinket["on_use"],
            )
        )
    return trinkets


TRINKETS: typing.List[Trinket] = _load_trinkets()


def get_trinkets_for_spec(wow_spec: WowSpec) -> tuple:
    """New function to return all available trinkets for a spec
    TODO: see https://trinitycore.atlassian.net/wiki/spaces/tc/pages/2130045/item+sparse#item_sparse-AllowableClass

    Arguments:
      wow_spec {WowSpec} -- instance of a WowSpec

    Returns:
      tuple[Trinket] -- Tuple of all Trinkets
    """

    trinkets: typing.List[Trinket] = []
    for trinket in TRINKETS:
        if wow_spec.role in trinket.role:
            trinkets.append(trinket)
        elif wow_spec.stat in trinket.stat:
            trinkets.append(trinket)
    return tuple(trinkets)


def get_versatility_trinket(stat: Stat) -> Trinket:
    """Returns a vers stat stick with the given Stat.

    Returns:
        Trinket -- Versatility Stat stick
    """
    empty_translation = EmptyTranslation()
    empty_translation.US = "Versatility Stat Stick"
    if stat == Stat.AGILITY:
        # "Stat Stick (Versatility)", "142506,bonus_id=607"
        return Trinket(
            item_id=142506,
            bonus_ids=[
                607,
            ],
            itemlevels=[CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.AGILITY,
            ],
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
        )
    elif stat == Stat.INTELLECT:
        # "Stat Stick (Versatility)", "142507,bonus_id=607"
        return Trinket(
            item_id=142507,
            bonus_ids=[
                607,
            ],
            itemlevels=[CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.INTELLECT,
            ],
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
        )
    elif stat == Stat.STRENGTH:
        # "Stat Stick (Versatility)", "142508,bonus_id=607"
        return Trinket(
            item_id=142508,
            bonus_ids=[
                607,
            ],
            itemlevels=[CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.STRENGTH,
            ],
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
        )
