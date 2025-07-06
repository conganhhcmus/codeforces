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
    n, a, b, x, y = read_ints()
    ans = 0
    sub = 0
    while n >= a or n >= b:
        if n >= a and n >= b:
            val = a if x <= y else b
            sub = (n - val) // min(x, y) + 1
            ans += sub
            n -= sub * min(x, y)
        elif n >= a:
            sub = ((n - a) // x) + 1
            ans += sub
            n -= sub * x
        elif n >= b:
            sub = ((n - b) // y) + 1
            ans += sub
            n -= sub * y

    print(ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
