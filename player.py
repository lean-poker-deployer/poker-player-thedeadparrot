
class Player:
    VERSION = "The Dead Parrot"

    def betRequest(self, game_state):
        in_action = game_state['in_action']
        current_player = game_state['players'][in_action]
        cards = current_player['hole_cards']

        if cards[0]['rank'] == cards[1]['rank']:
            return 1000

        return 0

    def showdown(self, game_state):
        pass

