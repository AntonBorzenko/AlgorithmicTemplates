class Bit:
    def __init__(self, length):
        self.bit = [0] * (length + 1)
        self.length = length + 1

    def add(self, index, value):
        index += 1
        while index < self.length:
            self.bit[index] += value
            index += index & (-index)

    def set(self, index, value):
        delta = value - self.sum(index, index)
        self.add(index, delta)

    def sum(self, from_index, to_index=None):
        if to_index is None:
            return self._prefix_sum(from_index)
        result = self._prefix_sum(to_index)
        if from_index > 0:
            result -= self._prefix_sum(from_index - 1)
        return result

    def _prefix_sum(self, to_index):
        to_index += 1
        result = 0
        while to_index:
            result += self.bit[to_index]
            to_index -= to_index & (-to_index)
        return result
