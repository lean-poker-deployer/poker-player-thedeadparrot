
class RankingHelper:
    def __init__(self):
        self._rank2value = dict()
        for rank in range(2, 11):
            self._rank2value[str(rank)] = rank
        for i, rank in enumerate("JQKA"):
            self._rank2value[rank] = 11 + i

    def getValue(self, rank):
        return self._rank2value[rank]
