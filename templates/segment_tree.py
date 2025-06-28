class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i, value):
        i += self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


class SegmentTreeLazy:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        self.build(data)

    def build(self, data):
        # Fill leaves
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # Build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def push(self, node, node_left, node_right):
        # Push lazy value to children
        if self.lazy[node] != 0:
            self.tree[node] += (node_right - node_left + 1) * self.lazy[node]
            if node < self.size:  # not a leaf
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, l, r, val, node=1, node_left=0, node_right=None):
        if node_right is None:
            node_right = self.size - 1
        self.push(node, node_left, node_right)
        if r < node_left or l > node_right:
            return
        if l <= node_left and node_right <= r:
            self.lazy[node] += val
            self.push(node, node_left, node_right)
            return
        mid = (node_left + node_right) // 2
        self.update(l, r, val, node * 2, node_left, mid)
        self.update(l, r, val, node * 2 + 1, mid + 1, node_right)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, l, r, node=1, node_left=0, node_right=None):
        if node_right is None:
            node_right = self.size - 1
        self.push(node, node_left, node_right)
        if r < node_left or l > node_right:
            return 0
        if l <= node_left and node_right <= r:
            return self.tree[node]
        mid = (node_left + node_right) // 2
        left_sum = self.query(l, r, node * 2, node_left, mid)
        right_sum = self.query(l, r, node * 2 + 1, mid + 1, node_right)
        return left_sum + right_sum
