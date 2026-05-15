import sys, math, itertools, functools, collections  # noqa

input = sys.stdin.readline


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


def solution():
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    ans = []
    g = 0
    for i in range(1, n):
        g = gcd(g, a[i] - a[0])
    for i in range(m):
        ans.append(gcd(a[0] + b[i], g))
    print(*ans)


# for _ in range(int(input())):
solution()
