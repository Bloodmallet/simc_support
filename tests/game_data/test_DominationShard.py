import unittest

from simc_support.game_data.DominationShard import DOMINATION_SHARDS
from simc_support.game_data.DominationShard import ShardType


class TestDominationShards(unittest.TestCase):
    def test_type(self):
        self.assertTrue(isinstance(DOMINATION_SHARDS, list))

    def test_non_emptyness(self):
        self.assertTrue(len(DOMINATION_SHARDS) > 0)

    def test_for_each_shard_type(self):
        """At least one shard for each shard type is available."""
        for type in ShardType:
            with self.subTest(type=type):
                found = False
                for shard in DOMINATION_SHARDS:
                    if type == shard.school_type:
                        found = True
                        break
                self.assertTrue(found)
