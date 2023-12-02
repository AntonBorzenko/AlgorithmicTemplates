BASE = 10 ** 9 + 7
catalans = [1] * 502
inv = [1] * 503

for i in range(2, 502):
    inv[i] = inv[BASE % i] * (BASE - BASE // i) % BASE

for n in range(1, 501):
    catalans[n + 1] = (2 * catalans[n] * (2 * n - 1) * inv[n + 1]) % BASE
