import unittest

from simc_support.game_data.Covenant import COVENANTS
from simc_support.game_data.Covenant import Covenant
from simc_support.game_data.Covenant import get_covenant


class TestCovenants(unittest.TestCase):
    def test_non_empty(self):
        self.assertTrue(len(COVENANTS) > 0)

    def test_known_count(self):
        self.assertTrue(len(COVENANTS) == 4)


class TestGetCovenant(unittest.TestCase):
    def setUp(self) -> None:
        self.kyrian = "Kyrian"
        self.night_fae = "Night Fae"

    def test_return_type(self):
        self.assertTrue(isinstance(get_covenant(name=self.kyrian), Covenant))
        self.assertTrue(isinstance(get_covenant(name=self.night_fae), Covenant))

    def test_return_value(self):
        self.assertTrue(get_covenant(name=self.night_fae).full_name == self.night_fae)
