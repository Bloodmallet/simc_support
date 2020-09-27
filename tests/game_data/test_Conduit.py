import unittest

from simc_support.game_data.Conduit import Conduit
from simc_support.game_data.Conduit import CONDUITS
from simc_support.game_data.Conduit import get_conduits_for_spec
from simc_support.game_data.WowSpec import get_wow_spec


class TestConduit(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = get_wow_spec("Shaman", "Elemental")
        self.conduits = get_conduits_for_spec(self.spec)

    def test_type(self):
        self.assertTrue(isinstance(CONDUITS, list))

    def test_non_emptyness(self):
        self.assertTrue(len(CONDUITS) > 0)

    def test_content_types(self):
        for conduit in CONDUITS:
            with self.subTest(conduit=conduit):
                self.assertTrue(isinstance(conduit, Conduit))

    def test_get_conduits_for_spec_existence(self):
        self.assertTrue(len(self.conduits) > 0)

    def test_get_conduits_for_spec_type(self):
        self.assertTrue(isinstance(self.conduits, tuple))

    def test_get_conduits_for_spec_types(self):
        self.assertTrue(
            all([isinstance(conduit, Conduit) for conduit in self.conduits])
        )

    def test_has_finesse(self):
        self.assertTrue(any([conduit.is_finesse for conduit in CONDUITS]))

    def test_has_potency(self):
        self.assertTrue(any([conduit.is_potency for conduit in CONDUITS]))

    def test_has_endurance(self):
        self.assertTrue(any([conduit.is_endurance for conduit in CONDUITS]))
