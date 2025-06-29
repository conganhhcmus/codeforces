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


# Main function
def solve():
    n, a = read_int(), read_ints()
    count = 1
    prev = a[0]
    for i in range(1, n):
        if a[i] > prev + 1:
            prev = a[i]
            count += 1

    print(count)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
