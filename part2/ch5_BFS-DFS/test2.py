# 재귀 함수
"""
종료 조건 명시가 중요

"""

# 팩토리얼
from collections import deque
from time import time


def f(x):
    if x == 0 or x == 1:
        return 1
    return x * f(x - 1)


print(f(10))

# dfs 기본
# p 137 의 그래프
# 각 행의 0 index, 1행은 이용하지 않지만, 인덱스 (노드가 1부터 시작) 맞추기 편하게 하기 위해 이렇게 인접 행렬을 만드는 게 좋다
graph1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
]

# 마찬가지로 graph2[0] 은 빈 배열 (노드는 1부터 시작) 로 만들어 놓으면 편하다
graph2 = [
    [],
    [2, 3, 8],  # 1
    [1, 7],  # 2
    [1, 4, 5],  # 3
    [3, 5],  # 4
    [3, 4],  # 5
    [7],  # 6
    [2, 6, 8],  # 7
    [1, 7]  # 8
]

visited = [0 for _ in range(8 + 1)]


# 인접 행렬 사용
def dfs1(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, 8 + 1):
        if graph1[v][i] == 1 and visited[i] == 0:
            dfs1(i)


time1 = time()
dfs1(1)
time2 = time()
print(time2 - time1)
visited = [0 for _ in range(8 + 1)]


# 인접 리스트 사용
def dfs2(v):
    visited[v] = 1
    print(v, end=' ')
    for node in graph2[v]:
        if visited[node] == 0:
            dfs2(node)


time1 = time()
dfs2(1)
time2 = time()
print(time2 - time1)


# 재귀없이

def dfs3(v):
    stack = [v]
    visited = [0 for _ in range(8 + 1)]

    while stack:
        node = stack.pop()
        if visited[node] == 0:
            tmp = []
            visited[node] = 1
            print(node, end=' ')
            for i in range(1, 8 + 1):
                if graph1[node][i] == 1:
                    tmp.append(i)
            stack.extend(tmp[::-1])


time1 = time()
dfs3(1)
time2 = time()
print(time2 - time1)


def dfs4(v):
    stack = [v]
    visited = [0 for _ in range(8 + 1)]

    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            print(node, end=' ')
            stack.extend(graph2[node][::-1])


time1 = time()
dfs4(1)
time2 = time()
print(time2 - time1)

graph3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
]

# 마찬가지로 graph2[0] 은 빈 배열 (노드는 1부터 시작) 로 만들어 놓으면 편하다
graph4 = [
    [],
    [2, 3, 8],  # 1
    [1, 7],  # 2
    [1, 4, 5],  # 3
    [3, 5],  # 4
    [3, 4],  # 5
    [7],  # 6
    [2, 6, 8],  # 7
    [1, 7]  # 8
]


def bfs1(v):
    queue = deque([v])
    visited = [0 for _ in range(8 + 1)]

    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            print(node, end=' ')
            visited[node] = 1
            for i in range(1, 8 + 1):
                if graph3[node][i] == 1:
                    queue.append(i)


time1 = time()
bfs1(1)
time2 = time()
print(time2 - time1)


def bfs2(v):
    queue = deque([v])
    visited = [0 for _ in range(8 + 1)]

    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            print(node, end=' ')
            visited[node] = 1
            queue.extend(graph4[node])


time1 = time()
bfs2(1)
time2 = time()
print(time2 - time1)


def bfs3(v):
    queue = deque([v])
    visited = [0 for _ in range(8 + 1)]
    visited[v] = 1
    print(v, end=' ')

    while queue:
        node = queue.popleft()
        for v in graph4[node]:
            if visited[v] == 0:
                visited[v] = 1
                print(v, end=' ')
                queue.append(v)


time1 = time()
bfs1(3)
time2 = time()
print(time2 - time1)
