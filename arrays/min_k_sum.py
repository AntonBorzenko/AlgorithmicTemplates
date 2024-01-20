from sortedcontainers import SortedList


class MinKSum:
    """
    Holds the sum of minimal `length` elements
    `add` and `remove` work for `O(logN)`


    Example of use:
    min_sum = MinKSum(3)
    min_sum.add(3)  # min_sum.total() == 3
    min_sum.add(4)  # min_sum.total() == 3 + 4
    min_sum.add(5)  # min_sum.total() == 3 + 4 + 5
    min_sum.add(2)  # min_sum.total() == 2 + 3 + 4
    """
    def __init__(self, length: int):
        self.list = SortedList()
        self.length = length
        self.sum = 0

    def total(self):
        return self.sum

    def add(self, val):
        if len(self.list) >= self.length and val < self.list[self.length - 1]:
            self.sum -= self.list[self.length - 1]

        self.sum += val
        self.list.add(val)

    def remove(self, val):
        if len(self.list) > self.length and val < self.list[self.length]:
            self.sum += self.list[self.length]

        self.sum -= val
        self.list.remove(val)

    def __len__(self):
        return len(self.list)
