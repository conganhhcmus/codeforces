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
    a, b, c = read_ints()
    if a + b == c or b + c == a or c + a == b:
        print("YES")
    else:
        print("NO")


# Entry point
if __name__ == "__main__":
    # For multiple test cases
    for _ in range(read_int()):
        solve()
