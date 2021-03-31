# O(n2) 이라 해결 불가하다
# 벽을 뚫는 방법을 생각해 보자
# 한 번의 bfs 수행으로 가능하다고 한다

from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return visited[n - 1][m - 1]


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

result = 1e9

distance = bfs()
if distance != 0:
    result = min(result, distance)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 0
            distance = bfs()
            arr[i][j] = 1

            if distance != 0:
                result = min(result, distance)

print(result) if result != 1e9 else print(-1)

