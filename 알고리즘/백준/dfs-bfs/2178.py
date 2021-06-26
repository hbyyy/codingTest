import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    queue = deque([v])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

bfs((0, 0))

print(arr[n - 1][m - 1])

