# # from collections import deque
# #
# # queue = deque([1, 2, 3, 4, 5])
# # # queue.extend([1, 2, 3, 4, 5])
# # print(queue)
# # queue.rotate(1)
# # print(queue)
# # print(queue)
# # print([x for x in queue])
# #
# #
# # def recursive(i):
# #     if i == 100:
# #         return
# #
# #     print(f'{i} 번째에서 {i + 1} 번째를 호출합니다')
# #     recursive(i + 1)
# #     print(f'{i}번째 종료')
# #
# #
# # def factorial_recursive(n):
# #     if n <= 1:
# #         return 1
# #     return n * factorial_recursive(n - 1)
# #
# #
# # # 노드가 3개인 그래프의 인접 행렬, 리스트
# # """
# #      0
# #   /(7)  |(5)
# #   1     2
# # """
# # INF = 999999
# # graph1 = [
# #     [0, 7, 5],
# #     [7, 0, INF],
# #     [5, INF, 0],
# # ]
# #
# # graph2 = [[] for _ in range(3)]
# # graph2[0].append((1, 7))
# # graph2[0].append((2, 5))
# #
# # graph2[1].append((0, 7))
# #
# # graph2[2].append((0, 5))
# #
# # print(graph1)
# # print(graph2)
# #
# # # DFS 기본
# # visited = [0 for _ in range(8 + 1)]
# # graph3 = [
# #     [],
# #     [2, 3, 8],
# #     [1, 7],
# #     [1, 4, 5],
# #     [3, 5],
# #     [3, 4],
# #     [7],
# #     [2, 6, 8],
# #     [1, 7],
# # ]
# #
# #
# # def dfs(graph, v, visited):
# #     visited[v] = 1
# #     print(v, end=' ')
# #     for i in graph[v]:
# #         if not visited[i]:
# #             dfs(graph, i, visited)
# #
# #
# # dfs(graph3, 1, visited)
# #
# # # BFS 기본
# # visited = [0 for _ in range(8 + 1)]
# # graph4 = [
# #     [],
# #     [2, 3, 8],
# #     [1, 7],
# #     [1, 4, 5],
# #     [3, 5],
# #     [3, 4],
# #     [7],
# #     [2, 6, 8],
# #     [1, 7],
# # ]
# #
# # print()
# #
# #
# # def bfs(graph, v):
# #     queue = deque([v])
# #     visited = [0 for _ in range(8 + 1)]
# #     visited[v] = 1
# #
# #     while queue:
# #         node = queue.popleft()
# #         print(node, end=' ')
# #         for i in graph4[node]:
# #             if not visited[i]:
# #                 queue.append(i)
# #                 visited[i] = True
# #
# #
# # bfs(graph4, 1)
#
# from collections import deque
#
# N, M, K, X = map(int, input().split())
# graph = [[0] * (N + 1) for _ in range(N + 1)]
# arr = [[0] * (N + 1) for _ in range(N + 1)]
#
# for _ in range(M):
#     x, y = map(int, input().split())
#     graph[x][y] = 1
#
#
# def bfs(start_node):
#     queue = deque([start_node])
#     visited = [0] * (N + 1)
#     visited[start_node] = 1
#
#     while queue:
#         node = queue.popleft()
#         for v, e in enumerate(graph[node]):
#             if e:
#                 visited[e] = min(visited[e], visited[node] + 1) if visited[e] == 0 else visited[node] + 1
#                 queue.append(v)
#     return visited
#
#
# result = bfs(X)
# count = 0
# for i in range(1, N + 1):
#     if result[i] == K:
#         count += 1
#         print(i)
# if count == 0:
#     print(-1)

from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

virus_index = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus_index.append((i, j))


def dfs(x, y):
    graph[x][y] = 2
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dfs(nx, ny)


for x, y in virus_index:
    dfs(x, y)

count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
print(count)