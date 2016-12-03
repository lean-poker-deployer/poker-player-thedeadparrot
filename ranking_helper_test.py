import unittest

from ranking_helper import RankingHelper


class PlayerTest(unittest.TestCase):
    # def setUp(self):
    #     self.rankingHelper = RankingHelper()

    def test_is_pair(self):
        helper = RankingHelper([
            {"rank": 4},
            {"rank": 9},
            {"rank": 4},
        ])

        self.assertTrue(helper.is_pair())


if __name__ == '__main__':
    unittest.main()
