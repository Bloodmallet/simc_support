import json
import pkg_resources
import typing

from simc_support.game_data.Covenant import Covenant
from simc_support.game_data.Covenant import COVENANTS
from simc_support.game_data.Language import _get_translations
from simc_support.game_data.Language import Translation
from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data.WowSpec import WowSpec
from simc_support.game_data.WowSpec import WOWSPECS


class Conduit(SimcObject):
    def __init__(
        self,
        *args,
        id: int,
        conduit_type: int,
        covenants: typing.List[Covenant],
        spec_mask: int,
        wow_specs: typing.List[WowSpec],
        spell_id: int,
        ranks: typing.List[int],
        translations: Translation,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.id = int(id)
        self.type = int(conduit_type)
        if not isinstance(covenants, (list, tuple)):
            raise TypeError(
                f"covenants expected list or tuple. Got '{type(covenants)}' instead."
            )
        if not all([isinstance(covenant, Covenant) for covenant in covenants]):
            raise TypeError(
                "covenants expected a list or tuple of Covenant type objects."
            )
        self.covenants = covenants
        self.spec_mask = int(spec_mask)
        if not all([isinstance(spec, WowSpec) for spec in wow_specs]):
            raise TypeError("wow_specs expected a list or tuple of WowSpec's.")
        self.wow_specs = wow_specs
        self.spell_id = int(spell_id)
        self.ranks = ranks

        if isinstance(translations, Translation):
            self.translations = translations
        elif isinstance(translations, dict):
            self.translations = Translation(translations=translations)
        else:
            raise TypeError(
                "translations must either be a dictionary or a Translaton object."
            )

    @property
    def is_finesse(self) -> bool:
        return self.type == 0

    @property
    def is_potency(self) -> bool:
        return self.type == 1

    @property
    def is_endurance(self) -> bool:
        return self.type == 2


def _load_conduits() -> typing.List[Conduit]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "conduits.json"))
    ) as f:
        loaded_conduits = json.load(f)

    def _get_specs(conduit: dict) -> typing.List[WowSpec]:
        return list([spec for spec in WOWSPECS if spec.id in conduit["spec_ids"]])

    def _get_covenants(conduit: dict) -> typing.List[Covenant]:
        return list(
            [
                covenant
                for covenant in COVENANTS
                if covenant.id == conduit["id_covenant"] or conduit["id_covenant"] == 0
            ]
        )

    conduits = []
    for conduit in loaded_conduits:
        conduits.append(
            Conduit(
                full_name=conduit["name"],
                id=conduit["id"],
                conduit_type=conduit["type"],
                covenants=_get_covenants(conduit),
                spec_mask=conduit["id_spec_set"],
                wow_specs=_get_specs(conduit),
                spell_id=conduit["spell_id"],
                ranks=list([rank + 1 for rank in conduit["ranks"]]),
                translations=_get_translations(conduit),
            )
        )
    return conduits


CONDUITS: typing.List[Conduit] = _load_conduits()


def get_conduits_for_spec(wow_spec: WowSpec) -> typing.Tuple[Conduit]:
    """Return all dps conduits for a spec.

    Arguments:
      wow_spec {WowSpec} -- instance of a WowSpec

    Returns:
      tuple[Conduit] -- Tuple of all dps Conduits
    """

    conduits = [
        conduit
        for conduit in CONDUITS
        if wow_spec in conduit.wow_specs and conduit.is_potency
    ]

    return tuple(conduits)
