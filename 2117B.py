# Import
import sys
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

# Fast I/O
input = sys.stdin.readline


# Input Parsing Helpers
def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split()))


def read_str():
    return input().strip()


def read_strs():
    return list(input().split())


# Optional: Recursion Limit (if needed for deep recursion)
# sys.setrecursionlimit(10**6)


# Main problem-solving function
def solve():
    n = read_int()
    ans = [0] * n
    val = 1
    for i in range(n // 2):
        ans[i] = val
        ans[n - i - 1] = val + 1
        val += 2

    if n % 2 == 1:
        ans[n // 2] = val
    print(*ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
