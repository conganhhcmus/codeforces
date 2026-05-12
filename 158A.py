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
    n, k = read_ints()
    p = read_ints()
    p.sort(reverse=True)
    c = 0
    for i in range(n):
        if p[i] > 0 and p[i] >= p[k - 1]:
            c += 1
    print(c)


# Entry point
if __name__ == "__main__":
    solve()
