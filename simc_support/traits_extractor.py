#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract all traits from simulationcraft and write a file with their content for simc_support"""

import json
import logging
import subprocess
from simc_support import wow_lib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


def update_map(trait_dict):

    try:
        with open("trait_map.json", "r") as r:
            LOADED_MAP = json.load(r)
    except Exception as e:
        LOADED_MAP = {}
        logger.error(e)
        logger.error("trait_map.json will be created.")

    updated_map = LOADED_MAP

    # logger.info(updated_map)

    trait_classes = {}
    newly_created = 0

    for wow_class in trait_dict:
        for wow_spec in trait_dict[wow_class]:
            for trait_id in trait_dict[wow_class][wow_spec]:
                if not trait_id in trait_classes:
                    trait_classes[trait_id] = {}
                if not wow_class in trait_classes[trait_id]:
                    trait_classes[trait_id][wow_class] = []
                trait_classes[trait_id][wow_class].append(wow_spec)

    for wow_class in trait_dict:
        for wow_spec in trait_dict[wow_class]:
            for trait_id in trait_dict[wow_class][wow_spec]:
                if not trait_id in updated_map:
                    updated_map[trait_id] = {
                        "name":
                        trait_dict[wow_class][wow_spec][trait_id]["name"],
                        "trait_id": trait_dict[wow_class][wow_spec][trait_id]["trait_id"],
                        "class":
                        trait_classes[trait_id],
                        "description":
                        trait_dict[wow_class][wow_spec][trait_id]["description"],
                        "min_itemlevel":
                        -1,
                        "max_itemlevel":
                        -1,
                        "max_stack":
                        1
                    }

                    newly_created += 1

                else:
                    logger.debug(
                        "Trait {} (id={}) was already found in MAP. Only name and description will be updated.".
                        format(
                            trait_dict[wow_class][wow_spec][trait_id]["name"], trait_id
                        )
                    )
                    updated_map[trait_id]["name"] = trait_dict[wow_class][wow_spec][
                        trait_id
                    ]["name"]
                    updated_map[trait_id]["trait_id"] = trait_dict[wow_class][wow_spec][
                        trait_id
                    ]["trait_id"]
                    updated_map[trait_id]["description"] = trait_dict[wow_class][
                        wow_spec
                    ][trait_id]["description"]
                    # add wow_class if class wasn't present before
                    if not wow_class in updated_map[trait_id]["class"]:
                        logger.info(
                            "Class {} was added to trait {} (id={}) in MAP. If you want to disable a trait, delete only the specs from MAP.".
                            format(
                                wow_class, trait_dict[wow_class][wow_spec][trait_id]["name"],
                                trait_id
                            )
                        )
                        updated_map[trait_id]["class"][wow_class] = trait_classes[
                            trait_id
                        ][wow_class]

                    # delete old class if class is no longer in the list of the trait
                    to_delete_list = []
                    for check_class in updated_map[trait_id]["class"]:
                        if not check_class in trait_classes[trait_id]:
                            logger.warning(
                                "Trait {} (id={}) lost class {}.".format(
                                    updated_map[trait_id]["name"], trait_id, check_class
                                )
                            )
                            to_delete_list.append(check_class)
                    for to_delete in to_delete_list:
                        updated_map[trait_id]["class"].pop(to_delete)

    with open("trait_map.json", "w") as f:
        f.write(json.dumps(updated_map, sort_keys=True, indent=4))

    if newly_created:
        logger.info("Added {} entries to MAP.".format(newly_created))
    else:
        logger.info(
            "All traits were already known. No new traits were added to MAP."
        )


def update_list(trait_dict):
    try:
        with open("trait_map.json", "r") as r:
            LOADED_MAP = json.load(r)
    except Exception as e:
        LOADED_MAP = {}
        logger.error(e)

    trait_classes = {}
    for wow_class in wow_lib.get_classes():
        trait_classes[wow_class] = {}
        for wow_spec in wow_lib.get_specs(wow_class):
            trait_classes[wow_class][wow_spec] = {}

            for trait_id in trait_dict[wow_class][wow_spec]:
                try:
                    # if trait is in map for the spec
                    if wow_spec in LOADED_MAP[trait_id]["class"][wow_class]:
                        trait_classes[wow_class][wow_spec][trait_id] = {
                            "name":
                            trait_dict[wow_class][wow_spec][trait_id]["name"],
                            "description":
                            trait_dict[wow_class][wow_spec][trait_id]["description"],
                            "max_itemlevel":
                            LOADED_MAP[trait_id]["max_itemlevel"],
                            "max_stack":
                            LOADED_MAP[trait_id]["max_stack"],
                            "min_itemlevel":
                            LOADED_MAP[trait_id]["min_itemlevel"],
                            "spell_id":
                            trait_dict[wow_class][wow_spec][trait_id]["spell_id"],
                            "trait_id":
                            trait_dict[wow_class][wow_spec][trait_id]["trait_id"]
                        }
                except KeyError:
                    logger.error(
                        "Class {} for trait {} (id={}) wasn't in MAP. Try updating MAP first.".
                        format(
                            wow_class, trait_dict[wow_class][wow_spec][trait_id]["name"],
                            trait_id
                        )
                    )

    with open("trait_list.json", "w") as f:
        f.write(json.dumps(trait_classes, sort_keys=True, indent=4))


def main():
    logger.info("Started")

    class_list = wow_lib.get_classes()

    trait_list = []
    trait_dict = {}
    # prepare dict with all specs
    for wow_class in class_list:
        trait_dict[wow_class] = {}
        for spec in wow_lib.get_specs(wow_class):
            trait_dict[wow_class][spec] = {}

    for wow_class in class_list:
        try:
            simc_output = subprocess.run([
                "../../SimulationCraft/simc.exe",
                "spell_query=azerite.class={}".format(
                    wow_class.lower().replace("_", "")
                )
            ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True)
        except Exception as e:
            logger.info("{} failed to load. {}".format(wow_class, e))
            continue

        logger.info(wow_class)

        new_trait = True
        trait_name = ""
        trait_spell_id = -1
        trait_id = -1
        trait_description = ""
        trait_specs = []

        for line in simc_output.stdout.splitlines():
            # logger.info(line)

            if "Name             : " in line:
                trait_name = line.split(
                    "Name             : ")[1].split(" (id=")[0]
                trait_spell_id = line.split("Name             : "
                                            )[1].split(" (id=")[1].split(") ")[0]

                if trait_name in trait_list:
                    new_trait = False
                else:
                    new_trait = True
                    trait_list.append(trait_name)

            if "Class            : " in line and new_trait:
                trait_classes = line.split("Class            : ")[
                    1].split(", ")
                trait_specs = []
                for trait_class in trait_classes:
                    for spec in wow_lib.get_specs(trait_class.replace(" ", "_")):
                        trait_specs.append(
                            (trait_class.replace(" ", "_"), spec))

            if "Azerite Power Id : " in line and new_trait:
                trait_id = line.split("Azerite Power Id : ")[1]

            if "Description      : " in line and new_trait:
                trait_description = line.split("Description      : ")[1]

                for spec in trait_specs:

                    trait_dict[spec[0]][spec[1]][trait_spell_id] = {}
                    trait_dict[spec[0]][spec[1]
                                        ][trait_spell_id]["name"] = trait_name
                    trait_dict[spec[0]][spec[1]][trait_spell_id]["spell_id"
                                                                 ] = trait_spell_id
                    trait_dict[spec[0]][spec[1]
                                        ][trait_spell_id]["trait_id"] = trait_id
                    trait_dict[spec[0]][spec[1]
                                        ][trait_spell_id]["min_itemlevel"] = -1
                    trait_dict[spec[0]][spec[1]
                                        ][trait_spell_id]["max_itemlevel"] = -1
                    trait_dict[spec[0]][spec[1]
                                        ][trait_spell_id]["max_stack"] = 1
                    trait_dict[spec[0]][spec[1]][trait_spell_id]["description"
                                                                 ] = trait_description

        logger.info("{} unique traits found.".format(len(trait_list)))

    update_map(trait_dict)
    update_list(trait_dict)


if __name__ == '__main__':
    main()
