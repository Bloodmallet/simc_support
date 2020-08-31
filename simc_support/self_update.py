"""
This script updates data_files by using SimulationCrafts casc and dbc extractors.
Basically; execute this script once per patch.
"""
import argparse
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

logger.addHandler(ch)


def handle_arguments() -> argparse.ArgumentParser:
    """Scan user provided arguments and provide the corresponding argparse ArgumentParser.

    Returns:
        argparse.ArgumentParser: [description]
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-s",
        "--simc",
        nargs="?",
        default="../SimulationCraft",
        help="Path to your local SimulationCraft version.",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        default="./tmp",
        help="Path to the save location of DB files.",
    )
    parser.add_argument(
        "-w",
        "--wow",
        nargs=1,
        help="Path to your World of Warcaft installation to get hotfixes. E.g. /games/World\ of\ Warcraft/_beta_",
    )
    # parser.add_argument(
    #     "--no-load",
    #     action="store_true",
    #     help="Flag disables download from CDN. Instead only already present local files are used.",
    # )

    return parser


def update_trinkets(args: dict) -> None:

    DB_FILES = ["ItemSparse"]

    WHITELIST = []

    def is_trinket(item: dict) -> bool:
        """See https://github.com/simulationcraft/simc/blob/shadowlands/engine/dbc/data_enums.hh#L335"""
        return item.get("inv_type") == 12

    def is_gte_rare(item: dict) -> bool:
        """See https://github.com/simulationcraft/simc/blob/shadowlands/engine/dbc/data_enums.hh#L369"""
        return item.get("quality") >= 3

    def is_shadowlands(item: dict) -> bool:
        """Tests for itemlevel and chracter level requirement."""
        return is_gte_ilevel(item) and is_gte_level(item)

    def is_gte_level(item: dict) -> bool:
        """An Expansion starts at the last possible character level of the previous one."""
        return item.get("req_level") >= 50

    def is_gte_ilevel(item: dict) -> bool:
        """Value of normal Dungeon items at level 50."""
        return item.get("ilevel") >= 155

    def is_whitelisted(item: dict) -> bool:
        return item.get("id") in WHITELIST

    with open(f"{DB_FILES[0]}.json", "r") as f:
        items = json.load(f)

    trinkets = [
        item
        for item in items
        if is_trinket(item)
        and is_gte_rare(item)
        and is_shadowlands(item)
        or is_whitelisted(item)
    ]

    logger.debug(f"Count: {len(trinkets)}")

    with open("trinkets.json", "w") as f:
        json.dump(trinkets, f)


def main() -> None:
    args = handle_arguments().parse_args()
    logger.info(args)
    # update_trinkets(args)


if __name__ == "__main__":
    main()
