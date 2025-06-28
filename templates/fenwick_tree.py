class FenwickTree:
    def __init__(self, size):
        self.n = size + 1
        self.tree = [0] * self.n

    def update(self, i, delta):
        while i < self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
