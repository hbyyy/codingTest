# 삼각 달팽이
"""
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

입출력 예
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
"""


def fill_arr(arr, n, start_number, start_x, start_y):
    number = start_number
    for i in range(start_x, start_x + n):
        arr[i][start_y] = number
        number += 1

    for i in range(start_y + 1, n + start_y):
        arr[n + start_x - 1][i] = number
        number += 1

    for i in range(n + start_x - 2, start_x, -1):
        arr[i][-1 - start_y] = number
        number += 1

    if n < 3:
        return

    if arr[start_x + 2][start_y + 1] == 0:
        fill_arr(arr, n - 3, number, start_x + 2, start_y + 1)
    else:
        return


def solution(n):
    arr = []
    for i in range(1, n + 1):
        arr.append([0] * i)

    fill_arr(arr, n, 1, 0, 0)

    answer = []
    for i in arr:
        answer.extend(i)
    return answer


tmp = solution(6)
for i in tmp:
    print(i)
