from collections import deque


def bfs(v):
    queue = deque([v])

    while queue:
        x, y = queue.popleft()
        arr[x][y] = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                queue.append((nx, ny))


def dfs(v):
    x, y = v
    arr[x][y] = 1

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                dfs((nx, ny))


count = 0
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs((i, j))
            count += 1
print(count)
