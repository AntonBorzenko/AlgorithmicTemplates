def get_lps(string):
    result = [0] * len(string)
    size = 0
    i = 1

    while i < len(string):
        if string[i] == string[size]:
            size += 1
            result[i] = size
            i += 1
        elif size != 0:
            size = result[size - 1]
        else:
            result[i] = 0
            i += 1

    return result


def get_minimal_cycle_length(string):
    lps = get_lps(string)

    result = len(string) - lps[-1]
    if len(string) % result != 0:
        return len(string)

    return result
