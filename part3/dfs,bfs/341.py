# 내 풀이
import copy
import sys

input = sys.stdin.readline


def sec_area(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                count += 1
    return count


def dfs(arr, v):
    x, y = v

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                dfs(arr, (nx, ny))


original_arr = []
n, m = map(int, input().split())
for _ in range(n):
    original_arr.append(list(map(int, input().split())))

result = 0
zero_idx = []
for i in range(n):
    for j in range(m):
        if original_arr[i][j] == 0:
            zero_idx.append((i, j))

for a in range(len(zero_idx)):
    for b in range(a + 1, len(zero_idx)):
        for c in range(b + 1, len(zero_idx)):
            wall_arr = copy.deepcopy(original_arr)
            wall_arr[zero_idx[a][0]][zero_idx[a][1]] = 1
            wall_arr[zero_idx[b][0]][zero_idx[b][1]] = 1
            wall_arr[zero_idx[c][0]][zero_idx[c][1]] = 1
            for i in range(n):
                for j in range(m):
                    if wall_arr[i][j] == 2:
                        dfs(wall_arr, (i, j))
            result = max(result, sec_area(wall_arr))
print(result)

# 모범 답안
import sys

input = sys.stdin.readline


def sec_area(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                count += 1
    return count


def virus(arr, v):
    x, y = v

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                virus(arr, (nx, ny))

# 조합 선택하는 dfs 기법
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp_arr[i][j] = original_arr[i][j]

        for i in range(n):
            for j in range(m):
                if tmp_arr[i][j] == 2:
                    virus(tmp_arr, (i, j))
        result = max(result, sec_area(tmp_arr))
        return
    for i in range(n):
        for j in range(m):
            if original_arr[i][j] == 0:
                original_arr[i][j] = 1
                count += 1
                dfs(count)
                original_arr[i][j] = 0
                count -= 1


original_arr = []

n, m = map(int, input().split())
for _ in range(n):
    original_arr.append(list(map(int, input().split())))
tmp_arr = [[0] * len(original_arr[0]) for _ in range(len(original_arr))]
result = 0

dfs(0)
print(result)
