# 벽 세우는 기법 체크!
# 풀었다..!

import sys

input = sys.stdin.readline


def check(arr):
    teacher_idx = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                teacher_idx.append((i, j))

    for x, y in teacher_idx:
        for i in range(x, n):
            if arr[i][y] == 'O':
                break
            if arr[i][y] == 'S':
                return False
        for i in range(x, -1, -1):
            if arr[i][y] == 'O':
                break
            if arr[i][y] == 'S':
                return False
        for i in range(y, n):
            if arr[x][i] == 'O':
                break
            if arr[x][i] == 'S':
                return False
        for i in range(y, -1, -1):
            if arr[x][i] == 'O':
                break
            if arr[x][i] == 'S':
                return False
    return True


def dfs(count):
    global result
    if count == 3:
        if check(origin_arr) is True:
            result = True
    else:
        for i in range(n):
            for j in range(n):
                if origin_arr[i][j] == 'X':
                    origin_arr[i][j] = 'O'
                    count += 1
                    dfs(count)
                    origin_arr[i][j] = 'X'
                    count -= 1


n = int(input())
origin_arr = []
result = False

for _ in range(n):
    origin_arr.append(list(input().split()))

dfs(0)
print("YES") if result else print("NO")