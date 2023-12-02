class EratospheneSieve:
    def __init__(self, max_value):
        if max_value < 1:
            raise ValueError(f'max_value should be more than 0')
        self.max_value = max_value
        max_value += 1
        sieve = [1] * max_value
        for i in range(2, max_value):
            if sieve[i] == 1:
                sieve[i] = i
                for j in range(i * i, max_value, i):
                    sieve[j] = i
        self.sieve = sieve

    def _check(self, value):
        if value < 1 or value > self.max_value:
            raise ValueError(f'value must be in range from 1 to {self.max_value}, got: {value}')

    def is_prime(self, value):
        self._check(value)
        return self.sieve[value] == value

    def primes(self, value):
        self._check(value)
        while value > 1:
            yield self.sieve[value]
            value //= self.sieve[value]

    @staticmethod
    def prime_iter(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                n /= i
                yield i
            else:
                i += 1

        if n > 1:
            yield n


sieve = EratospheneSieve(-1)
