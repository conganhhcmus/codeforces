class RollingHash61:
    MOD = (1 << 61) - 1

    def __init__(self, base, n):
        assert base > 0 and n >= 0
        self.M = base
        self.len = 0
        self.hash = [0] * (n + 1)
        self.pows = [1] * (n + 1)
        for i in range(1, n + 1):
            self.pows[i] = self.mul(self.pows[i - 1], base)

    def mod(self, x):
        x = (x & self.MOD) + (x >> 61)
        if x >= self.MOD:
            x -= self.MOD
        return x

    def mul(self, a, b):
        # Emulate 64-bit * 64-bit -> 128-bit -> MOD (Python handles big ints)
        return self.mod(a * b)

    def add(self, x):
        self.hash[self.len + 1] = self.mod(self.mul(self.hash[self.len], self.M) + x)
        self.len += 1

    def get_hash(self, l, r):
        assert 0 <= l <= r <= self.len
        return self.mod(self.hash[r] - self.mul(self.hash[l], self.pows[r - l]))
