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


def reverse(arr, st, ed):
    arr[st : ed + 1] = arr[st : ed + 1][::-1]


# Main problem-solving function
def solve():
    n = read_int()
    print(2 * n - 3)
    for i in range(2, n + 1):
        print(i, 1, i)
    for i in range(1, n - 1):
        print(i, i + 1, n)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
