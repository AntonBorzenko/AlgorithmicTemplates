"""

Example of use:

array = [5, 3, 9, 10]
left, right = get_max_range(array)

"""

from typing import Callable


def get_max_range(array: list, key: Callable[[int], int] = None):
    if key is None:
        def key(value):
            return value

    length = len(array)

    stack = []
    right = [0] * length
    for i in range(length):
        current_key = key(array[i])
        while stack and current_key > stack[-1][1]:
            right[stack.pop()[0]] = i - 1
        stack.append((i, current_key))
    for i, _ in stack:
        right[i] = length - 1

    stack = []
    left = [0] * length
    for i in range(length - 1, -1, -1):
        current_key = key(array[i])
        while stack and current_key >= stack[-1][1]:
            left[stack.pop()[0]] = i + 1
        stack.append((i, current_key))
    for i, _ in stack:
        left[i] = 0

    return left, right
