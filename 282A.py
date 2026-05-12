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
    x = 0
    n = read_int()
    for _ in range(n):
        line = read_str()
        if "--" in line:
            x -= 1
        elif "++" in line:
            x += 1
    print(x)


# Entry point
if __name__ == "__main__":
    solve()
