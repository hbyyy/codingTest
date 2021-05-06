import random
from collections import deque


def set_minefield(n, mine_n):
    arr = [[0] * n for _ in range(n)]
    mine = []

    dxdy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), ]

    count = 0
    while count < mine_n:
        x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        if (x, y) not in mine:
            mine.append((x, y))
            count += 1

    for x, y in mine:
        arr[x][y] = 'm'
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 'm':
                arr[nx][ny] += 1
    return arr, mine


def process(x, y, arr, check_arr):
    dxdy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), ]

    if arr[x][y] != 0:
        check_arr[x][y] = True
        return

    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        check_arr[x][y] = True
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr) and not check_arr[nx][ny]:
                check_arr[nx][ny] = True
                if arr[nx][ny] == 0:
                    queue.append((nx, ny))


def answer_check(mine_idx, check_arr):
    for i in range(len(check_arr)):
        for j in range(len(check_arr)):
            if (i, j) in mine_idx:
                continue
            if check_arr[i][j] is False:
                return False

    for x, y in mine_idx:
        check_arr[x][y] = True
    return True


def print_minefield(arr, check_arr):
    for i in range(1, len(check_arr) + 1):
        if i == 1:
            print('\t', end=' ')
        print(f' {i:<2}', end='')
    print('\n')

    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == 0:
                print(f'{i + 1:>2}\t', end=' ')
            if check_arr[i][j] is False:
                print(' *', end=' ')
            else:
                print(f' {arr[i][j]}', end=' ')
        print()
    print()


if __name__ == '__main__':
    while True:
        n = int(input('필드 크기를 입력해주세요 (n >= 10) : '))
        mine_n = int(input('지뢰 갯수를 입력해주세요 n >= 10 : '))
        if n < 10 or mine_n < 10:
            print('제대로된 값을 넣어주세요 (10 이상의 값)')
            continue
        break

    minefield, mine_idx = set_minefield(n, mine_n)
    check_arr = [[False] * n for _ in range(n)]
    end = False

    print('시작합니다!')
    print_minefield(minefield, check_arr)

    while not end:
        x, y = map(int, input('클릭할 셀의 인덱스를 입력해주세요 (ex: 1 3) : ').split())
        x -= 1
        y -= 1
        if x < 0 and x >= n and y < 0 and y >= n:
            print(f'인덱스를 정확히 입력해주세요 (1 <= x <= {n}, 1 <= y <= {n})')
            continue

        if minefield[x][y] == 'm':
            print('지뢰입니다! 게임 종료')
            break
        elif check_arr[x][y]:
            print('이미 선택했던 위치입니다. 다시 선택해 주세요')
        else:
            process(x, y, minefield, check_arr)
            print_minefield(minefield, check_arr)

        if answer_check(mine_idx, check_arr):
            print_minefield(minefield, check_arr)
            print('승리했습니다!')
            break
