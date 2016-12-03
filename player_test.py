import unittest
import json

from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player(test=True)

    def test_bet_request_should_return_integer(self):
        with open('GameState.json') as json_file:
            game_state = json.load(json_file)
        self.assertIsInstance(self.player.betRequest(game_state), int)


if __name__ == '__main__':
    unittest.main()