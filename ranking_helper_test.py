import unittest

from ranking_helper import RankingHelper


class RankingHelperTest(unittest.TestCase):
    def test_is_pair_GivenPair_ReturnsTrue(self):
        helper = RankingHelper([
            {"rank": 4},
            {"rank": 9},
            {"rank": 4},
        ])

        self.assertTrue(helper.is_pair())

    def test_is_two_pairs_GivenTwoPairs_ReturnsTrue(self):
        helper = RankingHelper([
            {"rank": 4},
            {"rank": 9},
            {"rank": 4},
            {"rank": 9},
            {"rank": 8},
        ])

        self.assertTrue(helper.is_two_pairs())

    def test_is_drill_GivenDrill_ReturnsTrue(self):
        helper = RankingHelper([
            {"rank": 2},
            {"rank": 9},
            {"rank": 2},
            {"rank": 7},
            {"rank": 2},
        ])

        self.assertTrue(helper.is_drill())


if __name__ == '__main__':
    unittest.main()
