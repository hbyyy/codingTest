n = int(input())

movements = list(input().split())

i, j = 1, 1
direction = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

for move in movements:
    di, dj = direction[move]
    ni, nj = i + di, j + dj
    if 0 < ni <= n and 0 < nj <= n:
        i, j = ni, nj

print(ni, nj)
