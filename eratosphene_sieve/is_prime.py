MAX = -1
if MAX == -1:
    raise ValueError('Please, change MAX value')
is_prime: list[bool | None] = [None] * MAX

for i in range(2, MAX):
    if is_prime[i] is None:
        is_prime[i] = True
        for j in range(i * i, MAX, i):
            is_prime[j] = False
