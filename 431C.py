import sys
from functools import lru_cache

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
    n, k, d = read_ints()
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1, 1):
        for j in range(1, k + 1, 1):
            if i >= j:
                if j >= d:
                    dp[i][1] += dp[i - j][0] + dp[i - j][1]
                else:
                    dp[i][0] += dp[i - j][0]
                    dp[i][1] += dp[i - j][1]

    print(dp[n][1] % MOD)


# Entry point
if __name__ == "__main__":
    solve()
