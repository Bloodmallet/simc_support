# -*- coding: utf-8 -*-

from simc_support import wow_lib

def print_simc_file(trinket_list, name):
  with open("trinkets_" + name + ".simc", 'w') as f:
    for trinket in trinket_list:
      t_name, t_id, _, t_ilevel, _ = trinket
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
