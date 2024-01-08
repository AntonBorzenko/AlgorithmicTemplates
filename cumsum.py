from itertools import accumulate


class CumSum:
    def __init__(self, iterable, assert_boundaries: bool = False):
        self.cumsum = list(accumulate(iterable))
        self.cumsum.append(0)
        self.assert_boundaries = assert_boundaries

    def __call__(self, left: int, right: int) -> int:
        if left > right:
            if self.assert_boundaries:
                raise IndexError(f'left > right: {left} > {right}')
            return 0
        return self.cumsum[right] - self.cumsum[left - 1]
