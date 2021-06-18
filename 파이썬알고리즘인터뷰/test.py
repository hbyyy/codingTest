def solution(rows, columns, queries):
    def rotate(p1, p2):
        x1, y1 = p1[0] - 1, p1[1] - 1
        x2, y2 = p2[0] - 1, p2[1] - 1
        prev = arr[x1 + 1][y1]
        min_value = prev

        # 위
        for i in range(y1, y2 + 1):
            arr[x1][i], prev = prev, arr[x1][i]
            min_value = min(min_value, prev)
        # 오른쪽
        for i in range(x1 + 1, x2 + 1):
            arr[i][y2], prev = prev, arr[i][y2]
            min_value = min(min_value, prev)

        # 아래
        for i in range(y2 - 1, y1 - 1, -1):
            arr[x1][i], prev = prev, arr[x1][i]
            min_value = min(min_value, prev)
        # 왼쪽
        for i in range(x2 - 1, x1 - 1, -1):
            arr[i][y2], prev = prev, arr[i][y2]
            min_value = min(min_value, prev)

        return min_value

    arr = []
    answer = []
    for i in range(rows):
        arr.append([*range(i * columns + 1 + 100, (i + 1) * columns + 1 + 100)])

    for query in queries:
        result = rotate(query[:2], query[2:])
        answer.append(result)
    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
