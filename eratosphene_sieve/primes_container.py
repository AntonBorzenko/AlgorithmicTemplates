from collections import Counter, defaultdict
from .eratosphene_class import EratospheneSieve


class PrimeCounter:
    def __init__(self, sieve: EratospheneSieve = None, max_value=-1):
        self.sieve = sieve if sieve else EratospheneSieve(max_value)
        self.length = 0
        self.primes2counts = Counter()  # (prime, id) -> number of numbers of primes
        self.counts2primes = defaultdict(set)  # number of numbers of primes -> set[(prime, id)]

    def add(self, value):
        self.length += 1

        for key in self._prime_keys(value):
            count = self.primes2counts[key]
            if count:
                self._remove_key_count(key, count)

            self.primes2counts[key] += 1
            self.counts2primes[count + 1].add(key)

    def remove(self, value):
        self.length -= 1

        for key in self._prime_keys(value):
            count = self.primes2counts[key]
            self._remove_key_count(key, count)

            if count == 1:
                del self.primes2counts[key]
            else:
                self.primes2counts[key] -= 1
                self.counts2primes[count - 1].add(key)

    def __len__(self):
        return self.length

    def gcd_len(self):
        if not self.length in self.counts2primes:
            return 0
        return len(self.counts2primes[self.length])

    def _prime_keys(self, value):
        prime_counter = Counter()
        for prime in self.sieve.primes(value):
            yield prime, prime_counter[prime]
            prime_counter[prime] += 1

    def _remove_key_count(self, key, count):
        current_set = self.counts2primes[count]
        if len(current_set) == 1:
            del self.counts2primes[count]
        else:
            current_set.remove(key)
