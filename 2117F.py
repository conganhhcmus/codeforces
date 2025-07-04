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


# Main function
def solve():
    n = read_int()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = read_ints()
        adj[u].append(v)
        adj[v].append(u)

    ans = 0
    print(ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
