import unittest

from simc_support.game_data.WowSpec import WOWSPECS, get_wow_spec
from simc_support.game_data.Talent import Talent
from simc_support.game_data.Talent import TREES


# class TestTalent(unittest.TestCase):
#     def test_type(self):
#         self.assertTrue(isinstance(TREES, list))

#     def test_non_emptyness(self):
#         self.assertTrue(len(TREES) > 0)

#     def test_content_types(self):
#         for talent in TREES:
#             with self.subTest(talent=talent):
#                 self.assertTrue(isinstance(talent, Talent))

# no working one yet
# def test_talent_combination_generator(self):
#     elemental = get_wow_spec("shaman", "elemental")
#     for wow_spec in WOWSPECS:
#         combinations = wow_spec.get_talent_combinations()
#         with self.subTest(wow_spec=wow_spec):
#             self.assertGreater(len(combinations), 0)

#             if wow_spec == elemental:
#                 self.assertEqual(len(combinations), 243)
