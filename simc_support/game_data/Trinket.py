import json
import pkg_resources
import typing

from simc_support.game_data.SimcObject import SimcObject
import simc_support.game_data.ItemLevel as ItemLevel
from simc_support.game_data.Language import _get_translations
from simc_support.game_data.Language import EmptyTranslation
from simc_support.game_data.Language import Translation
from simc_support.game_data.Role import Role
from simc_support.game_data.Source import Source
from simc_support.game_data.Stat import Stat
from simc_support.game_data.WowSpec import WowSpec


class Trinket(SimcObject):
    def __init__(
        self,
        *args,
        item_id: str,
        itemlevels: typing.List[int],
        role: typing.Optional[Role],
        stats: typing.Union[typing.List[Stat], typing.Tuple[Stat]],
        class_mask: int,
        translations: Translation,
        source: Source = None,
        on_use: bool = False,
        bonus_ids: typing.Union[typing.Tuple, typing.List[int], typing.Tuple[int]] = (),
        **kwargs,
    ):
        """Creates a Trinket instance

        Args:
            item_id (str): Item ID
            itemlevels (typing.List[int]): item is available at all these itemlevels
            role (Role):
            stats (typing.Union[typing.List[Stat], typing.Tuple[Stat]]): primary stats
            translations (Translation): name of the item in all languages
            source (str, optional): Drop source. Defaults to None.
            on_use (bool, optional): Is the trinket on use? Defaults to False.
            bonus_ids (typing.Union[typing.List[int], typing.Tuple[int]]):
        """
        super().__init__(translations.US, *args, **kwargs)
        self.translations = translations
        self.name: str = self.translations.US
        self.item_id: str = str(item_id)
        self.itemlevels: list = sorted(itemlevels)

        if isinstance(stats, list) or isinstance(stats, tuple):
            for element in stats:
                if element not in Stat:
                    raise TypeError("One or more provided stats are unknown.")
        else:
            raise TypeError(f"stats: Expected list or tuple. Got {type(stats)}")
        if isinstance(stats, list) or isinstance(stats, tuple):
            self.stats = tuple(stats)

        self.class_mask = class_mask
        self.role = role

        if not isinstance(source, Source):
            raise ValueError(f"Unknown source '{source}'.")
        self.source: Source = source

        self.on_use: bool = bool(on_use)

        if isinstance(bonus_ids, list) or isinstance(bonus_ids, tuple):
            for bonus in bonus_ids:
                if not isinstance(bonus, int):
                    raise TypeError("One or more provided bonus IDs was not an INT.")
        else:
            raise TypeError(f"bonus_id: Expected list or tuple. Got {type(bonus_ids)}")
        if isinstance(bonus_ids, list) or isinstance(bonus_ids, tuple):
            self.bonus_ids = tuple(bonus_ids)

    @property
    def min_itemlevel(self) -> int:
        return self.itemlevels[0]

    @property
    def max_itemlevel(self) -> int:
        return self.itemlevels[-1]

    def is_usable_by_class(self, class_id: int) -> bool:
        return bool(self.class_mask & 1 << (class_id - 1))

    def _stringify(self) -> str:
        return f"{self.item_id} {self.name} {self.stats} {self.source}"


def _load_trinkets() -> typing.List[Trinket]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "trinkets.json"))
    ) as f:
        loaded_trinkets = json.load(f)

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

    def _get_itemlevels(item: dict, source: Source) -> typing.List[int]:

        # add special cases here
        if item["name"] == "Spiritual Alchemy Stone":
            return [
                item.get("ilevel", 0),
                200,
            ]

        if source == Source.DUNGEON:
            return ItemLevel.DUNGEON
        if source == Source.RAID and item["id_journal_instance"] == 1190:
            return sorted(ItemLevel.CASTLE_NATHRIA + ItemLevel.CASTLE_NATHRIA_ENDBOSSES)
        if source == Source.PROFESSION:
            return [
                item["ilevel"],
            ]
        if source == Source.PVP:
            return list(
                [
                    itemlevel
                    for itemlevel in ItemLevel.PVP
                    if itemlevel >= item.get("ilevel", 0)
                ]
            )
        return [
            item["ilevel"],
        ]

    def _get_bonus_ids(item: dict) -> typing.List[int]:
        ids = []

        # Unbound Changeling
        if item["id"] == 178708:
            # crit
            ids.append(6916)
            # haste
            ids.append(6917)
            # mastery
            ids.append(6918)
            # crit haste mastery
            ids.append(6915)

        return ids

    def _get_source(item: dict) -> Source:
        instance_mapping = {
            1: Source.DUNGEON,
            2: Source.RAID,
        }
        item_mapping = {
            175884: Source.PVP,
            175921: Source.PVP,
            178298: Source.PVP,
            178334: Source.PVP,
            178386: Source.PVP,
            178447: Source.PVP,
            181333: Source.PVP,
            181335: Source.PVP,
            181816: Source.PVP,
            184052: Source.PVP,
            184053: Source.PVP,
            184054: Source.PVP,
            184055: Source.PVP,
            184056: Source.PVP,
            184057: Source.PVP,
            184058: Source.PVP,
            184059: Source.PVP,
            184060: Source.PVP,
            184807: Source.WORLD_DROP,
            182455: Source.WORLD_DROP,
            182454: Source.WORLD_DROP,
            182453: Source.WORLD_DROP,
            182452: Source.WORLD_DROP,
            182451: Source.WORLD_DROP,
            175729: Source.WORLD_DROP,
            175943: Source.PROFESSION,
            175942: Source.PROFESSION,
            175941: Source.PROFESSION,
            171323: Source.PROFESSION,
            173069: Source.PROFESSION,
            173078: Source.PROFESSION,
            173087: Source.PROFESSION,
            173096: Source.PROFESSION,
        }
        if item["instance_type"]:
            # use handcrafted mapping
            return instance_mapping[item["instance_type"]]
        # print(item)
        return item_mapping.get(item["id"], Source.UNKNOWN)

    trinkets = []
    for trinket in loaded_trinkets:
        source = _get_source(trinket)
        itemlevels = _get_itemlevels(trinket, source)
        if not itemlevels:
            continue
        trinkets.append(
            Trinket(
                item_id=trinket["id"],
                itemlevels=itemlevels,
                role=None,  # TODO
                stats=_get_stats(trinket),
                class_mask=trinket["class_mask"],
                translations=_get_translations(trinket),
                source=_get_source(trinket),
                on_use=trinket["on_use"],
                bonus_ids=_get_bonus_ids(trinket),
            )
        )
    return trinkets


TRINKETS: typing.List[Trinket] = _load_trinkets()


def get_trinkets_for_spec(wow_spec: WowSpec) -> typing.Tuple[Trinket, ...]:
    """New function to return all available trinkets for a spec

    Arguments:
      wow_spec {WowSpec} -- instance of a WowSpec

    Returns:
      tuple[Trinket] -- Tuple of all Trinkets
    """

    trinkets: typing.List[Trinket] = []
    for trinket in TRINKETS:
        if trinket.is_usable_by_class(wow_spec.wow_class.id):
            if wow_spec.stat in trinket.stats or len(trinket.stats) == 0:
                trinkets.append(trinket)

    return tuple(trinkets)


def get_versatility_trinket(stat: Stat) -> Trinket:
    """Returns a vers stat stick with the given Stat.

    Returns:
        Trinket -- Versatility Stat stick
    """
    empty_translation = EmptyTranslation()
    empty_translation.US = "Versatility Stat Stick"
    all_classes = 2 ** 16 - 1
    if stat == Stat.AGILITY:
        # "Stat Stick (Versatility)", "142506,bonus_id=607"
        return Trinket(
            item_id="142506",
            bonus_ids=[
                607,
            ],
            itemlevels=[ItemLevel.CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.AGILITY,
            ],
            class_mask=all_classes,
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
        )
    elif stat == Stat.INTELLECT:
        # "Stat Stick (Versatility)", "142507,bonus_id=607"
        return Trinket(
            item_id="142507",
            bonus_ids=[
                607,
            ],
            itemlevels=[ItemLevel.CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.INTELLECT,
            ],
            class_mask=all_classes,
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
        )
    elif stat == Stat.STRENGTH:
        # "Stat Stick (Versatility)", "142508,bonus_id=607"
        return Trinket(
            item_id="142508",
            bonus_ids=[
                607,
            ],
            itemlevels=[ItemLevel.CASTLE_NATHRIA[0]],
            role=None,
            stats=[
                Stat.STRENGTH,
            ],
            class_mask=all_classes,
            translations=empty_translation,
            source=Source.UNKNOWN,
            on_use=False,
        )
    raise ValueError(f"Unknown stat {stat}. No Versatility trinket available.")
