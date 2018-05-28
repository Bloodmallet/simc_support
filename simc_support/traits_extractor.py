#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract all traits from simulationcraft and write a file with their content for simc_support"""

import logging
import subprocess
from simc_support import wow_lib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


def main():
  logger.info("Started")

  class_list = wow_lib.get_classes()

  with open("trait_list.txt", "w") as f:
    trait_list = []
    for wow_class in class_list:
      try:
        simc_output = subprocess.run([
          "../../SimulationCraft_BfA/simc.exe",
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
      for line in simc_output.stdout.splitlines():
        logger.info(line)

        if "Name             : " in line:
          new_trait = True
          name = line.split("Name             : ")[1].split(" (id=")[0]

          if name in trait_list:
            new_trait = False
            continue
          else:
            trait_list.append(name)

          spell_id = line.split("Name             : "
                               )[1].split(" (id=")[1].split(") ")[0]

          f.write("  Azerite_Trait(\n")
          f.write("    \"{}\",\n".format(name))

        if "Class            : " in line and new_trait:
          classes_list = line.split("Class            : ")[1].split(", ")
          f.write("    [\n")
          for trait_class in classes_list:
            for spec in wow_lib.get_specs(trait_class.replace(" ", "_")):
              f.write(
                "      (\"{}\", \"{}\"),\n".format(
                  trait_class.replace(" ", "_"), spec
                )
              )
          f.write("    ],\n")
          f.write("    {},\n".format(spell_id))

        if "Azerite Power Id : " in line and new_trait:
          trait_id = line.split("Azerite Power Id : ")[1]

          f.write("    {},\n".format(trait_id))
          f.write("    -1,\n")
          f.write("    -1,\n")
          f.write("    1,\n")

        if "Description      : " in line and new_trait:
          description = line.split("Description      : ")[1]

          f.write("    \"{}\"\n".format(description))

          f.write("  ),\n")
      logger.info("{} unique traits found.".format(len(trait_list)))


if __name__ == '__main__':
  main()
