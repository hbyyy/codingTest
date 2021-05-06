"""
예시

5 6
101010
111111
000001
111111
111111

10
"""
from collections import deque

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

start_x = start_y = 0


def bfs(v):
    queue = deque([v])

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))


bfs((start_x, start_y))
print(arr[N - 1][M - 1])
