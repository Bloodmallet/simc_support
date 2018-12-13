#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract all traits from seriallos equipable-items and azerite-power-sets files and write a file with their content for simc_support
  Link: https://www.raidbots.com/static/data/equippable-items.json
        https://www.raidbots.com/static/data/azerite-power-sets.json
  Link PTR/Beta: https://www.raidbots.com/static/data/equippable-items-beta.json
                https://www.raidbots.com/static/data/azerite-power-sets-beta.json
"""

import json
import logging
import subprocess
from simc_support import wow_lib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


def load_azerite_items() -> dict:
  """Load all items and creates a dictionary of all azerite items. Return that dictionary. "itemslot": [ items, items ]

  Returns:
    dict -- Items sorted by itemslot
  """

  with open('equippable-items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

  sorted_items = {
    "head": [],
    "shoulders": [],
    "chest": []
  }
  item_type = {
    1: "head",
    3: "shoulders",
    5: "chest", # ???
    20: "chest" # ???
  }

  for item in items:
    if "azeritePowerSetId" in item:
      logger.debug("{} found. Adding.".format(item['name']))

      try:
        sorted_items[item_type[item["inventoryType"]]].append(item)
      except Exception as e:
        logger.error("Adding {} to azerite_items dictionary failed! Data: {} ERROR: {}".format(item['name'], item, e))


  return sorted_items

def load_azerite_traits() -> dict:
  """Load all azerite traits from serialos file.

  Returns:
    dict -- [description]
  """

  with open('azerite-power-sets.json', 'r', encoding='utf-8') as f:
    azerite_traits = json.load(f)

  return azerite_traits


def combine(item_dict: dict, trait_dict: dict) -> dict:
  """Combine the item_dict with trait_dict to have all necessary data to simulate trait combinations from the resulting item dictionary

  Arguments:
    item_dict {dict} -- [description]
    trait_dict {dict} -- [description]

  Returns:
    dict -- [description]
  """

  for slot in item_dict:
    for i in range(len(item_dict[slot])):
      item = item_dict[slot][i]
      try:
        item_dict[slot][i]["azeriteTraits"] = trait_dict[str(item_dict[slot][i]["azeritePowerSetId"])]
      except Exception as e:
        logger.error(e)
        logger.error("slot: {}".format(slot))
        logger.error("item: {}".format(item))
        logger.error("item data: {}".format(item_dict[slot][i]))
        logger.error("azeritePowerSetId: {}".format(item_dict[slot][i]["azeritePowerSetId"]))
        logger.error(trait_dict[str(item_dict[slot][i]["azeritePowerSetId"])])


  return item_dict

def main():
  azerite_items_list = load_azerite_items()
  logger.info(azerite_items_list)
  azerite_traits = load_azerite_traits()

  enriched_azerite_items_list = combine(azerite_items_list, azerite_traits)
  # logger.info(enriched_azerite_items_list)

  with open('azerite_items.json', 'w', encoding='utf-8') as f:
    json.dump(enriched_azerite_items_list, f, indent=2, ensure_ascii=False)



if __name__ == '__main__':
  main()
