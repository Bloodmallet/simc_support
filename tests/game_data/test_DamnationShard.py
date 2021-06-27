import unittest

from simc_support.game_data.DamnationShard import DAMNATION_SHARDS
from simc_support.game_data.DamnationShard import ShardType


class TestDamnationShards(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(DAMNATION_SHARDS, list))

    def test_non_emptyness(self):
        self.assertTrue(len(DAMNATION_SHARDS) > 0)

    def test_for_each_shard_type(self):
        """At least one shard for each shard type is available."""
        for type in ShardType:
            with self.subTest(type=type):
                found = False
                for shard in DAMNATION_SHARDS:
                    if type == shard.school_type:
                        found = True
                        break
                self.assertTrue(found)
