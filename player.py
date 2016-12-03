import logging

class Player:
    VERSION = "The Dead Parrot"

    def betRequest(self, game_state):
        in_action = game_state['in_action']
        current_player = game_state['players'][in_action]
        cards = current_player['hole_cards']

        players = game_state['players']

        #call_value = game_state['current_buy_in'] - players[game_state['in_action']] + game_state['minimum_raise']
        #print "call value: {0}".format(call_value)

        if cards[0]['rank'] == cards[1]['rank']:
            if cards[0]['rank'] in ("Q", "K", "A"):
                return 1000
            return 1000

        return 0

    def showdown(self, game_state):
        pass
