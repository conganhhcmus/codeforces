import sys
from typing import Counter

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
    s = read_str()
    has = read_ints()
    cost = read_ints()
    tot = read_int()
    c = INF
    cnt = [0, 0, 0]
    for ch in s:
        if ch == "B":
            cnt[0] += 1
        elif ch == "S":
            cnt[1] += 1
        else:
            cnt[2] += 1

    low, high, ans = 0, INF, 0

    def ok(val):
        need = 0
        for i in range(3):
            need += max(0, val * cnt[i] - has[i]) * cost[i]

        return need <= tot

    while low <= high:
        mid = (low + high) >> 1

        if ok(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)


# Entry point
if __name__ == "__main__":
    # for _ in range(read_int()):
    solve()
