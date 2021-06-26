# 접근은 비슷했다
# 연합을 구성할 수 있는 노드를 찾으면 바로 bfs를 돌리지 말고, 다른 연합도 모두 찾고 돌려야 한

from collections import deque


def check(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if L <= abs(origin_arr[x][y] - origin_arr[nx][ny]) <= R:
                return True
    return False


def bfs(i, j):
    visited = [[0] * n for _ in range(n)]
    queue = deque([(i, j)])
    visited_count = 0
    sum_population = origin_arr[i][j]
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if L <= abs(origin_arr[x][y] - origin_arr[nx][ny]) <= R:
                    if visited[nx][ny] == 0:
                        visited_count += 1
                        sum_population += origin_arr[nx][ny]
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

    if visited_count == 0:
        return
    else:
        avg_population = sum_population // (visited_count + 1)
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 1:
                    origin_arr[i][j] = avg_population


n, L, R = map(int, input().split())
origin_arr = []
for _ in range(n):
    origin_arr.append(list(map(int, input().split())))

count = 0
i = 0
while i < n:
    j = 0
    while j < n:
        if check(i, j):
            bfs(i, j)
            count += 1
            i = j = 0
        else:
            j += 1
    i += 1

print(count)
