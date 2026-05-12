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
    s = read_str()
    a = ""
    for i in range(len(s)):
        if s[i].upper() in "AOYEUI":
            continue
        a += "." + s[i].lower()
    print(a)


# Entry point
if __name__ == "__main__":
    solve()
