from simc_support.game_data.Trinket import TRINKETS
import unittest


class Trinkets(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(TRINKETS, list))

    def test_non_emptyness(self):
        self.assertTrue(len(TRINKETS) > 0)
