# Import
import sys

# Fast I/O
input = sys.stdin.readline
INF = 10**18


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
    # Your solution logic here
    a, b, c, d = read_ints()
    p1 = min(a, c)
    p2 = min(b, d)
    if p1 >= p2:
        print("Gellyfish")
    else:
        print("Flower")


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
