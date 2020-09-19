import unittest

from simc_support.game_data.SoulBind import SOULBINDS
from simc_support.game_data.SoulBind import SoulBind
from simc_support.game_data.SoulBind import get_soul_bind


class TestSoulBind(unittest.TestCase):
    def test_non_empty(self):
        self.assertTrue(len(SOULBINDS) > 0)

    def test_known_count(self):
        self.assertTrue(len(SOULBINDS) == 4 * 3)


class TestGetSoulBind(unittest.TestCase):
    def setUp(self) -> None:
        self.mikanikos = "Forgelite Prime Mikanikos"

    def test_return_type(self):
        self.assertTrue(isinstance(get_soul_bind(name=self.mikanikos), SoulBind))

    def test_return_value(self):
        self.assertTrue(get_soul_bind(name=self.mikanikos).full_name == self.mikanikos)
