BASE = 10 ** 9 + 7


def inverse(num):
    return pow(num, BASE - 2, BASE)
