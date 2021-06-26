"""
맨해튼 거리    (r1, c1) <-> (r2, c2)
          :  |r1 - r2| + |c1 - c2|
"""


def check(place):
    for xy in range(5 * 5):
        x, y = xy // 5, xy % 5
        if place[x][y] == 'P':
            for dx, dy in [(0, -1), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if place[nx][ny] == 'P':
                        return False

            for i, (dx, dy) in enumerate([(0, -2), (2, 0), (0, 2)]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if place[nx][ny] == 'P':
                        if i == 0:
                            if place[nx][ny + 1] == 'O':
                                return False
                        elif i == 1:
                            if place[nx - 1][ny] == 'O':
                                return False
                        else:
                            if place[nx][ny - 1] == 'O':
                                return False

            for i, (dx, dy) in enumerate([(1, -1), (1, 1)]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if i == 0:
                        if place[nx][ny] == 'P':
                            if place[nx - 1][ny] == 'O' or place[nx][ny + 1] == 'O':
                                return False
                    else:
                        if place[nx][ny] == 'P':
                            if place[nx - 1][ny] == 'O' or place[nx][ny - 1] == 'O':
                                return False
    return True


def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))