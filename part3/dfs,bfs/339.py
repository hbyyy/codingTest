# from collections import deque
#
# n, m, k, x = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
# visited = [0 for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
#
# def bfs(v):
#     queue = deque([v])
#     visited[v] = 0
#
#     while queue:
#         node = queue.popleft()
#         for i in graph[node]:
#             if visited[i] == 0:
#                 visited[i] = visited[node] + 1
#                 queue.append(i)
#                 if visited[i] == k:
#                     print(i, end=' ')
#
#
#
# bfs(x)
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)
                if visited[i] == k:
                    result.append(i)


result = []
bfs(x)
if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)
