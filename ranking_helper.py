class RankingHelper:
    _ranks2values = {"J": 11, "Q": 12, "K": 13, "A": 14}
    _rank2chenvalue = {"J": 6, "Q": 7, "K": 8, "A": 10}

    def __init__(self, cards):
        self._rank2value = dict()
        self._value_frequency_map = {}

        for rank in [str(x) for x in range(2, 11)]:
            self._rank2value[rank] = int(rank)
            self._rank2chenvalue[str(rank)] = int(rank) / 2.0

        self._cards = cards


    def computeFrequencies(self):
        for card in self._cards:
            card_value = self.value_of_rank(str(card['rank']))
            self._value_frequency_map[card_value] = self._value_frequency_map.get(card_value, 0) + 1
        self._value_frequencies = self._value_frequency_map.values()

    def value_of_rank(self, rank):
        return self._rank2value[rank]

    def is_pair(self):
        return 2 in self._value_frequencies

    def is_two_pairs(self):
        return self._value_frequencies.count(2) == 2

    def is_drill(self):
        return 3 in self._value_frequencies

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

