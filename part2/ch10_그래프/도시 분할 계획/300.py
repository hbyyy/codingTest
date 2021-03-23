n, m = map(int, input().split())
edges = []
parents = [0 for _ in range(n + 1)]
result = 0

for i in range(n + 1):
    parents[i] = i


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_find(parents, x, y):
    _x = find_parent(parents, x)
    _y = find_parent(parents, y)

    if _x < _y:
        parents[_y] = _x
    else:
        parents[_x] = _y


for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
max_load = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) == find_parent(parents, b):
        continue
    union_find(parents, a, b)
    max_load = cost
    result += cost

print(result - max_load)
