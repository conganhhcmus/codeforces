# Import
import sys

# Fast I/O
input = sys.stdin.readline
INF = 10**18
MOD = 998244353


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


def mod(a):
    return a % MOD


# Main problem-solving function
def solve():
    # Your solution logic here
    n, p, q = read_int(), read_ints(), read_ints()
    pow = [0] * n
    pow[0] = mod(1)
    for i in range(1, n, 1):
        pow[i] = mod(pow[i - 1] * 2)
    ans = [0] * n
    # 2^p[j] + 2^q[i-j] = max(2^p[x] + 2^q[i-x], 2^p[i-y] + 2^q[y])
    # where x is p[x] is max p from 0 to i
    # where y is q[y] is max q from 0 to i
    maxp, maxq = 0, 0
    for i in range(n):
        if p[maxp] < p[i]:
            maxp = i
        if q[maxq] < q[i]:
            maxq = i

        a1, a2 = p[maxp], q[i - maxp]
        b1, b2 = p[i - maxq], q[maxq]
        if max(a1, a2) > max(b1, b2):
            ans[i] = mod(pow[a1] + pow[a2])
        elif max(a1, a2) < max(b1, b2):
            ans[i] = mod(pow[b1] + pow[b2])
        elif min(a1, a2) >= min(b1, b2):
            ans[i] = mod(pow[a1] + pow[a2])
        else:
            ans[i] = mod(pow[b1] + pow[b2])

    print(*ans)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
