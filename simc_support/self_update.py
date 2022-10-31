"""
This script updates data_files by using SimulationCrafts casc and dbc extractors.
Basically; execute this script once per patch.

e.g. python self_update.py -s ../../simulationcraft/ --beta --no-load --no-extract
"""
import json
import logging
import os
import typing
from .update.extractor import Extractor
from .update.utils import (
    ArgsObject,
    handle_arguments,
    dbc,
    casc,
    get_compiled_data_path,
    collect_localizations,
    safely_convert_to,
)
from .update.talents import TalentLoader
from .update.trinkets import TrinketExtractor


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

fh = logging.FileHandler("debug.log", encoding="utf-8", mode="w")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

_LOCALES = [
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

DATA_PATH = "simc_support/game_data/data_files"


def update_wow_classes(args: ArgsObject) -> None:
    logger.info("Update WowClasses")

    # TODO: class - race connection can be established via ChrClassRaceSex table
    CHRCLASSES = "ChrClasses"
    dbc(
        args,
        [
            CHRCLASSES,
        ],
    )
    data = {}

    for locale in _LOCALES:
        with open(
            os.path.join(get_compiled_data_path(args, locale), f"{CHRCLASSES}.json"),
            "r",
        ) as f:
            data[locale] = json.load(f)

    wow_classes = []

    wow_classes = collect_localizations(data, translation_field="name_lang")

    with open(os.path.join(DATA_PATH, "wow_classes.json"), "w", encoding="utf-8") as f:
        json.dump(wow_classes, f, ensure_ascii=False)

    logger.info(f"Updated {len(wow_classes)} WowClasses")


def update_legendaries(args: ArgsObject) -> None:
    logger.info("Update legendaries")

    RUNEFORGELEGENDARYABILITY = "RuneforgeLegendaryAbility"
    SPECSETMEMBER = "SpecSetMember"

    dbc(
        args,
        [
            RUNEFORGELEGENDARYABILITY,
            SPECSETMEMBER,
        ],
    )
    data = {
        RUNEFORGELEGENDARYABILITY: {},
        SPECSETMEMBER: {},
    }
    for key in data:
        for locale in _LOCALES:
            with open(
                os.path.join(get_compiled_data_path(args, locale), f"{key}.json"),
                "r",
            ) as f:
                data[key][locale] = json.load(f)

    legendaries = collect_localizations(data[RUNEFORGELEGENDARYABILITY])
    specs = data[SPECSETMEMBER][_LOCALES[0]]

    for legendary in legendaries:

        legendary["spec_ids"] = list(
            [
                safely_convert_to(spec["id_spec"], int, -1)
                for spec in specs
                if spec["id_parent"] == legendary["id_spec_set"]
            ]
        )

    with open(os.path.join(DATA_PATH, "legendaries.json"), "w", encoding="utf-8") as f:
        json.dump(legendaries, f, ensure_ascii=False)

    logger.info(f"Updated {len(legendaries)} legendaries")


def main() -> None:
    args = handle_arguments()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    casc(args)

    updates: typing.List[typing.Callable[[ArgsObject], None]] = [
        # update_trinkets,
        # update_wow_classes,
        # update_legendaries,
    ]
    for update in updates:
        update(args)

    extractors: typing.List[typing.Type[Extractor]] = [
        TalentLoader,
        TrinketExtractor,
    ]
    for extractor in extractors:
        extractor(args).extract()

    logger.debug("self_update done")


if __name__ == "__main__":
    main()
