def bisearch(check, lo, hi, false2true=True, right_border=True):
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
