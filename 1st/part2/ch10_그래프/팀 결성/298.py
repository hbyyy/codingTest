n, m = map(int, input().split())
parents = [0 for _ in range(n + 1)]


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


for i in range(n + 1):
    parents[i] = i

for i in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union_find(parents, a, b)
    else:
        if find_parent(parents, a) == find_parent(parents, b):
            print('YES')
        else:
            print('NO')
