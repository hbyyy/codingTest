# 내 풀이
n = int(input())
x = y = 0

for c in list(input().split()):
    if c == "L":
        y = y - 1 if y > 0 else y
    elif c == "R":
        y = y + 1 if y < n - 1 else y
    elif c == "U":
        x = x - 1 if x > 0 else x
    else:
        x = x + 1 if x < n - 1 else x

print(x + 1, y + 1)

# 책
"""
    dx, dy 로 활용하는 부분이 유용할 것 같다
    (대각선 이동 같은 기능이 필요할 때 유용할듯)
"""
n = int(input())
plans = input().split()
x = y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny < n:
        continue
    x += nx
    y += ny

print(x, y)
