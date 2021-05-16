"""
게임 개발
    난이도 2
    풀이시간 40분

예시:

input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

output
3
"""

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
mark_arr = [[0 for _ in range(m)] for _ in range(n)]
mark_arr[x][y] = 1
result = 1
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    for _ in range(4):
        d = d - 1 if d > 0 else 3
        nx, ny = x + dx[d], y + dy[d]
        if mark_arr[nx][ny] == arr[nx][ny] == 0:
            x = nx
            y = ny
            mark_arr[x][y] = 1
            result += 1
            break
    else:
        nx, ny = x - dx[d], y - dy[d]
        if arr[nx][ny] == 1:
            break
        x = nx
        y = ny

print(result)

