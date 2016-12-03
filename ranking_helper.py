class RankingHelper:
    _ranks2values = {"J": 11, "Q": 12, "K": 13, "A": 14}
    _ranks2chen = {"J": 6, "Q": 7, "K": 8, "A": 10}

    def __init__(self, cards):
        self._rank2value = dict()
        self._value_frequency_map = {}

        for rank in [str(x) for x in range(2, 11)]:
            self._rank2value[rank] = int(rank)
            self._ranks2chen[rank] = int(rank) / 2

        self._cards = cards
        self._computeFrequency()

    def value_of_rank(self, rank):
        return self._rank2value[rank]

    def _computeFrequency(self):
        for card in self._cards:
            card_value = self.value_of_rank(str(card['rank']))
            self._value_frequency_map[card_value] = self._value_frequency_map.get(card_value, 0) + 1
        self._value_frequencies = self._value_frequency_map.values()

    def is_pair(self):
        return 2 in self._value_frequencies

    def is_two_pairs(self):
        return self._value_frequencies.count(2) == 2

    def is_drill(self):
        return 3 in self._value_frequencies
