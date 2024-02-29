def prefix_function(string: str) -> list[int]:
    n = len(string)
    result = [0] * n

    left = 0
    right = 0
    for i in range(1, n):
        result[i] = max(0, min(right - i, result[i - left]))
        while i + result[i] < n and string[result[i]] == string[i + result[i]]:
            result[i] += 1
        if i + result[i] > right:
            left = i
            right = i + result[i]

    return result
