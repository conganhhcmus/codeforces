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


def div_ceil(a, b):
    return (a + b - 1) // b


# Main problem-solving function
def solve():
    n, m, a = read_ints()
    print(div_ceil(n, a) * div_ceil(m, a))


# Entry point
if __name__ == "__main__":
    # For multiple test cases
    # num_test_cases = read_int()
    # for _ in range(num_test_cases):
    solve()
