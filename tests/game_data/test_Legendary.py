import unittest

from simc_support.game_data.Legendary import Legendary
from simc_support.game_data.Legendary import LEGENDARIES


class TestLegendary(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(LEGENDARIES, list))

    def test_non_emptyness(self):
        self.assertTrue(len(LEGENDARIES) > 0)

    def test_content_types(self):
        for legendary in LEGENDARIES:
            with self.subTest(legendary=legendary):
                self.assertTrue(isinstance(legendary, Legendary))
