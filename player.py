import json
import logging

log = logging.getLogger('player.Player')

class Player:
    VERSION = "The Dead Parrot"

    def betRequest(self, game_state):
        in_action = game_state['in_action']
        current_player = game_state['players'][in_action]
        cards = current_player['hole_cards']


        call_value = game_state['current_buy_in'] - current_player['bet'] + game_state['minimum_raise']

        if cards[0]['rank'] == cards[1]['rank']:
            if cards[0]['rank'] in ("Q", "K", "A"):
                log.info('All in (or at least 1000)')
                return 1000

            log.info('Call!')
            return call_value

        log.info('Fold!')
        return 0

    def showdown(self, game_state):
        log.info("game state: %s", json.dumps(game_state))
        pass
