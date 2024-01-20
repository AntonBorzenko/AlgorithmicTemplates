from .lps import get_lps


def get_minimal_cycle_length(string):
    lps = get_lps(string)

    result = len(string) - lps[-1]
    if len(string) % result != 0:
        return len(string)

    return result
