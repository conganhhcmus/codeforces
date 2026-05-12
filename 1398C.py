import sys
from collections import defaultdict

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
    # 1 2 0
    # sum[u] - sum[v] = sum of s[v+1....u] have u - v length
    # sum[u] - sum[v] = u - v
    # sum[u] - u = sum[v] - v
    n = read_int()
    a = read_str()
    d = defaultdict(int)
    d[0] = 1
    s = 0
    res = 0
    for i in range(n):
        s += (int)(a[i])
        bal = s - i - 1
        res += d[bal]
        d[bal] += 1
    print(res)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
