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


def bit_array(n, bits=64):
    return [(n >> i) & 1 == 1 for i in range(bits)]


# Main problem-solving function
def solve():
    max_bit = 64
    n, k = read_ints()
    arr = read_ints()
    bit_map = []
    sum = 0
    for i in arr:
        tmp = bit_array(i, max_bit)
        bit_map.append(tmp)
        sum += tmp.count(True)

    for i in range(max_bit):
        for bits in bit_map:
            if k < (1 << i):
                break
            if not bits[i]:
                sum += 1
                k -= 1 << i

    print(sum)


# Entry point
if __name__ == "__main__":
    for _ in range(read_int()):
        solve()
