import unittest
import json

import player
from player import Player
from config import Config


class PlayerTest(unittest.TestCase):
    def setUp(self):
        player.config = Config(True)
        self.player = Player()

    def test_bet_request_should_return_integer(self):
        with open('GameState.json') as json_file:
            game_state = json.load(json_file)
        self.assertIsInstance(self.player.betRequest(game_state), int)


if __name__ == '__main__':
    unittest.main()