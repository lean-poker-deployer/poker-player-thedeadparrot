def _rankSort(a, b):
    return RankingHelper.STRAIGHT_VALUES.index(a["rank"]) - RankingHelper.STRAIGHT_VALUES.index(b["rank"])


class RankingHelper:
    _rank2value = {"J": 11, "Q": 12, "K": 13, "A": 14}
    _rank2chenvalue = {"J": 6, "Q": 7, "K": 8, "A": 10}
    STRAIGHT_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    RANKING_ONE_PAIR = 1
    RANKING_TWO_PAIRS = 2
    RANKING_DRILL = 3
    RANKING_STRAIGHT = 4
    RANKING_FLUSH = 5
    RANKING_FULL = 6
    RANKING_POKER = 7

    def __init__(self, cards):
        self._ranks = dict()
        self._suits = dict()
        self._values = list()
        self._value_frequency_map = {}

        for rank in [str(x) for x in range(2, 11)]:
            self._rank2value[rank] = int(rank)
            self._rank2chenvalue[str(rank)] = int(rank) / 2.0

        self._cards = cards
        self._computeFrequencies()
        self._computeRanksAndSuits()

    def _computeFrequencies(self):
        for card in self._cards:
            card_value = self.value_of_rank(str(card['rank']))
            self._value_frequency_map[card_value] = self._value_frequency_map.get(card_value, 0) + 1
        self._value_frequencies = self._value_frequency_map.values()

    def _computeRanksAndSuits(self):
        for card in self._cards:
            rank = card["rank"]
            suit = card["suit"]
            self._ranks[rank] = self._ranks.get(rank, 0) + 1
            self._suits[suit] = self._suits.get(suit, 0) + 1
            self._values.append(self._rank2value[rank])

    def value_of_rank(self, rank):
        return self._rank2value[rank]

    def is_pair(self):
        return 2 in self._value_frequencies

    def is_two_pairs(self):
        return self._value_frequencies.count(2) == 2

    def is_drill(self):
        return 3 in self._value_frequencies

    def is_poker(self):
        return 4 in self._ranks.values()

    def is_full(self):
        return (2 in self._ranks.values()) and (3 in self._ranks.values())

    def is_flush(self):
        return 5 in self._suits.values() or 6 in self._suits.values() or 7 in self._suits.values()

    def is_straight(self):
        for idx in range(1, len(self._cards)):
            diff = abs(self._values[idx - 1] - self._values[idx])
            if diff != 1:
                return False
        return True

    def get_chen_ranking(self):
        ranks = [card["rank"] for card in self._cards]
        suits = [card["suit"] for card in self._cards]
        values = [self._rank2value[rank] for rank in ranks]
        chen_values = [self._rank2chenvalue[rank] for rank in ranks]

        chen = max(chen_values)

        is_pair = ranks[0] == ranks[1]
        if is_pair:
            value = values[0]
            if value < 5:
                chen = 5
            elif value == 5:
                chen = 6
            else:
                chen *= 2

        same_suits = suits[0] == suits[1]
        if same_suits:
            chen += 2

        higher_value = max(values)
        lower_value = min(values)
        gap = higher_value - lower_value

        gap2minus = {
            2: -1,
            3: -2,
            4: -4
        }

        if gap in gap2minus:
            chen += gap2minus[gap]
        elif gap >= 5:
            chen -= 5

        if gap in [1, 2] and higher_value < 12:
            chen += 1

        return chen

    def get_ranking(self):
        if self.is_poker():
            return self.RANKING_POKER
        if self.is_full():
            return self.RANKING_FULL
        if self.is_flush():
            return self.RANKING_FLUSH
        if self.is_straight():
            return self.RANKING_DRILL
        if self.is_drill():
            return self.RANKING_DRILL
        if self.is_two_pairs():
            return self.RANKING_TWO_PAIRS
        if self.is_pair():
            return self.RANKING_ONE_PAIR
        return 0
