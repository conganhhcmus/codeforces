import sys

# Fast I/O
input = sys.stdin.readline

# Recursion Limit
sys.setrecursionlimit(10**6)


# Input/Output Helpers
def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split()))


def read_str():
    return input().strip()


def read_strs():
    return list(input().split())


def YN(a):
    print("YES" if a else "NO")


# Constants
INF = 10**18


def dfs(u, p, val, adj, a):
    min_val = min(a[u - 1], a[u - 1] - val[1])
    max_val = max(a[u - 1], a[u - 1] - val[0])
    a[u - 1] = max_val
    for v in adj[u]:
        if p != v:
            dfs(v, u, [min_val, max_val], adj, a)


# Main function
def solve():
    n = read_int()
    a = read_ints()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = read_ints()
        adj[u].append(v)
        adj[v].append(u)

    dfs(1, -1, [0, 0], adj, a)

    print(*a)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
