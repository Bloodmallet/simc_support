"""File contains an interface to get wow data.
"""

import json

from .game_data import Source
from .game_data.AzeriteEssence import essences as __essences
from .game_data.AzeriteItem import itemlevel_dict as __azerite_item_max_level
from .game_data.ItemLevel import *     # pylint: disable=unused-wildcard-import
from .game_data.Race import races as __races
from .game_data.Race import translations as __race_translations
from .game_data.Trinket import Trinket
from .game_data.Trinket import trinket_list as __trinket_list
from .game_data.WowClass import class_data as __class_data


def is_melee(wow_class, wow_spec):
    """True if spec is melee spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if role of the spec is 'melee'.
    """

    return get_role(wow_class, wow_spec) == "melee"


def is_ranged(wow_class, wow_spec):
    """True if spec is a ranged spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if role of the spec is 'ranged'.
    """

    return get_role(wow_class, wow_spec) == "ranged"


def get_mask_for_spec(wow_class, wow_spec):
    """Mask to get appropriate Trinkets.

    Arguments:
      wow_class {str} -- world of warcraft class name
      wow_spec {str} -- world of warcraft spec name

    Returns:
      tuple(main_stat_agi{bool}, main_stat_int{bool}, main_stat_str{bool}, melee{bool}, ranged{bool} ) -- Returns a bool tuple mask to match the True's with Trinket
    """

    melee = is_melee(wow_class, wow_spec)
    ranged = is_ranged(wow_class, wow_spec)
    main_stat = get_main_stat(wow_class, wow_spec)
    main_stat_agi = main_stat == "agi"
    main_stat_int = main_stat == "int"
    main_stat_str = main_stat == "str"

    return (main_stat_agi, main_stat_int, main_stat_str, melee, ranged)


def _compare_trinket_lists():
    import pkg_resources

    path = "equippable-items.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    # compare from wow data to local list
    print("Searching through equippable-items.json:")
    missing = 0
    for item in loaded_items:
        if item["inventoryType"] == 12 and item["itemLevel"] >= EXPANSION_START_ITEMLEVEL:
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
            print(f"  {trinket.get_name()} not found in equippable-items.json! id: {trinket.get_id()}")


def get_trinkets_for_spec(wow_class: str, wow_spec: str) -> list:
    """New function to return all available trinkets for a spec

    Arguments:
      wow_class {str} -- name of the wow class
      wow_spec {str} -- name of the wow spec

    Returns:
      list[Trinket] -- List of all Trinkets
    """

    agility, intellect, strength, melee, ranged = get_mask_for_spec(wow_class, wow_spec)
    return_list = []
    for trinket in __trinket_list:
        if melee and trinket.melee:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel, trinket.max_itemlevel,
                trinket.max_itemlevel_drop, trinket.active
            ))
        elif ranged and trinket.ranged:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel, trinket.max_itemlevel,
                trinket.max_itemlevel_drop, trinket.active
            ))
        elif agility and trinket.agility:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel, trinket.max_itemlevel,
                trinket.max_itemlevel_drop, trinket.active
            ))
        elif intellect and trinket.intellect:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel, trinket.max_itemlevel,
                trinket.max_itemlevel_drop, trinket.active
            ))
        elif strength and trinket.strength:
            return_list.append((
                trinket.name, trinket.item_id, trinket.min_itemlevel, trinket.max_itemlevel,
                trinket.max_itemlevel_drop, trinket.active
            ))
    return return_list


def get_race_translation(race: str) -> dict:
    """Return the translation dict for a race.

    Arguments:
        race {str} -- wow race

    Returns:
        dict -- [description]
    """

    try:
        return __race_translations[race.lower().replace(" ", "_")]
    except Exception:
        return None


def get_trinket_list() -> list:
    """Get a full trinket list for the ongoing expansion from equippable-items.json.

    Returns:
        list -- item list
    """

    import pkg_resources

    path = "equippable-items.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

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

    import pkg_resources

    path = "trinket_translations.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

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

    import pkg_resources

    path = "azerite_item_translations.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    try:
        return loaded_items[item_name]
    except Exception as e:
        raise LookupError("Translation not found for {}. {}".format(item_name, e))


def get_item_translation(item_name: str = "", item_id: int = None, item_list: list = None) -> dict:
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
        import pkg_resources

        path = "equippable-items.json"

        with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

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

    import pkg_resources

    path = "azerite_trait_translations.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

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
        import pkg_resources

        path = "azerite_trait_translations.json"

        with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

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


def get_second_trinket_for_spec(wow_class, wow_spec):
    """Returns a vers stat stick for the spec.

    Arguments:
        wow_class {[type]} -- [description]
        wow_spec {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    main_stat = get_main_stat(wow_class, wow_spec)
    if main_stat == "agi":
        # "Stat Stick (Versatility)", "142506,bonus_id=607"
        return ',id={}'.format("142506,bonus_id=607")
    if main_stat == "int":
        # "Stat Stick (Versatility)", "142507,bonus_id=607"
        return ',id={}'.format("142507,bonus_id=607")
    if main_stat == "str":
        # "Stat Stick (Versatility)", "142508,bonus_id=607"
        return ',id={}'.format("142508,bonus_id=607")


def get_trinket_id(trinket_name):
    """Return the trinket id as string. Function can handly extended names like 'Pancakes Specialtext' and will still return the ID of 'Pancakes' in this case.

    Arguments:
      trinket_name {str} -- trinket name

    Returns:
      str -- item ID as string
    """

    for trinket in __trinket_list:
        # ordered like this to allows look ups of extended names like "Norgannons + 15" to yield an ID
        if trinket.name in trinket_name:
            return trinket.item_id


def get_trinket(name: str = "", item_id: str = "") -> Trinket:
    """Return Trinket of matching name or item_id. One must be provided. Else None will be returned.

    Keyword Arguments:
      name {str} -- name of the trinket (default: {""})
      item_id {str} -- id of the trinket (default: {""})

    Returns:
      Trinket or None -- Instance of Trinket class
    """

    if name or item_id:
        for trinket in __trinket_list:
            if trinket.name == name or trinket.item_id == item_id:
                return trinket
    return None


def get_azerite_traits(wow_class: str, wow_spec: str) -> dict:
    """Get all azerite traits for the given wow class and spec.

    Arguments:
        wow_class {str} -- [description]
        wow_spec {str} -- [description]

    Raises:
        e -- [description]

    Returns:
        dict -- Dict{spell_id: str : Dict{description: str : str, max_itemlevel: str : int, max_stack: str : int, min_itemlevel: str : int, name: str : str, spell_id: str : str, trait_id: str : str}}
    """

    import pkg_resources

    path = "azerite_trait_list.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:
        traits = json.load(f, encoding="UTF-8")

    try:
        return traits[wow_class.title()][wow_spec.title()]
    except Exception as e:
        raise e


def get_azerite_items(wow_class: str, wow_spec: str) -> dict:
    """Return a dictionary of all azerite items for the given spec. Dictionary is organized by item slot. Items have all available traits for them, too.

    REQUIRED: 'equippable-items-live.json' and 'azerite-power-sets-live.json'
    https://www.raidbots.com/static/data/live/azerite-power-sets.json
    https://www.raidbots.com/static/data/live/equippable-items.json

    "head": [item, item, ...],
    "shoulders": [item, item, ...],
    "chest": [item, item, ...]

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      dictionary -- all available azerite items for the given spec
    """

    import pkg_resources

    path = "equippable-items.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:

        loaded_items = json.load(f, encoding="UTF-8")

    items: dict = {"head": [], "shoulders": [], "chest": []}
    item_type = {
        1: "head",
        3: "shoulders",
        5: "chest",     # ???
        20: "chest"     # ???
    }

    for item in loaded_items:
        if "azeritePowerSetId" in item:

            try:
                items[item_type[item["inventoryType"]]].append(item)
            except Exception:
                pass

    # enrich dict with azerite traits
    path = "azerite-power-sets.json"

    with open(pkg_resources.resource_filename(__name__, path), 'r', encoding="UTF-8") as f:
        azerite_traits = json.load(f, encoding="UTF-8")

    for slot in items:
        for i in range(len(items[slot])):
            item = items[slot][i]
            try:
                items[slot][i]["azeriteTraits"] = azerite_traits[str(items[slot][i]["azeritePowerSetId"])]
            except Exception:     # as e:
                # logger.error(e)
                # logger.error("slot: {}".format(slot))
                # logger.error("item: {}".format(item))
                # logger.error("item data: {}".format(items[slot][i]))
                # logger.error("azeritePowerSetId: {}".format(items[slot][i]["azeritePowerSetId"]))
                # logger.error(trait_dict[str(items[slot][i]["azeritePowerSetId"])])
                pass

    # create a new itemlist with only items for the wow spec/class
    response: dict = {}
    class_id = get_class_id(wow_class)
    spec_id = get_spec_id(wow_class, wow_spec)     # unused...for now

    for slot in items:
        # create slot in new dict
        if not slot in response:
            response[slot] = []

        for item in items[slot]:
            new_trait_list = []

            for trait in item["azeriteTraits"]:
                if trait["classId"] == class_id and (trait["specUsable"] == [] or spec_id in trait["specUsable"]):
                    new_trait_list.append(trait)

            item["azeriteTraits"] = new_trait_list

            if item["azeriteTraits"]:
                # add item only to the response if it has traits for the givesn class/spec
                response[slot].append(item)

    return response


def get_azerite_tiers(wow_class: str, wow_spec: str, trait_id: str) -> int:
    """Get the tier number of an azerite trait.

    Arguments:
        wow_class {str} -- [description]
        wow_spec {str} -- [description]
        trait_id {str} -- [description]

    Returns:
        int -- [description]
    """

    traits = get_azerite_traits(wow_class, wow_spec)

    return traits[trait_id]["tiers"]


def get_azerite_trait_max_ilevel(wow_class: str, wow_spec, trait_id: str) -> int:

    traits = get_azerite_traits(wow_class, wow_spec)

    try:
        ilvl: int = traits[trait_id]['max_itemlevel']
    except Exception:
        ilvl = -1

    if ilvl == -1:
        ilvl = TITANFORGE_CAP - 10

    return ilvl


def get_all_trinkets():
    """Get a list of all known trinket names.

    Returns:
      list[trinket_name{str}] -- List of all trinket names.
    """

    all_trinkets = []
    for trinket in __trinket_list:
        all_trinkets.append(trinket.name)
    return all_trinkets


def get_talent_dict(wow_class: str, wow_spec: str, ptr: bool = False) -> dict:
    """Return the dict of all talents available to this spec. Structur: row -> column -> name, spell_id

    Arguments:
        wow_class {str} -- [description]
        wow_spec {str} -- [description]

    Returns:
        dict -- row -> column -> name, spell_id
    """
    import pkg_resources

    file_name = "talent_list.json"
    if ptr:
        file_name = "talent_list_ptr.json"

    with open(pkg_resources.resource_filename(__name__, file_name), 'r', encoding="UTF-8") as f:
        talents = json.load(f, encoding="UTF-8")

    return talents[wow_class.title()][wow_spec.title()]


def __generate_talent_combinations(blueprint, wow_class, wow_spec):
    """Generate all talent combinations matching blueprint. You're an enduser? Use get_talent_combinations(...).

    Arguments:
      blueprint {str} -- [description]
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      list[talent_combination{str}] -- [description]
    """

    if not ("x" in blueprint or "-" in blueprint):
        return [blueprint]
    data_talents = get_dps_talents(wow_class, wow_spec)
    pattern = ""

    for i in range(0, 7):
        if (blueprint[i] == "-" or blueprint[i] == "x") and data_talents[i] == "0":
            pattern += "0"
        else:
            pattern += blueprint[i]

    combinations = []
    for first in range(4):
        for second in range(4):
            for third in range(4):
                for forth in range(4):
                    for fivth in range(4):
                        for sixth in range(4):
                            for seventh in range(4):
                                combination = str(first) + str(second) + str(third) + str(forth) + str(fivth) + str(
                                    sixth
                                ) + str(seventh)
                                add_it = True

                                # check whether the generated talent combination fits the wanted blueprint
                                for i in range(7):
                                    if (not (pattern[i] == "-" or
                                             pattern[i] == "x")) and not combination[i] == pattern[i]:
                                        add_it = False
                                    if combination[i] == "0" and (pattern[i] == "-" or pattern[i] == "x"):
                                        add_it = False
                                if add_it:
                                    combinations += [combination]

    return combinations


def is_talent_combination(talent_combination):
    """Check the talent_combination for valid format.

    Arguments:
      talent_combination {str} -- [description]

    Returns:
      bool -- True, if the format matches the required format of get_talent_combinations
    """

    if talent_combination == None:
        return False
    if not type(talent_combination) is str:
        return False
    if talent_combination == "":
        return True
    if len(talent_combination) == 7:
        for letter in talent_combination:
            if not (
                letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "-" or letter == "x"
            ):
                return False
        return True
    elif len(talent_combination) == 2:
        for letter in talent_combination:
            if not (letter == "0" or letter == "1" or letter == "2" or letter == "3"):
                return False
        return True
    # Would've been for talent combinations that set certain rows to a value without declaring anything else.
    # Like 42 would set the forth row to the second talent. 4253 would set 4. row to 2 and 5. to 3
    # elif len(talent_combination) % 2 == 0:
    #  for i in range(0, len(talent_combination)):
    #    if (i + 1) % 2 == 1 and not int(talent_combination[i]) in range(1,8):
    #      return False
    #    elif not int(talent_combination[i]) in range(0,4):
    #      return False
    #  return True
    else:
        return False


def get_talent_combinations(wow_class, wow_spec, user_input=""):
    """Get a list of all valid dps talent combinations for a wow_class and wow_spec. If user_input is given the provided mask is used for this genertion and pruning of the talent combination list.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Keyword Arguments:
      user_input {str} -- Mask to determine whether a combination is valid or not. Class inherent masks are used in addition to the user input. Input can either be empty, of len 2 or len 7. len two is understood as a mask for the last two valid dps rows. len seven is understood as a mask for all talent rows. Write 'x' or '-' as a placeholder. Example: '201xx03' will generate 9 talent combinations if both x are dps talents. (default: {""})

    Returns:
      list[talent_combination{str}] -- List of all valied talent combinations for a class.
    """

    combinations = []

    if user_input == "" or user_input == None:
        combinations = __generate_talent_combinations(
            "xxxxxxx",
            wow_class,
            wow_spec,
        )

    elif len(user_input) == 2:
        combinations = __generate_talent_combinations(
            "xxxxx" + user_input,
            wow_class,
            wow_spec,
        )

    elif len(user_input) == 7:
        combinations = __generate_talent_combinations(
            user_input,
            wow_class,
            wow_spec,
        )

    else:
        # something unexpected occured
        return None

    return combinations


def get_classes():
    """Get a list of all wow classes.

    Returns:
      list[wow_class_name{str}] -- List of all wow class names.
    """

    classes = []
    for wow_class in __class_data:
        classes.append(wow_class)
    return classes


def get_classes_specs():
    """Get a list of all wow classes and wow specs.

    Returns:
      List[Tuple(String, String)] -- List of all wow_class and wow_spec combinations
    """

    class_list = get_classes()
    full_list = []
    for wow_class in class_list:
        for spec in get_specs(wow_class):
            full_list.append((wow_class, spec))
    return full_list


def get_races() -> list:
    """Get a list of all wow race names.

    Returns:
      list[wow_race_name{str}] -- List of all wow race names
    """

    races: list = []
    for faction in __races.keys():
        for race in __races[faction].keys():
            if not race in races:
                races.append(race)
    return races


def get_races_for_class(wow_class: str) -> list:
    """Get a list of all available races to the given wow_class.

    Arguments:
      wow_class {str} -- wow class name

    Returns:
      list[wow_race_name{str}] -- List of all available races to the given wow_class.
    """

    race_list: list = []
    for faction in __races.keys():
        for race in __races[faction].keys():
            # additionally prevent double races like pandaren
            if str(wow_class).lower() in __races[faction][race] and not race in race_list:
                race_list.append(race)
    return race_list


def get_role(wow_class: str, wow_spec: str) -> str:
    """Get the role of the given wow class and wow spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      str -- role ('ranged'/'melee')
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["role"]     # type: ignore


def get_class_id(wow_class: str) -> int:
    """Get the wow ID of the given class.

    Arguments:
      wow_class {str} -- [description]

    Returns:
      int -- wow_class_id
    """

    return __class_data[wow_class.title()]["id"]     # type: ignore


def get_spec_id(wow_class: str, wow_spec: str) -> int:
    """Get the ID of a given spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      int -- wow_spec_id
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["id"]     # type: ignore


def get_main_stat(wow_class, wow_spec):
    """Get the main stat of a class and spec.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      str -- main stat (agi / int / str)
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["stat"]


def get_dps_talents(wow_class, wow_spec):
    """Return the dps talent mask for a spec. DPS talents are represented by a '1', non-DPS talent are represented by a '0' (zero).

    Arguments:
      wow_class {str} -- [description]

    Keyword Arguments:
      wow_spec {str} -- wow spec, usually not needed as of Legion. Specs of one class share the same utility rows, not necessarily the talents there,though (default: {""})

    Returns:
      str -- talent mask, e.g. '1011101'
    """

    return __class_data[wow_class.title()]["specs"][wow_spec.title()]["talents"]


def get_specs(wow_class):
    """Get a list of spec names for a given wow class.

    Arguments:
      wow_class {str} -- [description]

    Returns:
      list[wow_spec{str}] -- List of all available wow specs of the wow_class.
    """

    spec_collection = []
    for spec in __class_data[wow_class.title()]["specs"]:
        spec_collection.append(spec)
    return spec_collection


def is_class(wow_class):
    """True, if wow_class is class of WoW.

    Arguments:
      wow_class {str} -- [description]

    Returns:
      boold -- True if wow_class is class of WoW.
    """

    for base_class in get_classes():
        if wow_class.lower() == base_class.lower():
            return True
    return False


def is_race(race):
    """True, if race is a wow race.

    Arguments:
      race {str} -- [description]

    Returns:
      bool -- True, if race is a wow race.
    """

    if race in get_races():
        return True
    return False


def is_spec(wow_spec):
    """True, if wow_spec is a spec in WoW.

    Arguments:
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if wow_spec is a spec in WoW.
    """

    spec_list = []
    classes = get_classes()
    for wow_class in classes:
        specs = get_specs(wow_class)
        for spec in specs:
            spec_list.append(spec)
    for spec in spec_list:
        if wow_spec.lower() == spec.lower():
            return True
    return False


def is_class_spec(wow_class, wow_spec):
    """True, if wow_spec and wow_class match.

    Arguments:
      wow_class {str} -- [description]
      wow_spec {str} -- [description]

    Returns:
      bool -- True, if wow_class and wow_spec match.
    """

    if is_class(wow_class):
        if is_spec(wow_spec):
            for spec in get_specs(wow_class):
                if wow_spec.lower() == spec.lower():
                    return True
    return False


def is_dps_talent_combination(talent_combination, wow_class):
    """Determines whether a given talent combination is a valid talent combination of the wow_class.

    Arguments:
      talent_combination {str} -- [description]
      wow_class {str} -- [description]

    Returns:
      bool -- True, if all dps talent rows have a talent selected and all utility rows have no talent selected.
    """

    for i in range(0, 7):
        if talent_combination[i] == "0" and __class_data[wow_class]["talents"][i] == "1":
            return False
        elif not talent_combination[i] == "0" and __class_data[wow_class]["talents"][i] == "0":
            return False
    return True


def get_essences(wow_class: str, wow_spec: str) -> dict:
    """Returns a dictionary of all available dps essences.

    Returns:
        [type] -- [description]
    """

    essences = {}

    raid_role = __class_data[wow_class]['specs'][wow_spec]['raid_role']

    for key, value in __essences.items():
        if raid_role in value['raid_roles']:
            essences[key] = value

    return essences


def get_essence_power_id(essence_id: int) -> int:
    """Returns powerID of rank 3 of an essence.

    Arguments:
        essence_id {int} -- [description]

    Returns:
        int -- [description]
    """

    import pkg_resources

    file_name = "azerite-essence-power-spell-map.json"

    with open(pkg_resources.resource_filename(__name__, file_name), 'r', encoding="UTF-8") as f:
        essences = json.load(f, encoding="UTF-8")

    return essences[str(essence_id)]["3"]["azeriteEssencePowerId"]


def get_azerite_item_max_itemlevel(item_name: str) -> int:
    """Look up the maximum possible itemlevel for an Azerite Item, or -1.

    Args:
        item_name (str): full name with spaces and special characters

    Returns:
        int: e.g. 380
    """
    try:
        return __azerite_item_max_level[item_name]
    except KeyError:
        return -1
