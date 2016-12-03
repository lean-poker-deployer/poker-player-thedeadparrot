class RankingHelper:
    _ranks2values = {"J": 11, "Q": 12, "K": 13, "A": 14}
    _value_frequencies = {}

    def __init__(self, cards):
        self._rank2value = dict()
        for rank in range(2, 11):
            self._rank2value[rank] = rank

        self._cards = cards
        self._computeFrequency()

    def value_of_rank(self, rank):
        return self._rank2value[rank]

    def _computeFrequency(self):
        for card in self._cards:
            card_value = self.value_of_rank(card['rank'])
            self._value_frequencies[card_value] = self._value_frequencies.get(card_value, 0) + 1

    def is_pair(self):
        return 2 in self._value_frequencies.values()

