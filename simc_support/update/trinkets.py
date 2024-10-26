import enum
import json
import logging
import os
import typing

from .extractor import Extractor, LOCALE_TABLES
from .utils import collect_localizations, safely_convert_to, DATA_PATH

logger = logging.getLogger(__name__)

WANTED_ITEM_IDS_OR_NAMES = [
    181457,
    184842,
]

US = "en_US"


class Expansion(int, enum.Enum):
    CLASSIC = 0
    BURNING_CRUSADE = 1
    WRATH_OF_THE_LICHKING = 2
    CATACLYSM = 3
    PANDARIA = 4
    WARLORDS_OF_DRAENOR = 5
    LEGION = 6
    BATTLE_FOR_AZEROTH = 7
    SHADOWLANDS = 8
    DRAGONFLIGHT = 9


MIN_RELEVANT_EXPANSION = Expansion.PANDARIA


def _is_trinket(item: dict) -> bool:
    """See https://github.com/simulationcraft/simc/blob/shadowlands/engine/dbc/data_enums.hh#L335"""
    return item.get("inv_type") == 12


def _is_wanted(item: dict) -> bool:
    return (
        item.get("id") in WANTED_ITEM_IDS_OR_NAMES
        or item.get("name") in WANTED_ITEM_IDS_OR_NAMES
    )


def _wanted_trinket(item: dict) -> bool:
    is_a_good_one = (
        _is_trinket(item)
        # and _is_gte_uncommon(item)
        # and _get_expansion(item) in _get_relevant_expansions()
        or _is_wanted(item)
    )

    return is_a_good_one


def _get_id_encounter(item_id: int, encounter_items: dict) -> typing.Optional[int]:
    if encounter_item := encounter_items.get(item_id):
        return int(encounter_item[0]["id_encounter"])
    return None


def _get_id_journal_instance(
    id_encounter: typing.Optional[int], encounters: dict
) -> typing.Optional[int]:
    if not id_encounter:
        return None
    if encounter := encounters.get(id_encounter):
        return int(encounter[0]["id_journal_instance"])
    return None


def _get_id_map(
    id_journal_instance: typing.Optional[int], instances: dict
) -> typing.Optional[int]:
    if not id_journal_instance:
        return None
    if map := instances.get(id_journal_instance):
        return int(map[0]["map"])
    return None


def _get_instance_type(id_map: int, maps: dict) -> typing.Optional[int]:
    if map := maps.get(id_map):
        return int(map[0]["instance_type"])
    return None


def _is_on_use(item_id: int, itemxitemeffects: dict) -> bool:
    if item_id in itemxitemeffects:
        return any([row["trigger_type"] == 0 for row in itemxitemeffects[item_id]])
    return False


def _create_id_dict_from_table(table: typing.List[dict], column: str = "id") -> dict:
    """Create a new dictionary containing all rows, but now associated by the declared column value.

    Args:
        table (typing.List[dict]): [{"example": "hello"}, {"example", "world"}]
        column (str): _description_

    Returns:
        dict: {"hello": [{"example": "hello"}], "world": [{"example", "world"}]}
    """
    id_dict = {}
    for row in table:
        if row[column] and row[column] not in id_dict:
            id_dict[row[column]] = [row]
        elif row[column] and row[column] in id_dict:
            id_dict[row[column]].append(row)

    return id_dict


class TrinketExtractor(Extractor):
    @property
    def tables(self) -> typing.List[str]:
        return [
            "ItemSparse",
            "ItemXItemEffect",
            "ItemEffect",
            "JournalEncounterItem",
            "JournalEncounter",
            "JournalInstance",
            "Map",
        ]

    def combine_into_json(self, data: typing.Dict[str, LOCALE_TABLES]) -> None:
        logger.info("Starting to create dictionaries.")
        logger.info("id_dict: ItemEffect")
        itemeffects = _create_id_dict_from_table(data["ItemEffect"][US], "id")

        logger.info("id_dict: special handling ItemXItemEffect")
        # _itemxitemeffects = _create_id_dict_from_table(
        #     data["ItemXItemEffect"][US], "id_parent"
        # )
        itemxitemeffects: typing.Dict[int, typing.List[typing.Dict]] = {}
        for effect in data["ItemXItemEffect"][US]:
            if isinstance(effect["id_parent"], int):
                if effect["id_parent"] in itemxitemeffects:
                    itemxitemeffects[effect["id_parent"]].append(
                        itemeffects.get(effect["id_item_effect"], [-1])[0]
                    )
                else:
                    itemxitemeffects[effect["id_parent"]] = [
                        itemeffects.get(effect["id_item_effect"], [-1])[0]
                    ]

        logger.info("id_dict: JournalEncounterItem")
        journal_encounter_items = _create_id_dict_from_table(
            data["JournalEncounterItem"][US], "id_item"
        )
        logger.info("id_dict: JournalEncounter")
        journal_encounters = _create_id_dict_from_table(
            data["JournalEncounter"][US], "id"
        )
        logger.info("id_dict: JournalInstance")
        journal_instances = _create_id_dict_from_table(
            data["JournalInstance"][US], "id"
        )
        logger.info("id_dict: Map")
        maps = _create_id_dict_from_table(data["Map"][US], "id")

        logger.info("Collecting localizations")
        trinkets = collect_localizations(
            data["ItemSparse"], filter_function=_wanted_trinket
        )

        logger.info("Done creating dictionaries. Processing trinkets.")

        for trinket in trinkets:
            trinket["on_use"] = _is_on_use(
                safely_convert_to(trinket["id"], int, -1), itemxitemeffects
            )
            trinket["id_encounter"] = _get_id_encounter(
                safely_convert_to(trinket["id"], int, -1),
                journal_encounter_items,
            )
            trinket["id_journal_instance"] = _get_id_journal_instance(
                safely_convert_to(trinket["id_encounter"], int, -1),
                journal_encounters,
            )
            trinket["id_map"] = _get_id_map(
                safely_convert_to(trinket["id_journal_instance"], int, -1),
                journal_instances,
            )
            trinket["instance_type"] = _get_instance_type(
                safely_convert_to(trinket["id_map"], int, -1),
                maps,
            )

        with open(os.path.join(DATA_PATH, "trinkets.json"), "w", encoding="utf-8") as f:
            json.dump(trinkets, f, ensure_ascii=False)
