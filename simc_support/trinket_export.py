"""Exports trinkets from simc_support to three copy= .simc files for testing purpose.
"""

import wow_lib


def print_simc_file(trinket_list, name):
    with open("trinkets_bfa_" + name + ".simc", 'w') as f:
        f.write("# PROFILE FOR TESTING ONLY!\n")
        f.write("# This file provides all available trinkets for {}s.\n".format(name.upper()))
        f.write("# Use this file to verify whether all trinkets are functioning as expected after changes.\n")
        f.write("# No appropriate drop itemlevel required.\n\n\n")

        for trinket in trinket_list:
            t_name, t_id, _, t_ilevel, _, _ = trinket
            f.write("copy=\"{}\"\n".format(t_name))
            f.write("trinket1=,id={},ilevel={}\n\n".format(t_id, t_ilevel))


def main():

    trinkets = wow_lib.get_trinkets_for_spec("warrior", "arms")
    print_simc_file(trinkets, "melee")

    trinkets = wow_lib.get_trinkets_for_spec("hunter", "marksmanship")
    print_simc_file(trinkets, "hunter")

    trinkets = wow_lib.get_trinkets_for_spec("shaman", "elemental")
    print_simc_file(trinkets, "caster")


if __name__ == '__main__':
    main()
