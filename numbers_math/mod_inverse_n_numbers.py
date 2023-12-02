def get_inv_array(length, base=10 ** 9 + 7):
    result = [1] * (length + 1)

    for i in range(2, length + 1):
        result[i] = result[base % i] * (base - base // i) % base

    return result
