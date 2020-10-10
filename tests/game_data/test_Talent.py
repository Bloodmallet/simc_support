import unittest

from simc_support.game_data.WowSpec import WOWSPECS
from simc_support.game_data.Talent import Talent
from simc_support.game_data.Talent import TALENTS
from simc_support.game_data.Talent import get_talent_dict


class TestTalent(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(TALENTS, list))

    def test_non_emptyness(self):
        self.assertTrue(len(TALENTS) > 0)

    def test_content_types(self):
        for talent in TALENTS:
            with self.subTest(talent=talent):
                self.assertTrue(isinstance(talent, Talent))

    def test_talent_dicts(self):
        for wow_spec in WOWSPECS:
            with self.subTest(wow_spec=wow_spec):
                self.assertTrue(isinstance(get_talent_dict(wow_spec), dict))

    def test_existance_of_all(self):
        for wow_spec in WOWSPECS:
            talents = wow_spec.talents
            for row in range(1, 8):
                for column in range(1, 4):
                    with self.subTest(
                        wow_spec=wow_spec, talents=talents, row=row, column=column
                    ):
                        self.assertTrue(
                            row in talents,
                            f"Talent row {row} for {wow_spec} was not found.",
                        )
                        self.assertTrue(
                            column in talents[row],
                            f"Talent {column} in row {row} for {wow_spec} was not found.",
                        )
