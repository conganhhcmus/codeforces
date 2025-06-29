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


# Constants
INF = 10**18


# Main function
def solve():
    n, a, b = read_int(), read_ints(), read_ints()

    seen = [False] * (n + 1)
    if a[-1] == b[-1]:
        return print(n)
    ans = -1
    for i in reversed(range(n - 1)):
        if a[i] == b[i] or a[i] == a[i + 1] or b[i] == b[i + 1] or seen[a[i]] or seen[b[i]]:
            ans = i
            break
        seen[a[i + 1]] = seen[b[i + 1]] = True
    print(ans + 1)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
