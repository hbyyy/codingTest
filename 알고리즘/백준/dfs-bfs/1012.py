# stack 이용 풀이

def dfs(v):
    stack = [v]

    while stack:
        x, y = stack.pop()
        if arr[x][y] != 1:
            continue
        arr[x][y] = 2

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    stack.append((nx, ny))


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs((i, j))
                count += 1

    print(count)


# 재귀 이용 풀이
import sys

sys.setrecursionlimit(100000)


def dfs(v):
    x, y = v
    arr[x][y] = 2

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                dfs((nx, ny))


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs((i, j))
                count += 1

    print(count)