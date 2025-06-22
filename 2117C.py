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
    a = read_ints()
    MAX_VAL = max(a) + 1
    ans = 0
    curr = [False] * MAX_VAL
    curr_cnt = 0
    next = [False] * MAX_VAL
    next_cnt = 0
    for x in a:
        if not next[x]:
            next[x] = True
            next_cnt += 1
        if curr[x]:
            curr[x] = False
            curr_cnt -= 1
        if curr_cnt == 0:
            ans += 1
            curr, next = next, curr
            curr_cnt, next_cnt = next_cnt, curr_cnt

    print(ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
