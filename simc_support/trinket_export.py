"""Exports trinkets from simc_support to three copy= .simc files for testing purpose.
"""
import typing

from simc_support.game_data.WowSpec import get_wow_spec
from simc_support.game_data.Trinket import get_trinkets_for_spec, Trinket


def print_simc_file(trinket_list: typing.List[Trinket], name: str):
    with open("trinkets_shadowlands_" + name + ".simc", "w") as f:
        f.write("# PROFILE FOR TESTING ONLY!\n")
        f.write(
            "# This file provides all available trinkets for {}s.\n".format(
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
                "trinket1=,id={},ilevel={}\n\n".format(
                    trinket.item_id, trinket.min_itemlevel
                )
            )


def main():

    trinkets = get_trinkets_for_spec(get_wow_spec("warrior", "arms"))
    print_simc_file(trinkets, "melee")

    trinkets = get_trinkets_for_spec(get_wow_spec("hunter", "marksmanship"))
    print_simc_file(trinkets, "hunter")

    trinkets = get_trinkets_for_spec(get_wow_spec("shaman", "elemental"))
    print_simc_file(trinkets, "caster")


if __name__ == "__main__":
    main()
