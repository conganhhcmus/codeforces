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
MOD = 10**9 + 7

lens = []
lca = -1


def dfs(u, p, adj, dep):
    if len(adj[u]) > 2:
        global lca
        lca = dep

    leaf = True
    for v in adj[u]:
        if v != p:
            dfs(v, u, adj, dep + 1)
            leaf = False

    if leaf:
        global lens
        lens.append(dep)


# Main function
def solve():
    global lca
    lca = -1
    global lens
    lens = []
    n = read_int()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = read_ints()
        adj[u].append(v)
        adj[v].append(u)

    adj[1].append(0)  # dummy node
    dfs(1, 0, adj, 1)

    pw = [1] * (n + 1)
    for i in range(1, n + 1):
        pw[i] = (pw[i - 1] * 2) % MOD

    if len(lens) > 2:
        return print(0)

    if len(lens) == 1:
        return print(pw[n])
    diff = abs(lens[0] - lens[1])
    x = diff + lca
    ans = 1
    if diff == 0:
        ans = 2 * pw[x] % MOD
    else:
        ans = ans * (pw[x] + pw[x - 1]) % MOD

    print(ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
