from .lps import get_lps


def get_all_indexes(string, pattern) -> list[int]:
    m = len(pattern)
    n = len(string)

    lps = get_lps(pattern)
    result = []
    i = j = 0
    while (n - i) >= (m - j):
        if pattern[j] == string[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result
