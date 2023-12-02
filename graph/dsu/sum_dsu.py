class SumDSU:
    def __init__(self, n):
        self.roots = list(range(n))
        self.sums = [1] * n

    def find(self, value):
        if self.roots[value] != value:
            self.roots[value] = self.find(self.roots[value])
        return self.roots[value]

    def sum(self, value):
        return self.sums[self.find(value)]

    def join(self, value1, value2):
        value1 = self.find(value1)
        value2 = self.find(value2)

        if value1 == value2:
            return False

        if self.sums[value1] < self.sums[value2]:
            value1, value2 = value2, value1

        self.roots[value2] = value1
        self.sums[value1] += self.sums[value2]
        return True
