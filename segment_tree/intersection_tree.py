import math

from sortedcontainers import SortedList


class IntersectionTree:
    def __init__(self, default_minimal_value=0):
        self.sorted_list = SortedList([[-math.inf, default_minimal_value]])

    def get_max_to(self, to):
        index = self.sorted_list.bisect_right([to, math.inf]) - 1
        return self.sorted_list[index][1]

    def set_max_from(self, from_, value):
        index = self.sorted_list.bisect_right([from_, value])
        if value <= self.sorted_list[index - 1][1]:
            return

        while index < len(self.sorted_list) and self.sorted_list[index][1] <= value:
            self.sorted_list.pop(index)

        self.sorted_list.add([from_, value])
