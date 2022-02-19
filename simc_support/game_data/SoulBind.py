import copy
import json
import pkg_resources
import typing

from simc_support.game_data.Language import Translation, _get_translations
from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data.Covenant import Covenant, get_covenant


SECOND_SOULBIND_RENOWN = 6
THIRD_SOULBIND_RENOWN = 25
# until found/extracted in game data, here the rown table
# soulbind_id: tier: renown
RENOWN = {
    1: {  # Niya
        0: 0,
        1: 0,
        2: 3,
        3: 7,
        4: 10,
        5: 18,
        6: 25,
        7: 30,
        8: 43,
        9: 46,
        10: 51,
        11: 55,
    },
    2: {  # Dreamweaver
        0: SECOND_SOULBIND_RENOWN,
        1: SECOND_SOULBIND_RENOWN,
        2: SECOND_SOULBIND_RENOWN,
        3: 9,
        4: 13,
        5: 21,
        6: 29,
        7: 34,
        8: 42,
        9: 45,
        10: 49,
        11: 54,
    },
    3: {  # General Draven
        0: THIRD_SOULBIND_RENOWN,
        1: THIRD_SOULBIND_RENOWN,
        2: THIRD_SOULBIND_RENOWN,
        3: THIRD_SOULBIND_RENOWN,
        4: THIRD_SOULBIND_RENOWN,
        5: THIRD_SOULBIND_RENOWN,
        6: 29,
        7: 31,
        8: 41,
        9: 48,
        10: 53,
        11: 57,
    },
    4: {  # Plague Deviser Marileth
        0: 0,
        1: 0,
        2: 3,
        3: 9,
        4: 10,
        5: 21,
        6: 25,
        7: 30,
        8: 43,
        9: 46,
        10: 51,
        11: 55,
    },
    5: {  # Emeni
        0: SECOND_SOULBIND_RENOWN,
        1: SECOND_SOULBIND_RENOWN,
        2: SECOND_SOULBIND_RENOWN,
        3: 7,
        4: 13,
        5: 18,
        6: 28,
        7: 34,
        8: 42,
        9: 45,
        10: 49,
        11: 54,
    },
    6: {  # Korayn
        0: THIRD_SOULBIND_RENOWN,
        1: THIRD_SOULBIND_RENOWN,
        2: THIRD_SOULBIND_RENOWN,
        3: THIRD_SOULBIND_RENOWN,
        4: THIRD_SOULBIND_RENOWN,
        5: THIRD_SOULBIND_RENOWN,
        6: 28,
        7: 31,
        8: 41,
        9: 48,
        10: 53,
        11: 57,
    },
    7: {  # Pelagos
        0: 0,
        1: 0,
        2: 3,
        3: 7,
        4: 10,
        5: 21,
        6: 25,
        7: 30,
        8: 43,
        9: 46,
        10: 51,
        11: 55,
    },
    8: {  # Nadjia the Mistblade
        0: 0,
        1: 0,
        2: 3,
        3: 7,
        4: 10,
        5: 21,
        6: 25,
        7: 30,
        8: 43,
        9: 46,
        10: 51,
        11: 55,
    },
    9: {  # Theotar the Mad Duke
        0: SECOND_SOULBIND_RENOWN,
        1: SECOND_SOULBIND_RENOWN,
        2: SECOND_SOULBIND_RENOWN,
        3: 9,
        4: 13,
        5: 18,
        6: 28,
        7: 34,
        8: 42,
        9: 45,
        10: 49,
        11: 54,
    },
    10: {  # Bonesmith Heirmir
        0: THIRD_SOULBIND_RENOWN,
        1: THIRD_SOULBIND_RENOWN,
        2: THIRD_SOULBIND_RENOWN,
        3: THIRD_SOULBIND_RENOWN,
        4: THIRD_SOULBIND_RENOWN,
        5: THIRD_SOULBIND_RENOWN,
        6: 29,
        7: 31,
        8: 41,
        9: 48,
        10: 53,
        11: 57,
    },
    13: {  # Kleia
        0: SECOND_SOULBIND_RENOWN,
        1: SECOND_SOULBIND_RENOWN,
        2: SECOND_SOULBIND_RENOWN,
        3: 9,
        4: 13,
        5: 18,
        6: 28,
        7: 34,
        8: 42,
        9: 45,
        10: 49,
        11: 54,
    },
    18: {  # Forgelite Prime Mikanikos
        0: THIRD_SOULBIND_RENOWN,
        1: THIRD_SOULBIND_RENOWN,
        2: THIRD_SOULBIND_RENOWN,
        3: THIRD_SOULBIND_RENOWN,
        4: THIRD_SOULBIND_RENOWN,
        5: THIRD_SOULBIND_RENOWN,
        6: 29,
        7: 31,
        8: 41,
        9: 48,
        10: 53,
        11: 57,
    },
}


class SoulBindTalent(SimcObject):
    def __init__(
        self,
        *args,
        id: int,
        spell_id: int,
        tier: int,
        order: int,
        parent_id: int,
        soulbind_id: int,
        type: int,
        translations: typing.Union[typing.Dict, Translation],
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.id = id
        self.spell_id = spell_id
        self.tier = tier
        self.order = order
        self.parent_id = parent_id
        self.soulbind_id = soulbind_id
        self.type = type
        if isinstance(translations, Translation):
            self.translations = translations
        elif isinstance(translations, dict):
            self.translations = Translation(translations=translations)
        else:
            raise TypeError(
                "translations must either be a dictionary or a Translaton object."
            )

    @property
    def is_dps_increase(self) -> bool:
        WHITELIST = [
            # Pelagos
            "Combat Meditation",
            "Better Together",
            "Newfound Resolve",
            # Kleia
            "Pointed Courage",
            "Spear of the Archon",
            "Light the Path",
            # Forgelite Prime Mikanikos
            "Hammer of Genesis",
            "Bron's Call to Action",
            "Soulglow Spectrometer",
            "Effusive Anima Accelerator",
            # Plague Deviser Marelith
            "Volatile Solvent",
            "Plaguey's Preemptive Strike",
            "Kevin's Oozeling",
            # Emeni
            "Lead by Example",
            "Gnashing Chompers",
            "Pustule Eruption",
            # Bonesmith Heirmir
            "Forgeborne Reveries",
            "Heirmir's Arsenal: Marrowed Gemstone",
            "Carver's Eye",
            "Mnemonic Equipment",
            # Niya
            "Niya's Tools: Burrs",
            "Niya's Tools: Poison",
            "Grove Invigoration",
            "Bonded Hearts",
            # Dreamweaver
            "Field of Blossoms",
            "Social Butterfly",
            "Dream Delver",
            # Korayn
            "First Strike",
            "Wild Hunt Tactics",
            "Wild Hunt Strategem",
            # Nadja the Mistblade
            "Exacting Preparation",
            "Dauntless Duelist",
            "Thrill Seeker",
            "Fatal Flaw",
            # Theotar the Mad Duke
            "Refined Palate",
            "Soothing Shade",
            "Wasteland Propriety",
            # General Draven
            "Superior Tactics",
            "Built for War",
            "Battlefield Presence",
        ]
        return self.full_name in WHITELIST or self.is_potency

    @property
    def is_finesse(self) -> bool:
        return self.type == 1

    @property
    def is_potency(self) -> bool:
        return self.type == 2

    @property
    def is_endurance(self) -> bool:
        return self.type == 3

    @property
    def renown(self) -> int:
        return RENOWN[self.soulbind_id][self.tier]


class SoulBind(SimcObject):
    """Shadowlands specific additional talent tree."""

    def __init__(
        self,
        *args,
        id: int,
        covenant: Covenant,
        translations: typing.Union[typing.Dict, Translation],
        soul_bind_talents: typing.List[SoulBindTalent],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.id: int = id
        self.covenant: Covenant = covenant
        self.soul_bind_talents: typing.List[SoulBindTalent] = soul_bind_talents

        if isinstance(translations, Translation):
            self.translations: Translation = translations
        elif isinstance(translations, dict):
            self.translations = Translation(translations=translations)
        else:
            raise TypeError(
                "translations must either be a dictionary or a Translaton object."
            )

    @property
    def talent_paths(self) -> typing.List[typing.List[SoulBindTalent]]:
        max_tier = 11

        paths: typing.List[typing.List[SoulBindTalent]] = [[]]

        for i in range(max_tier + 1):
            talents = [talent for talent in self.soul_bind_talents if talent.tier == i]

            new_paths = []
            # create a deepcopy for each
            for talent in talents:
                if talent.parent_id == 0:
                    for path in paths:
                        new_paths.append(copy.deepcopy(path) + [talent])
                else:
                    for path in paths:
                        if path[-1].id == talent.parent_id:
                            new_paths.append(copy.deepcopy(path) + [talent])
            paths = new_paths

        return paths


def _load_soul_binds() -> typing.List[SoulBind]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "soul_binds.json"))
    ) as f:
        loaded_soul_binds = json.load(f)

    def create_talent(dict, soulbind_id) -> SoulBindTalent:
        return SoulBindTalent(
            id=dict["id"],
            spell_id=dict["spell_id"],
            tier=dict["tier"],
            order=dict["ui_order"],
            parent_id=dict["id_garr_talent_prereq"],
            soulbind_id=soulbind_id,
            type=dict["conduit_type"],
            translations=_get_translations(dict),
            full_name=dict["name"],
            simc_name=dict["name"].lower().replace(" ", "_"),
        )

    soul_binds = []
    for soul_bind in loaded_soul_binds:
        soul_binds.append(
            SoulBind(
                id=soul_bind["id"],
                covenant=get_covenant(id=soul_bind["id_covenant"]),
                translations=_get_translations(soul_bind),
                full_name=soul_bind["name"],
                simc_name=soul_bind["name"].lower().replace(" ", "_"),
                soul_bind_talents=[
                    create_talent(talent, soul_bind["id"])
                    for talent in soul_bind["talents"]
                ],
            )
        )
    return soul_binds


SOULBINDS = _load_soul_binds()


def get_soul_bind(*, id: int = None, name: str = None) -> SoulBind:
    if not id and not name:
        raise ValueError("Function requires either 'id' or 'name'.")

    for soul_bind in SOULBINDS:
        if name and name == soul_bind.full_name or id and id == soul_bind.id:
            return soul_bind
    raise ValueError(f"No Soul Bind with id '{id}' or name '{name}' found.")
