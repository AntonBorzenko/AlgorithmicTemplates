def get_lps(string: str) -> list[int]:
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
