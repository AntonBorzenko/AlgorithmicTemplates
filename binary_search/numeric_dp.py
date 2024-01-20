from functools import cache


def numeric_dp(start: int, finish: int,
               update_bounds=lambda size, index, lower_bound, upper_bound: (lower_bound, upper_bound)):
    if start > finish:
        return 0

    finish_array = [int(digit) for digit in str(finish)]
    size = len(finish_array)
    start_array = [int(digit) for digit in str(start).zfill(size)]

    @cache
    def dp(index, use_lower_bound=True, use_upper_bound=True):
        if index == size:
            return 1

        lower_bound = start_array[index] if use_lower_bound else 0
        upper_bound = finish_array[index] if use_upper_bound else 9

        lower_bound, upper_bound = update_bounds(size, index, lower_bound, upper_bound)

        result = 0
        for value in range(lower_bound, upper_bound + 1):
            cur_use_lower_bound = use_lower_bound and value == start_array[index]
            cur_use_upper_bound = use_upper_bound and value == finish_array[index]
            result += dp(index + 1, cur_use_lower_bound, cur_use_upper_bound)
        return result

    return dp(0)
