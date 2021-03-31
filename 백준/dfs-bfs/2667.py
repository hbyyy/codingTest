# 단지 번호 붙이기
# 오타 주의하자

def dfs(v):
    x, y = v
    arr[x][y] = dangi
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1:
                dfs((nx, ny))


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dangi = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            dangi += 1
            dfs((i, j))

count = [0 for _ in range(dangi + 1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            count[arr[i][j]] += 1

count.sort()
print(dangi - 1)
for i in count:
    if i == 0:
        continue
    print(i)