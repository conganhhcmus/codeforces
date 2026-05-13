import sys, math, itertools, functools, collections  # noqa

input = sys.stdin.readline


def solution():
    n, m, k = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    tot = 0
    start = (0, 0)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                tot += 1
                start = (i, j)

    need = tot - k
    q = collections.deque([start])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vis = [[False] * m for _ in range(n)]
    vis[start[0]][start[1]] = True
    need -= 1
    while len(q) > 0 and need > 0:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not vis[nx][ny] and grid[nx][ny] == ".":
                    vis[nx][ny] = True
                    q.append((nx, ny))
                    need -= 1
                    if need == 0:
                        break

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and not vis[i][j]:
                grid[i][j] = "X"

    for row in grid:
        print("".join(row))


# for _ in range(int(input())):
solution()
