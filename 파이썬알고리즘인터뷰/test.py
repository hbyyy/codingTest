# 프로그래머스 행렬 테두리 회전하기

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

# 프로그래머스 카카오 2018 캐시
from collections import Counter


def solution(cacheSize, cities):
    def cache_update(c):
        for k in c.keys():
            c[k] += 1

    if not cacheSize:
        return len(cities) * 5

    answer = 0
    cache = Counter()

    for city in cities:
        cache_update(cache)
        if city in cache:
            cache[city] = 0
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache[city] = 0
            else:
                out = cache.most_common(1)[0]
                cache.pop(out)
                cache[city] = 0
            answer += 5

    return answer


solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
             "Rome"])
solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
             "Rome"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])


# 프로그래머스 카카오 2018 프렌즈4블록
def solution(m, n, board):
    def f(i, j):
        crash_indexes = []
        for x in range(i, m - 1):
            for y in range(n - 1):
                if board[x][y] == '-':
                    continue
                if board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1]:
                    crash_indexes += [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]

        for x, y in set(crash_indexes):
            board[x][y] = '-'

        for y in range(n):
            tmp = ''.join([board[i][y] for i in range(m - 1, -1, -1)]).replace('-', '')
            idx = m - 1
            for c in tmp:
                board[idx][y] = c
                idx -= 1
            for x in range(idx, -1, -1):
                board[x][y] = '-'

    board = [list(b) for b in board]
    while True:
        end = True
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == '-':
                    continue
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    f(i, j)
                    end = False
                    break
        if end:
            break

    return sum(x.count('-') for x in board)


# 프로그래머스 카카오 2018 프렌즈4블록 모범답안
def solution(m, n, board):
    board = [list(b) for b in board]

    matched = True
    while matched:
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != '-':
                    matched.append((i, j))

        for x, y in matched:
            board[x][y] = board[x + 1][y] = board[x + 1][y + 1] = board[x][y + 1] = '-'

        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '-':
                        board[i + 1][j], board[i][j] = board[i][j], '-'
    return sum(x.count('-') for x in board)


solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
