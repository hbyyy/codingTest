n = int(input())
board = [[0] * n for _ in range(n)]
result = 0


def f(count, x, y):
    global result

    if count == n:
        result += 1
        return
    for i in range(x, n):
        for j in range(n):
            if board[i][j] == 0:
                if check(i, j):
                    board[i][j] = 1
                    f(count + 1, i, j)
                    board[i][j] = 0


def check(x, y):
    for i in range(n):
        if board[i][y] == 1 or board[x][i] == 1:
            return False

    dxdy = [(-1, 1), (1, -1), (1, 1), (-1, -1)]
    for dx, dy in dxdy:
        i, j = x, y
        while True:
            i += dx
            j += dy
            if not (0 <= i < n and 0 <= j < n):
                break
            if board[i][j] == 1:
                return False
    return True


f(0, 0, 0)
print(result)
