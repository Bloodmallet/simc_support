import typing

from simc_support.game_data import Faction
from simc_support.game_data.Faction import ALLIANCE
from simc_support.game_data.Faction import HORDE
from simc_support.game_data.Language import Translation, Language
from simc_support.game_data.SimcObject import SimcObject


class Race(SimcObject):
    """Race defines how your character looks, moves, and what racial ability you have."""

    def __init__(
        self,
        faction: Faction.Faction,
        full_name: str,
        simc_name: str,
        translations: typing.Union[typing.Dict, Translation],
        *args,
        **kwargs,
    ) -> None:
        super().__init__(full_name, simc_name, *args, **kwargs)

        self.faction: Faction.Faction = faction

        if isinstance(translations, Translation):
            self.translations: Translation = translations
        elif isinstance(translations, dict):
            self.translations = Translation(translations=translations)
        else:
            raise TypeError(
                "translations must either be a dictionary or a Translaton object."
            )


# Alliance
DARKIRONDWARF = Race(
    ALLIANCE,
    "Dark Iron Dwarf",
    "dark_iron_dwarf",
    {
        Language.US: "Dark Iron Dwarf",
        Language.IT: "Nano Ferroscuro",
        Language.DE: "Dunkeleisenzwerg",
        Language.FR: "Nain sombrefer",
        Language.RU: "Дворф из клана Черного Железа",
        Language.ES: "Enano Hierro Negro",
        Language.KR: "검은무쇠 드워프",
        Language.CN: "黑铁矮人",
        Language.BR: "Anão Ferro Negro",
    },
)
DRACTHYR_ALLIANCE = Race(
    ALLIANCE,
    "Dracthyr",
    "dracthyr",
    {
        Language.US: "Dracthyr",
        Language.IT: "Dracthyr",
        Language.DE: "Dracthyr",
        Language.FR: "Dracthyr",
        Language.RU: "Dracthyr",
        Language.ES: "Dracthyr",
        Language.KR: "Dracthyr",
        Language.CN: "Dracthyr",
        Language.BR: "Dracthyr",
    },
)
DRAENEI = Race(
    ALLIANCE,
    "Draenei",
    "draenei",
    {
        Language.US: "Draenei",
        Language.IT: "Draenei",
        Language.DE: "Draenei",
        Language.FR: "Draeneï",
        Language.RU: "Дреней",
        Language.ES: "Draenei",
        Language.KR: "드레나이",
        Language.CN: "德莱尼",
        Language.BR: "Draenei",
    },
)
DWARF = Race(
    ALLIANCE,
    "Dwarf",
    "dwarf",
    {
        Language.US: "Dwarf",
        Language.IT: "Nano",
        Language.DE: "Zwerg",
        Language.FR: "Nain",
        Language.RU: "Дворф",
        Language.ES: "Enano",
        Language.KR: "드워프",
        Language.CN: "矮人",
        Language.BR: "Anão",
    },
)
EARTHEN_ALLIANCE = Race(
    ALLIANCE,
    "Earthen",
    "earthen",
    {
        Language.US: "Earthen",
        Language.IT: "Terrigeno",
        Language.DE: "Irdener",
        Language.FR: "Terrestre",
        Language.RU: "Земельник",
        Language.ES: "Terráneo",
        Language.KR: "토석인",
        Language.CN: "土灵",
        Language.BR: "Terrano",
    },
)
GNOME = Race(
    ALLIANCE,
    "Gnome",
    "gnome",
    {
        Language.US: "Gnome",
        Language.IT: "Gnomo",
        Language.DE: "Gnom",
        Language.FR: "Gnome",
        Language.RU: "Гном",
        Language.ES: "Gnomo",
        Language.KR: "노움",
        Language.CN: "侏儒",
        Language.BR: "Gnomo",
    },
)
HUMAN = Race(
    ALLIANCE,
    "Human",
    "human",
    {
        Language.US: "Human",
        Language.IT: "Umano",
        Language.DE: "Mensch",
        Language.FR: "Humain",
        Language.RU: "Человек",
        Language.ES: "Humano",
        Language.KR: "인간",
        Language.CN: "人类",
        Language.BR: "Humano",
    },
)
KULTIRAN = Race(
    ALLIANCE,
    "Kul Tiran",
    "kul_tiran",
    {
        Language.US: "Kul Tiran",
        Language.IT: "Kul Tirano",
        Language.DE: "Kul Tiraner",
        Language.FR: "Kultirassien",
        Language.RU: "Култирасец",
        Language.ES: "Ciudadano de Kul Tiras",
        Language.KR: "쿨 티란",
        Language.CN: "库尔提拉斯人",
        Language.BR: "Kultireno",
    },
)
LIGHTFORGEDDRAENEI = Race(
    ALLIANCE,
    "Lightforged Draenei",
    "lightforged_draenei",
    {
        Language.US: "Lightforged Draenei",
        Language.IT: "Draenei Forgialuce",
        Language.DE: "Lichtgeschmiedeter Draenei",
        Language.FR: "Draeneï sancteforge",
        Language.RU: "Озаренный дреней",
        Language.ES: "Draenei forjado por la Luz",
        Language.KR: "빛벼림 드레나이",
        Language.CN: "光铸德莱尼",
        Language.BR: "Draenei Forjado a Luz",
    },
)
MECHAGNOME = Race(
    ALLIANCE,
    "Mechagnome",
    "mechagnome",
    {
        Language.US: "Mechagnome",
        Language.IT: "Meccagnomo",
        Language.DE: "Mechagnom",
        Language.FR: "Mécagnome",
        Language.RU: "Механогном",
        Language.ES: "Mecagnomo",
        Language.KR: "기계노움",
        Language.CN: "机械侏儒",
        Language.BR: "Gnomecânico",
    },
)
NIGHTELF = Race(
    ALLIANCE,
    "Night Elf",
    "night_elf",
    {
        Language.US: "Night Elf",
        Language.IT: "Elfo della Notte",
        Language.DE: "Nachtelf",
        Language.FR: "Elfe de la nuit",
        Language.RU: "Ночной эльф",
        Language.ES: "Elfo de la noche",
        Language.KR: "나이트 엘프",
        Language.CN: "暗夜精灵",
        Language.BR: "Elfo Noturno",
    },
)
PANDAREN_ALLIANCE = Race(
    ALLIANCE,
    "Pandaren",
    "pandaren",
    {
        Language.US: "Pandaren",
        Language.IT: "Pandaren",
        Language.DE: "Pandaren",
        Language.FR: "Pandaren",
        Language.RU: "Пандарен",
        Language.ES: "Pandaren",
        Language.KR: "판다렌",
        Language.CN: "熊猫人",
        Language.BR: "Pandaren",
    },
)
WORGEN = Race(
    ALLIANCE,
    "Worgen",
    "worgen",
    {
        Language.US: "Worgen",
        Language.IT: "Worgen",
        Language.DE: "Worgen",
        Language.FR: "Worgen",
        Language.RU: "Ворген",
        Language.ES: "Huargen",
        Language.KR: "늑대인간",
        Language.CN: "狼人",
        Language.BR: "Worgen",
    },
)
VOIDELF = Race(
    ALLIANCE,
    "Void Elf",
    "void_elf",
    {
        Language.US: "Void Elf",
        Language.IT: "Elfo del Vuoto",
        Language.DE: "Leerenelf",
        Language.FR: "Elfe du Vide",
        Language.RU: "Эльф Бездны",
        Language.ES: "Elfo del Vacío",
        Language.KR: "공허 엘프",
        Language.CN: "虚空精灵",
        Language.BR: "Elfo Caótico",
    },
)

# Horde
BLOODELF = Race(
    HORDE,
    "Blood Elf",
    "blood_elf",
    {
        Language.US: "Blood Elf",
        Language.IT: "Elfo del Sangue",
        Language.DE: "Blutelf",
        Language.FR: "Elfe de sang",
        Language.RU: "Эльф крови",
        Language.ES: "Elfo de sangre",
        Language.KR: "블러드 엘프",
        Language.CN: "血精灵",
        Language.BR: "Elfo Sangrento",
    },
)
DRACTHYR_HORDE = Race(
    HORDE,
    "Dracthyr",
    "dracthyr",
    {
        Language.US: "Dracthyr",
        Language.IT: "Dracthyr",
        Language.DE: "Dracthyr",
        Language.FR: "Dracthyr",
        Language.RU: "Dracthyr",
        Language.ES: "Dracthyr",
        Language.KR: "Dracthyr",
        Language.CN: "Dracthyr",
        Language.BR: "Dracthyr",
    },
)
EARTHEN_HORDE = Race(
    HORDE,
    "Earthen",
    "earthen",
    {
        Language.US: "Earthen",
        Language.IT: "Terrigeno",
        Language.DE: "Irdener",
        Language.FR: "Terrestre",
        Language.RU: "Земельник",
        Language.ES: "Terráneo",
        Language.KR: "토석인",
        Language.CN: "土灵",
        Language.BR: "Terrano",
    },
)
GOBLIN = Race(
    HORDE,
    "Goblin",
    "goblin",
    {
        Language.US: "Goblin",
        Language.IT: "Goblin",
        Language.DE: "Goblin",
        Language.FR: "Gobelin",
        Language.RU: "Гоблин",
        Language.ES: "Goblin",
        Language.KR: "고블린",
        Language.CN: "地精",
        Language.BR: "Goblin",
    },
)
HIGHMOUNTAINTAUREN = Race(
    HORDE,
    "Highmountain Tauren",
    "highmountain_tauren",
    {
        Language.US: "Highmountain Tauren",
        Language.IT: "Tauren di Alto Monte",
        Language.DE: "Hochbergtauren",
        Language.FR: "Tauren de Haut-Roc",
        Language.RU: "Таурен Крутогорья",
        Language.ES: "Tauren Monte Alto",
        Language.KR: "높은산 타우렌",
        Language.CN: "至高岭牛头人",
        Language.BR: "Tauren Altamontês",
    },
)
MAGHARORC = Race(
    HORDE,
    "Mag'har Orc",
    "maghar_orc",
    {
        Language.US: "Mag'har Orc",
        Language.IT: "Orco Mag'har",
        Language.DE: "Mag'har",
        Language.FR: "Orc mag’har",
        Language.RU: "Маг'хар",
        Language.ES: "Orco Mag'har",
        Language.KR: "마그하르 오크",
        Language.CN: "玛格汉兽人",
        Language.BR: "Orc Mag'har",
    },
)
NIGHTBORNE = Race(
    HORDE,
    "Nightborne",
    "nightborne",
    {
        Language.US: "Nightborne",
        Language.IT: "Nobile Oscuro",
        Language.DE: "Nachtgeborener",
        Language.FR: "Sacrenuit",
        Language.RU: "Ночнорожденный",
        Language.ES: "Nocheterna",
        Language.KR: "나이트본",
        Language.CN: "夜之子",
        Language.BR: "Filho da Noite",
    },
)
ORC = Race(
    HORDE,
    "Orc",
    "orc",
    {
        Language.US: "Orc",
        Language.IT: "Orco",
        Language.DE: "Orc",
        Language.FR: "Orc",
        Language.RU: "Орк",
        Language.ES: "Orco",
        Language.KR: "오크",
        Language.CN: "兽人",
        Language.BR: "Orc",
    },
)
PANDAREN_HORDE = Race(
    HORDE,
    "Pandaren",
    "pandaren",
    {
        Language.US: "Pandaren",
        Language.IT: "Pandaren",
        Language.DE: "Pandaren",
        Language.FR: "Pandaren",
        Language.RU: "Пандарен",
        Language.ES: "Pandaren",
        Language.KR: "판다렌",
        Language.CN: "熊猫人",
        Language.BR: "Pandaren",
    },
)
TAUREN = Race(
    HORDE,
    "Tauren",
    "tauren",
    {
        Language.US: "Tauren",
        Language.IT: "Tauren",
        Language.DE: "Tauren",
        Language.FR: "Tauren",
        Language.RU: "Таурен",
        Language.ES: "Tauren",
        Language.KR: "타우렌",
        Language.CN: "牛头人",
        Language.BR: "Tauren",
    },
)
TROLL = Race(
    HORDE,
    "Troll",
    "troll",
    {
        Language.US: "Troll",
        Language.IT: "Troll",
        Language.DE: "Troll",
        Language.FR: "Troll",
        Language.RU: "Тролль",
        Language.ES: "Trol",
        Language.KR: "트롤",
        Language.CN: "巨魔",
        Language.BR: "Troll",
    },
)
UNDEAD = Race(
    HORDE,
    "Undead",
    "undead",
    {
        Language.US: "Undead",
        Language.IT: "Non Morto",
        Language.DE: "Untoter",
        Language.FR: "Mort-vivant",
        Language.RU: "Нежить",
        Language.ES: "No-muerto",
        Language.KR: "언데드",
        Language.CN: "亡灵",
        Language.BR: "Morto-vivo",
    },
)
VULPERA = Race(
    HORDE,
    "Vulpera",
    "vulpera",
    {
        Language.US: "Vulpera",
        Language.IT: "Vulpera",
        Language.DE: "Vulpera",
        Language.FR: "Vulpérin",
        Language.RU: "Вульпера",
        Language.ES: "Vulpera",
        Language.KR: "불페라",
        Language.CN: "狐人",
        Language.BR: "Vulpera",
    },
)
ZANDALARITROLL = Race(
    HORDE,
    "Zandalari Troll",
    "zandalari_troll",
    {
        Language.US: "Zandalari Troll",
        Language.IT: "Troll Zandalari",
        Language.DE: "Zandalaritroll",
        Language.FR: "Troll zandalari",
        Language.RU: "Зандалар",
        Language.ES: "Trol Zandalari",
        Language.KR: "잔달라 트롤",
        Language.CN: "赞达拉巨魔",
        Language.BR: "Troll Zandalari",
    },
)

RACES = (
    DARKIRONDWARF,
    DRACTHYR_ALLIANCE,
    DRAENEI,
    DWARF,
    EARTHEN_ALLIANCE,
    GNOME,
    HUMAN,
    KULTIRAN,
    LIGHTFORGEDDRAENEI,
    MECHAGNOME,
    NIGHTELF,
    PANDAREN_ALLIANCE,
    WORGEN,
    VOIDELF,
    BLOODELF,
    DRACTHYR_HORDE,
    EARTHEN_HORDE,
    GOBLIN,
    HIGHMOUNTAINTAUREN,
    MAGHARORC,
    NIGHTBORNE,
    ORC,
    PANDAREN_HORDE,
    TAUREN,
    TROLL,
    UNDEAD,
    VULPERA,
    ZANDALARITROLL,
)


def get_race(name: str) -> Race:
    for race in RACES:
        if race.full_name == name or race.simc_name == name:
            return race
    raise ValueError(f"No race '{name}' found.")
