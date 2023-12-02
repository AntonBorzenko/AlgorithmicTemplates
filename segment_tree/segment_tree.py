import math
import operator


class SegmentTree:
    def __init__(self, length, neutral_element=0, operator=operator.add):
        self.operator = operator
        self.neutral_element = neutral_element
        self._length = length
        self._inner_size = 1 << math.ceil(math.log2(length))
        self._array = [neutral_element] * (self._inner_size * 2 - 1)

    def __len__(self):
        return self._length

    @staticmethod
    def from_array(array, neutral_element=0, operator=operator.add):
        result = SegmentTree(len(array), neutral_element, operator)
        result.build(array)
        return result

    def build(self, array):
        if len(array) != self._length:
            raise ValueError('There are different lengths of arrays')
        self._build(array, 0, 0, self._inner_size)

    def _build(self, array, st_index, st_left, st_right):
        if st_right - st_left == 1:
            if st_left < len(array):
                self._array[st_index] = array[st_left]
            return

        st_mid = (st_left + st_right) // 2
        self._build(array, 2 * st_index + 1, st_left, st_mid)
        self._build(array, 2 * st_index + 2, st_mid, st_right)
        self._array[st_index] = self.operator(
            self._array[2 * st_index + 1],
            self._array[2 * st_index + 2]
        )

    def _update_index(self, index, right_bound=False):
        if not isinstance(index, int):
            raise TypeError(f'Expected int, got: {type(index)}')
        if not (-self._length - right_bound <= index < self._length + right_bound):
            raise IndexError(f'index should be between 0 and {self._length + right_bound}')
        if index < 0:
            index += self._length
        return index

    def __getitem__(self, index):
        if not isinstance(index, slice):
            index = self._update_index(index)
            return self._array[index - self._inner_size]
        if index.step is not None:
            raise ValueError(f'Steps are not supported')
        start_index = self._update_index(index.start)
        end_index = self._update_index(index.stop, True)
        return self._get(start_index, end_index, 0, 0, self._inner_size)

    def _get(self, left, right, st_index, st_left, st_right):
        if st_left >= right or left >= st_right:
            return self.neutral_element

        if left <= st_left and st_right <= right:
            return self._array[st_index]

        st_mid = (st_left + st_right) // 2

        lvalue = self._get(left, right, 2 * st_index + 1, st_left, st_mid)
        rvalue = self._get(left, right, 2 * st_index + 2, st_mid, st_right)

        return self.operator(lvalue, rvalue)

    def __setitem__(self, index, value):
        index = self._update_index(index)
        self._set(index, value, 0, 0, self._inner_size)

    def _set(self, index, value, st_index, st_left, st_right):
        if st_right - st_left == 1:
            self._array[st_index] = value
            return

        st_mid = (st_left + st_right) // 2
        if index < st_mid:
            self._set(index, value, 2 * st_index + 1, st_left, st_mid)
        else:
            self._set(index, value, 2 * st_index + 2, st_mid, st_right)

        self._array[st_index] = self.operator(
            self._array[2 * st_index + 1],
            self._array[2 * st_index + 2]
        )

    def __iter__(self):
        for i in range(self._length):
            yield self._array[i - self._inner_size]


class RangeUpdateSegmentTree(SegmentTree):
    def __init__(self, length, neutral_element=0, operator=operator.add):
        super().__init__(length, neutral_element, operator)
        self._update_array = [neutral_element] * (self._inner_size * 2 - 1)

    def update_value(self, value, update_value):
        pass

    def update_updatable_value(self, updatable_value, update_value, st_left, st_right):
        pass

    def update_range(self, update_value, start_index, end_index):
        pass
