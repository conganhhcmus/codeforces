# Build SPF (Smallest Prime Factor) for all numbers up to max_value
def build_spf(self, max_value):
    spf = list(range(max_value + 1))
    for i in range(2, int(max_value**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_value + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


# Get all primes using SPF (primes are numbers whose spf == itself)
def get_all_primes(self, spf):
    return [i for i in range(2, len(spf)) if spf[i] == i]


# Get prime factors of a number using precomputed SPF
def get_prime_factors(self, num, spf):
    factors = []
    while num > 1:
        prime = spf[num]
        factors.append(prime)
        num //= prime
    return factors
