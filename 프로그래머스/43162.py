def dfs(c, visited, computers):
    visited[c] = 1

    for i in range(len(computers)):
        if computers[c][i] == 1 and visited[i] == 0:
            dfs(i, visited, computers)


def solution(n, computers):
    result = 0
    visited = [0] * n
    is_continue = True
    for i in range(n):
        if visited[i] == 0:
            result += 1
            dfs(i, visited, computers)

    return result


# disjoint_set 사용
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


def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)

    for i in range(n):
        find_parent(parent, i)
    return len(set(parent))
