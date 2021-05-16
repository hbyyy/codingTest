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
    arr[x][y] = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                dfs((nx, ny))

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result += 1
            dfs((i, j))

print(result)