# # 간단한 다익스트라 알고리즘
# # 간단하지만 느림
# # O(V2)
# # 노드가 5,000개 이하이면 이것으로 가능, 10,000개가 넘어간다면 이 방법은 패스해야 한다
# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
#
# start = int(input())
# graph = [[] for _ in range(n + 1)]
#
# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
#
# dijkstra(start)
#
# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print('INFINITY')
#     else:
#         print(distance[i])
#
# # 개선된 다익스트라 알고리즘
# # O(ElogV)
#
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
#
# def dijkstra2(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#
# dijkstra2(start)
#
# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print('INFINITY')
#     else:
#         print(distance[i])
import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node(distance, visited):
    smallest = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < smallest and not visited[i]:
            smallest = distance[i]
            idx = i
    return idx


def dijkstra(start):
    visited = [0 for _ in range(n + 1)]
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    visited[start] = 1

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node(distance, visited)
        visited[now] = True
        for v in graph[now]:
            cost = distance[now] + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost

    return distance


print(dijkstra(start))


INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra2(start):
    visited = [0 for _ in range(n + 1)]
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        dist, now = heapq.heappop(queue)
        if visited[now] == 1:
            continue

        visited[now] = 1
        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(queue, (cost, v[0]))

    return distance


print(dijkstra2(start))
