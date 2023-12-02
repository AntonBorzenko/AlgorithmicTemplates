catalans = [1] * 502


for n in range(1, 501):
    catalans[n + 1] = 2 * catalans[n] * (2 * n - 1) // (n + 1)
