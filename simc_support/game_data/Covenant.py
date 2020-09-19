import json
import pkg_resources
import typing


from simc_support.game_data.Language import Translation
from simc_support.game_data.SimcObject import SimcObject


class Covenant(SimcObject):
    """Shadowlands specific faction. Each character joins one."""

    def __init__(
        self,
        *args,
        covenant_id: int,
        translations: typing.Union[typing.Dict, Translation],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.covenant_id = covenant_id

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

    covenants = []
    for covenant in loaded_covenants:
        covenants.append(
            Covenant(
                covenant_id=covenant["id"],
                translations=_get_translations(covenant),
                full_name=covenant["name"],
                simc_name=covenant["name"].lower().replace(" ", "_"),
            )
        )
    return covenants


COVENANTS = _load_covenants()


def get_covenant(name: str) -> Covenant:
    for covenant in COVENANTS:
        if name.lower().replace(" ", "_") == covenant.simc_name:
            return covenant
    raise ValueError(f"No Covenant with name '{name}' found.")
