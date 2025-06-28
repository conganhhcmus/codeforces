class LCA_Simple:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.adj = adj
        self.parent = [-1] * n
        self.depth = [0] * n
        self.dfs(root, -1)

    def dfs(self, u, p):
        self.parent[u] = p
        for v in self.adj[u]:
            if v == p:
                continue
            self.depth[v] = self.depth[u] + 1
            self.dfs(v, u)

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        while self.depth[u] > self.depth[v]:
            u = self.parent[u]
        while u != v:
            u = self.parent[u]
            v = self.parent[v]
        return u


LOG = 20  # Adjust as needed


class LCA_BinaryLifting:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.adj = adj
        self.depth = [0] * n
        self.parent = [[-1] * LOG for _ in range(n)]
        self.log2 = [0] * n
        for i in range(2, n):
            self.log2[i] = self.log2[i // 2] + 1
        self.dfs(root, -1)

    def dfs(self, u, p):
        self.parent[u][0] = p
        for i in range(1, LOG):
            if self.parent[u][i - 1] != -1:
                self.parent[u][i] = self.parent[self.parent[u][i - 1]][i - 1]
        for v in self.adj[u]:
            if v == p:
                continue
            self.depth[v] = self.depth[u] + 1
            self.dfs(v, u)

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for i in range(LOG):
            if diff & (1 << i):
                u = self.parent[u][i]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if self.parent[u][i] != self.parent[v][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]
        return self.parent[u][0]


class LCA_RMQ:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.adj = adj
        self.euler = []
        self.depths = []
        self.first_seen = [-1] * n
        self.time = 0
        self.dfs(root, -1, 0)
        m = len(self.euler)
        self.seg = [0] * (4 * m)
        self.build(1, 0, m - 1)

    def dfs(self, u, p, d):
        if self.first_seen[u] == -1:
            self.first_seen[u] = len(self.euler)
        self.euler.append(u)
        self.depths.append(d)
        for v in self.adj[u]:
            if v == p:
                continue
            self.dfs(v, u, d + 1)
            self.euler.append(u)
            self.depths.append(d)

    def build(self, node, l, r):
        if l == r:
            self.seg[node] = l
            return
        m = (l + r) // 2
        self.build(node * 2, l, m)
        self.build(node * 2 + 1, m + 1, r)
        left = self.seg[node * 2]
        right = self.seg[node * 2 + 1]
        self.seg[node] = left if self.depths[left] < self.depths[right] else right

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return -1
        if ql <= l and r <= qr:
            return self.seg[node]
        m = (l + r) // 2
        left = self.query(node * 2, l, m, ql, qr)
        right = self.query(node * 2 + 1, m + 1, r, ql, qr)
        if left == -1:
            return right
        if right == -1:
            return left
        return left if self.depths[left] < self.depths[right] else right

    def lca(self, u, v):
        i, j = self.first_seen[u], self.first_seen[v]
        if i > j:
            i, j = j, i
        idx = self.query(1, 0, len(self.euler) - 1, i, j)
        return self.euler[idx]
