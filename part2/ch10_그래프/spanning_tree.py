# 크루스칼 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    _x = find_parent(parent, x)
    _y = find_parent(parent, y)

    if _x < _y:
        parent[_y] = _x
    else:
        parent[_x] = _y


v, e = map(int, input().split())
parent = [0 for _ in range(v + 1)]

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    result += cost

print(result)



