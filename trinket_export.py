"""Exports trinkets from simc_support to three copy= .simc files for SimulationCraft testing purpose.
"""
import typing
from simc_support.game_data.Season import Season

from simc_support.game_data.WowSpec import get_wow_spec
from simc_support.game_data.Trinket import get_trinkets_for_spec, Trinket

EXPANSION = "dragonflight"


def print_simc_file(trinket_list: typing.Iterable[Trinket], name: str):
    with open(f"trinkets_{EXPANSION}_" + name + ".simc", "w") as f:
        f.write("# PROFILE FOR TESTING ONLY!\n")
        f.write(
            "# This file provides all available trinkets for {} and neutral ones.\n".format(
                name.upper()
            )
        )
        f.write(
            "# Use this file to verify whether all trinkets are functioning as expected after changes.\n"
        )
        f.write("# No appropriate drop itemlevel required.\n\n\n")

        for trinket in trinket_list:
            f.write('copy="{}"\n'.format(trinket.name))
            f.write(
                f"trinket1=,id={trinket.item_id},ilevel={trinket.min_itemlevel}\n\n"
            )


def main():

    trinkets = [
        t
        for t in get_trinkets_for_spec(get_wow_spec("warrior", "arms"))
        if Season.SEASON_1 in t.seasons
    ]
    print_simc_file(trinkets, "str")

    trinkets = [
        t
        for t in get_trinkets_for_spec(get_wow_spec("hunter", "marksmanship"))
        if Season.SEASON_1 in t.seasons
    ]

    print_simc_file(trinkets, "agi")

    trinkets = [
        t
        for t in get_trinkets_for_spec(get_wow_spec("shaman", "elemental"))
        if Season.SEASON_1 in t.seasons
    ]

    print_simc_file(trinkets, "int")


if __name__ == "__main__":
    main()
