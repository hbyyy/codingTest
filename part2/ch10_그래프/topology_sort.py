from collections import deque

v, e = map(int, input().split())

in_degree = [0 for _ in range(v + 1)]
grape = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    grape[a].append(b)
    in_degree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in grape[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    return result


print(topology_sort())
