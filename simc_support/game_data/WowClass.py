from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data import Race
from simc_support.game_data import Language


class WowClass(SimcObject):

    def __init__(
        self, id: int, races: list, translations: Language.Translation, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.id = int(id)
        # double check input to be of Race class
        for race in races:
            if type(race) != Race.Race:
                raise TypeError(
                    "Expected races to be of Race type. Got {} instead.".format(type(race))
                )
            if race not in Race.RACES:
                raise ValueError("Unknown race {}.".format(race))
        self.races = races
        if type(translations) == Language.Translation:
            self.translations = translations
        else:
            self.translations = Language.Translation(translations=translations)


empty_translation = {}
for lang in Language.LANGUAGES:
    empty_translation[lang] = ""

DEATHKNIGHT = WowClass(6, Race.RACES, empty_translation, "Death Knight", 'death_knight')
DEMONHUNTER = WowClass(
    12, [
        Race.NIGHTELF,
        Race.BLOODELF,
    ], empty_translation, "Demon Hunter", 'demon_hunter'
)
DRUID = WowClass(
    11, [
        Race.NIGHTELF,
        Race.WORGEN,
        Race.KULTIRAN,
        Race.TAUREN,
        Race.TROLL,
        Race.HIGHMOUNTAINTAUREN,
        Race.ZANDALARITROLL,
    ], empty_translation, "Druid", 'druid'
)
HUNTER = WowClass(3, Race.RACES, empty_translation, "Hunter", 'hunter')
MAGE = WowClass(
    8, [
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.WORGEN,
        Race.VOIDELF,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Mage", 'mage'
)
MONK = WowClass(
    10, [
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
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
        Race.NIGHTBORNE,
        Race.HIGHMOUNTAINTAUREN,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Monk", 'monk'
)
PALADIN = WowClass(
    2, [
        Race.DRAENEI,
        Race.DWARF,
        Race.HUMAN,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.BLOODELF,
        Race.TAUREN,
        Race.ZANDALARITROLL,
    ], empty_translation, "Paladin", 'paladin'
)
PRIEST = WowClass(
    5, [
        Race.DRAENEI,
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.WORGEN,
        Race.VOIDELF,
        Race.LIGHTFORGEDDRAENEI,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.PANDAREN_HORDE,
        Race.TAUREN,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Priest", 'priest'
)
ROGUE = WowClass(
    4, [
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.NIGHTELF,
        Race.PANDAREN_ALLIANCE,
        Race.WORGEN,
        Race.VOIDELF,
        Race.DARKIRONDWARF,
        Race.KULTIRAN,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.ORC,
        Race.PANDAREN_HORDE,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.MAGHARORC,
        Race.ZANDALARITROLL,
        Race.VULPERA,
    ], empty_translation, "Rogue", 'rogue'
)
SHAMAN = WowClass(
    7, [
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
    ], empty_translation, "Shaman", 'shaman'
)
WARLOCK = WowClass(
    9, [
        Race.DWARF,
        Race.GNOME,
        Race.HUMAN,
        Race.WORGEN,
        Race.VOIDELF,
        Race.DARKIRONDWARF,
        Race.MECHAGNOME,
        Race.BLOODELF,
        Race.GOBLIN,
        Race.ORC,
        Race.TROLL,
        Race.UNDEAD,
        Race.NIGHTBORNE,
        Race.VULPERA,
    ], empty_translation, "Warlock", 'warlock'
)
WARRIOR = WowClass(1, Race.RACES, empty_translation, "Warrior", 'warrior')

WOWCLASSES = [
    DEATHKNIGHT,
    DEMONHUNTER,
    DRUID,
    HUNTER,
    MAGE,
    MONK,
    PALADIN,
    PRIEST,
    ROGUE,
    SHAMAN,
    WARLOCK,
    WARRIOR,
]
