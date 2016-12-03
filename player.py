import json
import logging
from random import randint

import sys

logging.basicConfig(format='%(levelname)s %(lineno)d:%(funcName)s %(message)s')
log = logging.getLogger('player.Player')
log.addHandler(logging.StreamHandler(sys.stderr))
log.setLevel(logging.DEBUG)


class Player:
    VERSION = "Cautios parrot"

    def betRequest(self, game_state):
        in_action = game_state['in_action']
        current_player = game_state['players'][in_action]
        cards = current_player['hole_cards']

        call_value = game_state['current_buy_in'] - current_player['bet'] + game_state['minimum_raise']

        if cards[0]['rank'] == cards[1]['rank']:
            if cards[0]['rank'] in ("Q", "K", "A"):
                log.info('All in (or at least 1000)')
                return call_value + randint(100, 200)

            log.info('Call!')
            return call_value

        log.info('Fold!')
        return 0

    def showdown(self, game_state):
        log.info("number_of_community_cards %d", len(game_state['community_cards']))
