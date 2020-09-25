import json
import pkg_resources
import typing

from simc_support.game_data.SimcObject import SimcObject
from simc_support.game_data.Language import Translation, _get_translations
from simc_support.game_data.WowSpec import WowSpec, WOWSPECS


class Legendary(SimcObject):
    """World of Warcraft Legendary class"""

    def __init__(
        self,
        *args,
        id: int,
        bonus_id: int,
        spell_id: int,
        wow_specs: typing.List[WowSpec],
        translations: Translation,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.id = int(id)
        self.bonus_id = int(bonus_id)
        self.spell_id = int(spell_id)

        if not all([isinstance(spec, WowSpec) for spec in wow_specs]):
            raise TypeError("wow_specs expected a list or tuple of WowSpec's.")
        self.wow_specs = wow_specs

        if isinstance(translations, Translation):
            self.translations = translations
        else:
            self.translations = Translation(translations=translations)


def _load_legendaries() -> typing.List[Legendary]:
    with pkg_resources.resource_stream(
        __name__, "/".join(("data_files", "legendaries.json"))
    ) as f:
        loaded_legendaries = json.load(f)

    def _get_specs(legendary) -> typing.List[WowSpec]:
        specs: typing.List[int] = legendary["spec_ids"]

        wow_specs: typing.List[WowSpec] = []

        for spec in specs:
            for real_spec in WOWSPECS:
                if spec == real_spec.id:
                    wow_specs.append(real_spec)

        return wow_specs

    legendaries = []
    for legendary in loaded_legendaries:
        legendaries.append(
            Legendary(
                full_name=legendary["name"],
                id=legendary["id"],
                spell_id=legendary["id_spell"],
                bonus_id=legendary["id_bonus"],
                translations=_get_translations(legendary),
                wow_specs=_get_specs(legendary),
            )
        )

    return legendaries


LEGENDARIES: typing.List[Legendary] = _load_legendaries()


def get_legendaries_for_spec(wow_spec: WowSpec) -> typing.Tuple[Legendary]:
    """Return a tuple of legendaries for the provided WowSpec.

    Args:
        wow_spec (WowSpec): a valid WowSpec class instance

    Returns:
        typing.List[Legendary]: [description]
    """
    if not isinstance(wow_spec, WowSpec):
        raise TypeError("wow_spec needs to be of type WowSpec.")
    return tuple(
        [legendary for legendary in LEGENDARIES if wow_spec in legendary.wow_specs]
    )
