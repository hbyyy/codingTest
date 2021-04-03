from collections import deque


def bfs(v):
    global is_move
    queue = deque([v])
    union = [v]
    union_count = 1
    sum_population = arr[v[0]][v[1]]
    visited[v[0]][v[1]] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] == 0:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    sum_population += arr[nx][ny]
                    union_count += 1
                    union.append((nx, ny))
                    is_move = True

    if union_count == 1:
        return

    avg_population = sum_population // union_count
    for x, y in union:
        arr[x][y] = avg_population


def check(v):
    x, y = v
    if visited[x][y]:
        return False

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] == 0:
            if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                return True
    return False

arr = []
n, l, r = map(int, input().split())
for _ in range(n):
    arr.append(list(map(int, input().split())))
count = 0

while True:
    is_move = False
    visited = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check((i, j)):
                bfs((i, j))
    if is_move:
        count += 1
        continue
    else:
        break

print(count)
