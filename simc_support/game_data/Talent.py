import json
import pkg_resources
import typing

try:
    from simc_support.game_data.WowSpec import WowSpec
except ImportError:
    WowSpec: object = None  # type: ignore # test setup
from simc_support.game_data.Language import Translation, _get_translations
from simc_support.game_data.SimcObject import SimcObject


class Talent(SimcObject):
    def __init__(
        self,
        wow_class_id: int,
        wow_spec_id: int,
        name: str,
        spell_id: int,
        row: int,
        column: int,
        translations: Translation,
    ):
        super().__init__(full_name=name)
        self.wow_class_id = int(wow_class_id)
        self.wow_spec_id = int(wow_spec_id)
        self.name = str(name)
        self.spell_id = int(spell_id)
        self.row = int(row)
        self.column = int(column)
        if isinstance(translations, Translation):
            self.translations = translations
        else:
            self.translations = Translation(translations=translations)

    def get_dict(self) -> dict:
        return {"name": self.name, "spell_id": self.spell_id}

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.simc_name


def _load_talents() -> typing.List[Talent]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "talents.json"))
    ) as f:
        loaded_talents = json.load(f)

    talents = []
    for talent in loaded_talents:
        talents.append(
            Talent(
                wow_class_id=talent["class_id"],
                wow_spec_id=talent["spec_id"],
                name=talent["name"],
                spell_id=talent["id_spell"],
                row=talent["row"],
                column=talent["col"],
                translations=_get_translations(talent),
            )
        )

    return talents


TALENTS = _load_talents()


def get_talent_dict(wow_spec: WowSpec, ptr: bool = None) -> dict:
    """Return the dict of all talents available to this spec. Structur: row -> column -> name, spell_id

    Arguments:
        wow_spec {WowSpec} -- [description]

    Returns:
        dict -- row -> column -> name, spell_id
    """
    talents = list(
        [
            talent
            for talent in TALENTS
            if talent.wow_spec_id == wow_spec.id
            or talent.wow_spec_id == 0  # shared between specs
            and talent.wow_class_id == wow_spec.wow_class.id
        ]
    )

    result = {}  # type: ignore # newer python versions and thus mypy versions want an annotation here
    for row in range(1, 8):
        result[row] = {}

    for talent in talents:
        # spec specific information precedes class information
        if talent.wow_spec_id == 0 and (talent.column + 1) in result[talent.row + 1]:
            continue
        result[talent.row + 1][talent.column + 1] = talent.get_dict()

    return result


def get_talents_for_spec(wow_spec: WowSpec) -> typing.Tuple[Talent, ...]:
    return tuple(
        [
            talent
            for talent in TALENTS
            if talent.wow_spec_id == 0
            and talent.wow_class_id == wow_spec.wow_class.id
            or talent.wow_spec_id == wow_spec.id
        ]
    )
