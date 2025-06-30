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


def area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


# Main function
def solve():
    n = read_int()

    x = [0] * n
    y = [0] * n
    a = [[0, 0] for _ in range(n)]
    for i in range(n):
        a[i] = read_ints()
        x[i], y[i] = a[i]
    x.sort()
    y.sort()

    ans = area(x[0], y[0], x[-1], y[-1])

    if ans == n:
        return print(ans)
    for i in range(n):
        min_x, max_x, min_y, max_y = 0, n - 1, 0, n - 1
        if a[i][0] == x[min_x]:
            min_x += 1
        elif a[i][0] == x[max_x]:
            max_x -= 1
        if a[i][1] == y[min_y]:
            min_y += 1
        elif a[i][1] == y[max_y]:
            max_y -= 1
        val = area(x[min_x], y[min_y], x[max_x], y[max_y])
        if val < n:
            val += min(abs(x[min_x] - x[max_x]) + 1, abs(y[min_y] - y[max_y]) + 1)
        ans = min(ans, val)

    print(ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
