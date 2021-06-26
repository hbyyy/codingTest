# 최소 신장 트리를 만들면 됨
# 사용하지 않은 엣지의 비용을 합하면 최대 절약 금액!


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


n, m = map(int, input().split())

result = 0
parent = [0] * n
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

for i in range(n):
    parent[i] = i

edges.sort()

for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) == find_parent(parent, y):
        result += cost
        continue
    union_parent(parent, x, y)

print(result)