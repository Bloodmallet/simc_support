"""File contains an interface to get wow data.
"""

import json
import pkg_resources

from simc_support.game_data import Source
from simc_support.game_data.ItemLevel import *  # pylint: disable=unused-wildcard-import
from simc_support.game_data.Race import RACES as __races
from simc_support.game_data.Trinket import Trinket
from simc_support.game_data.Trinket import trinket_list as __trinket_list
from simc_support.game_data.WowClass import class_data as __class_data


def _compare_trinket_lists():
    path = "equippable-items.json"

    with open(
        pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
    ) as f:

        loaded_items = json.load(f, encoding="UTF-8")

    # compare from wow data to local list
    print("Searching through equippable-items.json:")
    missing = 0
    for item in loaded_items:
        if item["inventoryType"] == 12 and item["itemLevel"] >= 280:
            found = False
            for trinket in __trinket_list:
                if trinket.get_name() == item["name"]:
                    found = True

            if not found:
                missing += 1
                print(f"  {item['name']} not found in local list! id: {item['id']}")
    if missing:
        print(f"{missing} trinkets are missing.\n")

    print("Searching through local trinkets:")
    for trinket in __trinket_list:
        found = False

        for item in loaded_items:
            if int(trinket.get_id()) == int(item["id"]):
                found = True

        if not found:
            print(
                f"  {trinket.get_name()} not found in equippable-items.json! id: {trinket.get_id()}"
            )


def get_trinket_list() -> list:
    """Get a full trinket list for the ongoing expansion from equippable-items.json.

    Returns:
        list -- item list
    """

    path = "equippable-items.json"

    with open(
        pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
    ) as f:

        loaded_items = json.load(f, encoding="UTF-8")

    item_list: list = []

    for item in loaded_items:
        if item["inventoryType"] == 12 and item["itemLevel"] >= 280:
            item_list.append(item)

    return item_list


def get_trinket_translation(trinket_name) -> dict:
    """Returns the translation dict for a trinket

    Arguments:
        trinket_name {[type]} -- [description]

    Returns:
        dict -- [description]
    """
    path = "trinket_translations.json"

    with open(
        pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
    ) as f:

        loaded_items = json.load(f, encoding="UTF-8")

    try:
        return loaded_items[trinket_name]
    except Exception as e:
        raise LookupError("Translation not found for {}. {}".format(trinket_name, e))


def get_talent_blueprint(wow_class: str, wow_spec: str) -> str:
    """Returns a talent blueprint for the wow_class. 0 means non-dps relevant talents. 1 means dps relevant talent.

    Arguments:
        wow_class {string} -- [description]

    Keyword Arguments:
        wow_spec {str} -- [description] (default: {""})

    Returns:
        string -- 7 digits decsribing possible talent combinations. 0...non dps talent, 1...dps-talent
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["talents"]


def get_azerite_item_translation(item_name) -> dict:
    """Returns the translation dict for a trinket

    Arguments:
        trinket_name {[type]} -- [description]

    Returns:
        dict -- [description]
    """

    path = "azerite_item_translations.json"

    with open(
        pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
    ) as f:

        loaded_items = json.load(f, encoding="UTF-8")

    try:
        return loaded_items[item_name]
    except Exception as e:
        raise LookupError("Translation not found for {}. {}".format(item_name, e))


def get_item_translation(
    item_name: str = "", item_id: int = None, item_list: list = None
) -> dict:
    """Get the translation dictionary for an item. If item_list is provided, the lookup time is quicker.

    Keyword Arguments:
        item_name {str} -- English name of the Item (default: {""})
        item_id {int} -- Item ID (default: {None})
        item_list {list} -- item_list, can be generated with get_trinket_list() (default: {None})

    Raises:
        LookupError -- If no translation is found in data

    Returns:
        dict -- {language_shorthand: translation}
    """

    if item_list:
        loaded_items = item_list

    else:
        path = "equippable-items.json"

        with open(
            pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
        ) as f:

            loaded_items = json.load(f, encoding="UTF-8")

    for item in loaded_items:
        if item_name and item_name == item["name"]:
            return item["names"]
        elif item_id and int(item_id) == item["id"]:
            return item["names"]

    raise LookupError("Translation not found for {}{}".format(item_name, item_id))


def get_trait_translation_dict():
    """Return the dict of all azerite trait translations.

    Returns:
        dict -- {Name:{language:translation}}
    """

    path = "azerite_trait_translations.json"

    with open(
        pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
    ) as f:

        loaded_translations = json.load(f, encoding="UTF-8")

    return loaded_translations


def get_trait_translation(trait_name: str = "", translation_dict: dict = None) -> dict:
    """Return the translation dict of one trait. Providing the translation_dict speeds up the process.

    Keyword Arguments:
        trait_name {str} -- [description] (default: {""})
        translation_dict {dict} -- [description] (default: {None})

    Raises:
        LookupError -- [description]

    Returns:
        dict -- [description]
    """

    if translation_dict:
        loaded_translations = translation_dict
    else:
        path = "azerite_trait_translations.json"

        with open(
            pkg_resources.resource_filename(__name__, path), "r", encoding="UTF-8"
        ) as f:

            loaded_translations = json.load(f, encoding="UTF-8")

    try:
        return loaded_translations[trait_name]
    except Exception:
        for name in loaded_translations:
            if name in trait_name:
                try:
                    return loaded_translations[name]
                except Exception:
                    raise LookupError("Translation not found for {}".format(trait_name))
