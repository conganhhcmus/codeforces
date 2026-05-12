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

    @lru_cache(maxsize=None)
    def dp(remain, state):
        if remain < 0:
            return 0
        if remain == 0:
            return state
        ans = 0
        for i in range(1, k + 1, 1):
            newState = 1 if (state == 1 or i >= d) else 0
            ans += dp(remain - i, newState)

        return ans % MOD

    print(dp(n, 0))


# Entry point
if __name__ == "__main__":
    solve()
