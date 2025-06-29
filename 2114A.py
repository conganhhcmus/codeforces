import sys
from math import sqrt

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


# Constants
INF = 10**18


# Main function
def solve():
    year = read_int()
    sum = int(sqrt(year))
    if sum * sum == year:
        print(0, sum)
    else:
        print(-1)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
