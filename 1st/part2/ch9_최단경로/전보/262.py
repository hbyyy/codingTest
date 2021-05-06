import heapq
import sys

INF = 1e9
input = sys.stdin.readline
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

    return distance


distances = dijkstra(start)
count = 0
max_time = 0

for i in range(1, n + 1):
    if distances[i] == 0 or distances[i] == INF:
        continue
    count += 1
    max_time = max(distances[i], max_time)

print(count, max_time)
