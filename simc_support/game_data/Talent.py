import json

import pkg_resources

try:
    # import exists to enable type hinting
    from simc_support.game_data.WowSpec import WowSpec
except ImportError:
    WowSpec = object


class Talent(object):
    def __init__(
        self,
        name: str,
        spell_id: str,
        row: str,
        column: str,
    ):
        self.name = name
        self.spell_id = spell_id
        self.row = row
        self.column = column


def get_talent_dict(wow_spec: WowSpec, ptr: bool = False) -> dict:
    """Return the dict of all talents available to this spec. Structur: row -> column -> name, spell_id

    Arguments:
        wow_spec {WowSpec} -- [description]

    Returns:
        dict -- row -> column -> name, spell_id
    """

    file_name = "talent_list.json"
    if ptr:
        file_name = "talent_list_ptr.json"

    with open(
        pkg_resources.resource_filename(__name__, "/".join(("data_files", file_name))),
        "r",
        encoding="UTF-8",
    ) as f:
        talents = json.load(f, encoding="UTF-8")

    return talents[wow_spec.wow_class.simc_name.title()][wow_spec.simc_name.title()]
