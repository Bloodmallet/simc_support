from simc_support.game_data.Trinket import TRINKETS
from simc_support.game_data.Stat import Stat
import unittest


class Trinkets(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(TRINKETS, list))

    def test_non_emptyness(self):
        self.assertTrue(len(TRINKETS) > 0)

    def test_for_each_primary_stat(self):
        """At least one trinket for each primary stat is available."""
        for stat in Stat:
            with self.subTest(stat=stat):
                found = False
                for trinket in TRINKETS:
                    if stat in trinket.stats:
                        found = True
                        break
                self.assertTrue(found)
