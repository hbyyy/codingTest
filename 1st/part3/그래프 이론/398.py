# 행성 터널
# O(n2) 이라 통과 못 한다

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


n = int(input())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

edges = []
locations = [[]]
for i in range(n):
    locations.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1, n + 1):
        edges.append((min(abs(locations[i][0] - locations[j][0]), abs(locations[i][1] - locations[j][1]),
                          abs(locations[i][2] - locations[j][2])), i, j))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    result += cost
    union_parent(parent, a, b)

print(result)
