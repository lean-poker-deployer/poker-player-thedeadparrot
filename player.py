import json
import logging
from random import randint
from config import Config

import sys

from ranking_helper import RankingHelper

# logging.basicConfig(format='%(levelname)s %(lineno)d:%(funcName)s %(message)s')
log = logging.getLogger('player.Player')
log.addHandler(logging.StreamHandler(sys.stderr))
log.setLevel(logging.DEBUG)

TWO_PAIRS = 2


class Player:
    VERSION_FORMAT = "Cautious parrot [config: {config}]"
    VERSION = "Cautious parrot"

    def __init__(self):
        self.config = Config.get_instance()
        self.VERSION = self.VERSION_FORMAT.format(config=self.config.version)

    def betRequest(self, game_state):
        log.info('player version: %s', self.config.version)

        bet = 0
        in_action = game_state['in_action']
        current_player = game_state['players'][in_action]
        hand_cards = current_player['hole_cards']
        all_cards = hand_cards + game_state['community_cards']

        ranking_service = RankingHelper(all_cards)

        all_in_value = current_player["stack"]
        minimum_raise = int(game_state["minimum_raise"])
        small_blind = int(game_state["small_blind"])

        is_preflop = len(game_state["community_cards"]) == 0

        call_value = game_state['current_buy_in'] - current_player['bet'] + game_state['minimum_raise']
        active_player_count = len(filter(lambda player: player["status"] == "active", game_state["players"]))
        chen_ranking = ranking_service.get_chen_ranking()

        if is_preflop:
            if active_player_count == 2:
                if chen_ranking >= self.config.count_2_min_chen_ranking:
                    bet = min(call_value, all_in_value/2)
            elif active_player_count == 3:
                if chen_ranking >= self.config.count_3_min_chen_ranking:
                    bet = min(call_value, all_in_value/2)
            elif active_player_count == 4:
                if chen_ranking >= self.config.count_4_min_chen_ranking:
                    bet = min(call_value, all_in_value/2)

            if bet != all_in_value:
                did_somebody_raise = minimum_raise >= small_blind * 2

                if not did_somebody_raise:
                    bet = minimum_raise * 2

            if minimum_raise > small_blind * 8 and chen_ranking >= self.config.high_raise_min_chen_ranking:
                bet = min(call_value, all_in_value/2)
        else:
            if self.config.post_flop:
                ranking = ranking_service.get_ranking()
                if ranking == 0:
                    bet = 0
                elif ranking == 1:
                    bet = self._handle_one_pair(call_value, hand_cards)
                elif ranking >= TWO_PAIRS:
                    bet = all_in_value
            else:
                if ranking_service.is_pair():
                    bet = self._handle_one_pair(call_value, hand_cards)
                else:
                    log.info('decision fold')
                    return 0

        if self.config.fold_over_max_stack_ratio:
            if current_player['bet'] > all_in_value * self.config.max_stack_ratio:
                return call_value

        return bet

    def _handle_one_pair(self, call_value, hand_cards):
        if hand_cards[0]['rank'] in ("Q", "K", "A"):
            bet = call_value + self.config.bet_on_high_pair
            log.info('decision betting: %d', bet)
        else:
            bet = self.config.bet_on_pair
            log.info('decision betting: %d', bet)
        return bet

    def showdown(self, game_state):
        log.info("number_of_community_cards %d", len(game_state['community_cards']))
