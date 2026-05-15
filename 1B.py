import sys, math, itertools, functools, collections  # noqa

input = sys.stdin.readline


def is_rc(s):
    return s[0] == "R" and s[1].isdigit() and "C" in s


def solution():
    s = input().strip()

    if is_rc(s):
        # R23C55 -> BC23

        c = s.find("C")

        row = int(s[1:c])
        col = int(s[c + 1 :])

        ans = ""

        while col > 0:
            col -= 1
            ans = chr(ord("A") + col % 26) + ans
            col //= 26

        print(ans + str(row))

    else:
        # BC23 -> R23C55

        idx = next(i for i, ch in enumerate(s) if ch.isdigit())

        col = s[:idx]
        row = int(s[idx:])

        c = 0

        for ch in col:
            c = c * 26 + (ord(ch) - ord("A") + 1)

        ans = "R" + str(row) + "C" + str(c)

        print(ans)


for _ in range(int(input())):
    solution()
