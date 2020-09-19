import json
import pkg_resources
import typing


from simc_support.game_data.Language import _get_translations
from simc_support.game_data.Language import Translation
from simc_support.game_data.SimcObject import SimcObject


class Covenant(SimcObject):
    """Shadowlands specific faction. Each character joins one."""

    def __init__(
        self,
        *args,
        id: int,
        translations: typing.Union[typing.Dict, Translation],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.id = id

        if isinstance(translations, Translation):
            self.translations = translations
        elif isinstance(translations, dict):
            self.translations = Translation(translations=translations)
        else:
            raise TypeError(
                "translations must either be a dictionary or a Translaton object."
            )


def _load_covenants() -> typing.List[Covenant]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "covenants.json"))
    ) as f:
        loaded_covenants = json.load(f)

    covenants = []
    for covenant in loaded_covenants:
        covenants.append(
            Covenant(
                id=covenant["id"],
                translations=_get_translations(covenant),
                full_name=covenant["name"],
                simc_name=covenant["name"].lower().replace(" ", "_"),
            )
        )
    return covenants


COVENANTS = _load_covenants()


def get_covenant(*, id: int = None, name: str = None) -> Covenant:
    if not id and not name:
        raise ValueError("Function requires either 'id' or 'name'.")

    for covenant in COVENANTS:
        if (
            name
            and name.lower().replace(" ", "_") == covenant.simc_name
            or id
            and id == covenant.id
        ):
            return covenant
    raise ValueError(f"No Covenant with name '{name}' found.")
