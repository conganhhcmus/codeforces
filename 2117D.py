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
    # solution1()
    solution2()


def solution1():
    n, arr = read_int(), read_ints()
    # is increase or degrease with space is diff
    diff = arr[0] - arr[1]
    min_val = arr[0]
    for i in range(1, n, 1):
        if diff != arr[i - 1] - arr[i]:
            return print("NO")
        min_val = min(min_val, arr[i])

    diff = abs(diff)
    if min_val >= diff and (min_val - diff) % (n + 1) == 0:
        return print("YES")
    return print("NO")


def solution2():
    n, arr = read_int(), read_ints()
    num = n * arr[0] - arr[-1]
    den = n * n - 1
    if num < 0 or num % den != 0:
        return print("NO")

    y = num // den
    x = arr[0] - n * y
    if x < 0:
        return print("NO")

    for i, val in enumerate(arr, start=1):
        if i * x + (n - i + 1) * y != val:
            return print("NO")
    print("YES")


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
