from bisect import bisect_left


def bisearch(check, lo, hi, false2true=True, right_border=True):
    start, end = lo, hi
    if false2true:
        range_ = range(lo, hi + 1)
    else:
        range_ = range(hi, lo - 1, -1)

    index = bisect_left(range_, True, 0, hi - lo + 1, key=check)
    result = lo + index - (not right_border) if false2true else hi - index + right_border
    return min(max(start, result), end)
