MOD = 10**9 + 7


def mod_inv(a):
    return pow(a, MOD - 2, MOD)


def mod_fact(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    return fact


def mod_inv_fact(fact):
    inv = [1] * len(fact)
    inv[-1] = mod_inv(fact[-1])
    for i in range(len(fact) - 2, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    return inv


def comb(n, r, fact, inv):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD
