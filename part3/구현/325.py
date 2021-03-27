# def rotate(arr, n):
#     tmp = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             tmp[j][n - 1 - i] = arr[i][j]
#
#     return tmp
#
#
# def check(key, hom):
#     hom_x = len(hom)
#     hom_y = len(hom[0])
#     check = False
#
#     for i in range(len(key) - hom_x + 1):
#         for j in range(len(key) - hom_y + 1):
#             for k in range(hom_x):
#                 for g in range(hom_y):
#
#
#     return check
#
#
# def check_hom(arr, n):
#     tmp = []
#     min_x = n
#     min_y = n
#     max_x = 0
#     max_y = 0
#
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 0:
#                 min_x = min(min_x, i)
#                 min_y = min(min_y, j)
#                 max_x = max(min_x, i)
#                 max_y = max(min_y, j)
#
#     for i in range(min_x, max_x + 1):
#         tmp.append(arr[i][min_y:max_y + 1])
#
#     return tmp
#
#
# def solution(key, lock):
#     answer = False
#     hom = check_hom(lock)
#
#     for i in range(3):
#         key = rotate(key, len(key))
#         answer = check(key, hom)
#         if answer:
#             break
#
#     return answer


# 모범 답안
import copy


def rotate(arr, n):
    rotate_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotate_arr[j][n - 1 - i] = arr[i][j]

    return rotate_arr


def check(key, extend_arr, n):
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if extend_arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    extend_arr = [[0] * (3 * n) for _ in range(3 * n)]

    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            extend_arr[i][j] = lock[i % n][j % n]

    for i in range(4):
        for i in range(2 * n):
            for j in range(2 * n):
                check_arr = copy.deepcopy(extend_arr)

                for k in range(len(key)):
                    for g in range(len(key)):
                        check_arr[i + k][j + g] += key[k][g]

                if check(key, check_arr, n) is True:
                    return True
        key = rotate(key, len(key))
    return False


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
