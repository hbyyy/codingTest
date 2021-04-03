from collections import deque

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
result = 0

n, a = int(input()), int(input())
arr = [[0] * n for _ in range(n)]

for _ in range(a):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

arr[0][0] = 2
bam = deque([(0, 0)])

L = int(input())
info = deque()
for _ in range(L):
    turn_info = input().split()
    info.append((int(turn_info[0]), turn_info[1]))

while True:
    nx, ny = bam[-1][0] + direction[d][0], bam[-1][1] + direction[d][1]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
        if arr[nx][ny] == 0:
            arr[nx][ny] = 2
            bam.append((nx, ny))
            arr[bam[0][0]][bam[0][1]] = 0
            bam.popleft()
        else:
            arr[nx][ny] = 2
            bam.append((nx, ny))

    else:
        result += 1
        break
    result += 1

    if info and info[0][0] == result:
        if info[0][1] == 'L':
            d = d - 1 if d != 0 else 3
        else:
            d = d + 1 if d != 3 else 0
        info.popleft()

print(result)
