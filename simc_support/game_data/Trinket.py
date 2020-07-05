import typing

from simc_support.game_data import Source
from simc_support.game_data.ItemLevel import *  # pylint: disable=unused-wildcard-import
from simc_support.game_data.Role import Role
from simc_support.game_data.Source import Source
from simc_support.game_data.Stat import Stat

try:
    # import exists to enable type hinting
    from simc_support.game_data.WowSpec import WowSpec
except ImportError:
    WowSpec = object


class Trinket(object):

    def __init__(
        self,
        name: str,
        item_id: str,
        min_itemlevel: int,
        max_itemlevel: int,
        max_itemlevel_drop: int,
        stat: typing.Union[Stat, typing.List[Stat]],
        role: Role,
        legendary: bool = False,
        source: str = None,
        active: bool = False
    ):
        """Creates a Trinket instance

        Args:
            name (str): Name
            item_id (str): Item ID
            min_itemlevel (int): Minimal available itemlevel
            max_itemlevel (int): maximum available itemlevel (warforged/upgrades)
            max_itemlevel_drop (int): maximum dropping itemlevel
            stat (typing.Union[Stat, typing.List[Stat]]): primary stats
            role (Role): spec role
            legendary (bool, optional): Flag to determine legendaries. Defaults to False.
            source (str, optional): Drop source. Defaults to None.
            active (bool, optional): Is the trinket on use? Defaults to False.
        """
        super(Trinket, self).__init__()
        self.name: str = str(name)
        self.item_id: str = str(item_id)
        self.min_itemlevel: int = int(min_itemlevel)
        self.max_itemlevel: int = int(max_itemlevel)
        self.max_itemlevel_drop: int = int(max_itemlevel_drop)

        if isinstance(stat, list):
            for element in stat:
                if element not in Stat:
                    raise ValueError("One or more provided stats are unknown.")
        elif stat not in Stat:
            raise ValueError(f"Unknown stat '{stat}'")
        if isinstance(stat, list) or isinstance(stat, tuple):
            self.stat = tuple(stat)
        else:
            self.stat = tuple([stat])

        self.role = role

        self.legendary: bool = bool(legendary)
        if str(source) not in Source:
            raise ValueError(f"Unknown source '{source}'.")
        self.source: str = str(source)
        self.active: bool = bool(active)
        # might need to transform stat and role to spec at some point...


TRINKETS: typing.List[Trinket] = ()


def get_trinkets_for_spec(wow_spec: WowSpec) -> tuple:
    """New function to return all available trinkets for a spec

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
