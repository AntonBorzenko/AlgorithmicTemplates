"""

Example of use:

array = [5, 3, 9, 10]
left, right = get_max_range(array)

"""

from typing import Callable


def get_max_range(array: list, key: Callable[[int], int] = None, borders=(False, True)):
    if key is None:
        def key(value):
            return value

    left_border, right_border = borders
    length = len(array)

    stack = []
    left = [0] * length
    right = [length - 1] * length

    for i, value in enumerate(array):
        current_key = key(value)
        minimal_left = 0
        while stack and (
            current_key > stack[-1][1] or not right_border and current_key == stack[-1][1]
        ):
            removing_index, removing_key = stack.pop()
            right[removing_index] = i - 1
            if removing_key == current_key:
                minimal_left = left[removing_index] if left_border else removing_index + 1

        if stack:
            last_index, last_key = stack[-1]
            if last_key == current_key:
                minimal_left = left[last_index] if left_border else last_index + 1
            else:
                minimal_left = max(minimal_left, last_index + 1)

        left[i] = minimal_left
        stack.append((i, current_key))

    return left, right


def get_min_range(array: list, key: Callable[[int], int] = None, borders=(False, True)):
    if key is None:
        def key(value):
            return -value

    return get_max_range(array, key, borders)
