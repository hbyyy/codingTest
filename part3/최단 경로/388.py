# 화성 탐사
import heapq


def dijkstra(start):
    visited = [[0] * n for _ in range(n)]
    queue = []
    heapq.heappush(queue, (arr[start[0]][start[1]], start))
    distance[start[0]][start[1]] = arr[start[0]][start[1]]

    while queue:
        dist, location = heapq.heappop(queue)
        x, y = location
        if visited[x][y] == 1:
            continue

        visited[x][y] = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, (nx, ny)))


t = int(input())
INF = 1e9
for _ in range(t):
    n = int(input())
    arr = []
    distance = [[INF] * n for _ in range(n)]
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dijkstra((0, 0))
    print(distance[n-1][n-1])
