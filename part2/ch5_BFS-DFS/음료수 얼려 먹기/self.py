"""
예시
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

8
"""

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input())))


def dfs(v):
    x, y = v
    if arr[x][y] == 0:
        arr[x][y] = 1
        for nx, ny in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dx, dy = x + nx, y + ny
            if 0 <= dx < N and 0 <= dy < M:
                dfs((dx, dy))


result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            dfs((i, j))
            result += 1

print(result)
