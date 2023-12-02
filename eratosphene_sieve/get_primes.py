MAX = -1
if MAX == -1:
    raise ValueError('Please, change MAX value')

sieve = [1] * MAX

for i in range(2, MAX):
    if sieve[i] == 1:
        sieve[i] = i
        for j in range(i * i, MAX, i):
            sieve[j] = i


def primes(value):
    while value > 1:
        yield sieve[value]
        value //= sieve[value]


def is_prime(value):
    return sieve[value] == value
