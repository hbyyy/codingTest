from collections import deque
from time import time

# bfs 버전 (내가 푼 방식)
N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, list(input()))))
result = 0


def bfs(arr, start_node):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        arr[node[0]][node[1]] = 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    queue.append((nx, ny))


time1 = time()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(arr, (i, j))
            result += 1
time2 = time()
print(result, time2 - time1)


# dfs 버전
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))
result = 0


def dfs(x, y):
    graph[x][y] = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                dfs(nx, ny)


time1 = time()
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            dfs(i, j)
            result += 1
time2 = time()
print(result, time2 - time1)


## 책 버전
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))
result = 0


def dfs2(x, y):
    if not (0 <= x < N and 0 <= y < M):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


time1 = time()
for i in range(N):
    for j in range(M):
        if dfs2(i, j) is True:
            result += 1
time2 = time()
print(result, time2 - time1)


