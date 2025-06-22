import sys

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
    n, x = read_ints()
    a = read_ints()
    l, r = len(a), -1
    for i in range(len(a)):
        if a[i] == 1:
            r = i
            l = min(l, i)
    if x >= r - l + 1:
        print("YES")
    else:
        print("NO")


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
