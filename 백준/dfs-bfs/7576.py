# 토마토
# 잘 익은 토마토의 인덱스들을 먼저 큐에 넣어놓고 bfs 돌리면 된다

from collections import deque


def check():
    max_value = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
            max_value = max(max_value, arr[i][j])
    if max_value == 1:
        return 0
    return max_value


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))


m, n = map(int, input().split())
arr = []
ripe_tomatos = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            ripe_tomatos.append((i, j))
    arr.append(row)

bfs(deque(ripe_tomatos))

print(check())
