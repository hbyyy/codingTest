def check(l, r, target):
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == l:
                l_index = (i, j)
            if board[i][j] == r:
                r_index = (i, j)
            if board[i][j] == target:
                target_index = (i, j)

    if target_index[1] == 0:
        return 1
    elif target_index[1] == 2:
        return 2
    else:
        l_distance = abs(target_index[0] - l_index[0]) + abs(target_index[1] - l_index[1])
        r_distance = abs(target_index[0] - r_index[0]) + abs(target_index[1] - r_index[1])
        if l_distance == r_distance:
            return 0
        elif l_distance < r_distance:
            return 1
        else:
            return 2


def solution(numbers, hand):
    answer = []
    l_thumb = '*'
    r_thumb = '#'

    for i in numbers:
        flag = check(l_thumb, r_thumb, i)

        if flag == 0:
            if hand == 'left':
                l_thumb = i
                answer.append('L')
            else:
                r_thumb = i
                answer.append('R')
        elif flag == 2:
            r_thumb = i
            answer.append('R')
        else:
            l_thumb = i
            answer.append('L')

    return ''.join(answer)
