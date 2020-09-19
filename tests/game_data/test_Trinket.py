import unittest

from simc_support.game_data.Stat import Stat
from simc_support.game_data.Trinket import get_versatility_trinket
from simc_support.game_data.Trinket import Trinket
from simc_support.game_data.Trinket import TRINKETS


class TestTrinkets(unittest.TestCase):
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

    def test_for_on_use(self):
        found = False
        for trinket in TRINKETS:
            if trinket.on_use:
                found = True
                break
        self.assertTrue(found)

    def test_for_not_on_use(self):
        found = False
        for trinket in TRINKETS:
            if not trinket.on_use:
                found = True
                break
        self.assertTrue(found)


class TestGetVersatilityTrinket(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(get_versatility_trinket(Stat.STRENGTH), Trinket))

    def test_stats(self):
        for stat in Stat:
            with self.subTest(stat=stat):
                trinket = get_versatility_trinket(stat)
                self.assertTrue(stat in trinket.stats)
