import sys
sys.setrecursionlimit(100000)

result = 1e9

def f(v, n, direction, tmp, board):
    global result

    x, y = v
    if (x, y) == (n - 1, n - 1):
        result = min(result, tmp)
    else:
        for d, (dx, dy) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < n) and board[nx][ny] != 1:
                if d == direction:
                    f((nx, ny), n, d, tmp + 100, board)
                else:
                    f((nx, ny), n, d, tmp + 100 + 500, board)



def solution(board):
    global result

    f((0, 1), len(board), 1, 100, board)
    f((1, 0), len(board), 2, 100, board)

    answer = 0
    return result

print(solution([[0,0,0],[0,0,0],[0,0,0]]))