import sys

# Fast I/O
input = sys.stdin.readline


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


def index(c):
    return ord(c) - ord("0")


# Main function
def solve():
    n, k = read_ints()
    s = read_str()
    c0 = s.count("0")
    c1 = n - c0
    d = n / 2 - k
    c0 -= d
    c1 -= d
    ans = c0 >= 0 and c1 >= 0 and c0 // 2 + c1 // 2 == k
    YN(ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
