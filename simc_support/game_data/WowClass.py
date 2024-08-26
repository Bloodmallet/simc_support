import typing

from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data import Race
from simc_support.game_data import Language


class WowClass(SimcObject):
    def __init__(
        self,
        id: int,
        races: typing.Tuple[Race.Race, ...],
        translations: Language.Translation,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.id: int = int(id)
        # double check input to be of Race class
        for race in races:
            if not isinstance(race, Race.Race):
                raise TypeError(
                    "Expected races to be of Race type. Got {} instead.".format(
                        type(race)
                    )
                )
            if race not in Race.RACES:
                raise ValueError("Unknown race {}.".format(race))
        self.races: typing.Tuple[Race.Race, ...] = races
        if isinstance(translations, Language.Translation):
            self.translations: Language.Translation = translations
        else:
            self.translations = Language.Translation(translations=translations)


_all_non_dracthyr_and_earthen_races = tuple(
    [
        r
        for r in Race.RACES
        if r
        not in (
            Race.DRACTHYR_ALLIANCE,
            Race.DRACTHYR_HORDE,
            Race.EARTHEN_ALLIANCE,
            Race.EARTHEN_HORDE,
        )
    ]
)
_earthen = (Race.EARTHEN_ALLIANCE, Race.EARTHEN_HORDE)

DEATHKNIGHT = WowClass(
    6,
    _all_non_dracthyr_and_earthen_races,
    Language.EmptyTranslation(),
    "Death Knight",
    "death_knight",
)
DEMONHUNTER = WowClass(
    12,
    (
        Race.NIGHTELF,
        Race.BLOODELF,
    ),
    Language.EmptyTranslation(),
    "Demon Hunter",
    "demon_hunter",
)
DRUID = WowClass(
    11,
    (
        Race.NIGHTELF,
        Race.WORGEN,
        Race.KULTIRAN,
        Race.TAUREN,
        Race.TROLL,
        Race.HIGHMOUNTAINTAUREN,
        Race.ZANDALARITROLL,
    ),
    Language.EmptyTranslation(),
    "Druid",
    "druid",
)
EVOKER = WowClass(
    13,
    (
        Race.DRACTHYR_ALLIANCE,
        Race.DRACTHYR_HORDE,
    ),
    Language.EmptyTranslation(),
    "Evoker",
    "evoker",
)
HUNTER = WowClass(
    3,
    _all_non_dracthyr_and_earthen_races + _earthen,
    Language.EmptyTranslation(),
    "Hunter",
    "hunter",
)
MAGE = WowClass(
    8,
    _all_non_dracthyr_and_earthen_races + _earthen,
    Language.EmptyTranslation(),
    "Mage",
    "mage",
)
MONK = WowClass(
    10,
    (
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.LIGHTFORGEDDRAENEI,
        Race.NIGHTELF,
        Race.WORGEN,
        Race.PANDAREN_ALLIANCE,
        Race.VOIDELF,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TAUREN,
        Race.TROLL,
        Race.UNDEAD,
        Race.GOBLIN,
        Race.NIGHTBORNE,
        Race.HIGHMOUNTAINTAUREN,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    )
    + _earthen,
    Language.EmptyTranslation(),
    "Monk",
    "monk",
)
PALADIN = WowClass(
    2,
    (
        Race.DRAENEI,
        Race.DWARF,
        Race.HUMAN,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.BLOODELF,
        Race.TAUREN,
        Race.ZANDALARITROLL,
    )
    + _earthen,
    Language.EmptyTranslation(),
    "Paladin",
    "paladin",
)
PRIEST = WowClass(
    5,
    _all_non_dracthyr_and_earthen_races + _earthen,
    Language.EmptyTranslation(),
    "Priest",
    "priest",
)
ROGUE = WowClass(
    4,
    _all_non_dracthyr_and_earthen_races + _earthen,
    Language.EmptyTranslation(),
    "Rogue",
    "rogue",
)
SHAMAN = WowClass(
    7,
    (
        Race.DRAENEI,
        Race.DWARF,
        Race.PANDAREN_ALLIANCE,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.GOBLIN,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TAUREN,
        Race.TROLL,
        Race.HIGHMOUNTAINTAUREN,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    )
    + _earthen,
    Language.EmptyTranslation(),
    "Shaman",
    "shaman",
)
WARLOCK = WowClass(
    9,
    _all_non_dracthyr_and_earthen_races + _earthen,
    Language.EmptyTranslation(),
    "Warlock",
    "warlock",
)
WARRIOR = WowClass(
    1,
    _all_non_dracthyr_and_earthen_races + _earthen,
    Language.EmptyTranslation(),
    "Warrior",
    "warrior",
)

WOWCLASSES = (
    DEATHKNIGHT,
    DEMONHUNTER,
    DRUID,
    EVOKER,
    HUNTER,
    MAGE,
    MONK,
    PALADIN,
    PRIEST,
    ROGUE,
    SHAMAN,
    WARLOCK,
    WARRIOR,
)


def get_wow_class(name: str) -> WowClass:
    for wow_class in WOWCLASSES:
        if wow_class.full_name == name or wow_class.simc_name == name:
            return wow_class
    raise ValueError(f"No WowClass found with name '{name}'.")
