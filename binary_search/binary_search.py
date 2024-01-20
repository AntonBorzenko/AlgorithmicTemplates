"""
How to use:

bisearch(lambda v: v >= 15, lo=0, hi=100, right_border=True) == 15
bisearch(lambda v: v >= 15, lo=0, hi=100, right_border=False) == 14

bisearch(lambda v: v <= 14, lo=0, hi=100, false2true=False, right_border=True) == 15
bisearch(lambda v: v <= 14, lo=0, hi=100, false2true=False, right_border=False) == 14
"""


def bisearch(check, lo: int, hi: int, false2true=True, right_border=True):
    not_false2true = not false2true
    not_right_border = not right_border
    while lo < hi:
        mid = (lo + hi + not_right_border) // 2
        is_ok = check(mid) ^ not_false2true
        if is_ok:
            hi = mid - not_right_border
        else:
            lo = mid + right_border
    return lo
