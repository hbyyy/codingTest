n, m = map(int, input().split())

parent = [0] * (n + 1)
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i, n):
        if arr[i][j] == 1:
            parent[i+1] = i+1
            parent[j+1] = j+1


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, x, y):
    _x = find_parent(parent, x)
    _y = find_parent(parent, y)

    if _x < _y:
        parent[_y] = _x
    else:
        parent[_x] = _y


for i in range(n):
    for j in range(i, n):
        if arr[i][j]:
            union_find(parent, i + 1, j + 1)

towns = list(map(int, input().split()))
root = find_parent(parent, towns[0])
check = True
for i in range(1, len(towns)):
    if find_parent(parent, towns[i]) != root:
        check = False
        break

if check:
    print('YES')
else:
    print('NO')
