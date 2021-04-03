def is_possible(construct):
    for x, y, t in construct:
        if t == 0:
            if y == 0 or [x - 1, y, 1] in construct or [x, y, 1] in construct or [x, y - 1, 0] in construct:
                continue
            else:
                return False
        else:
            if [x, y - 1, 0] in construct or [x + 1, y - 1, 0] in construct or (
                    [x - 1, y, 1] in construct and [x + 1, y, 1] in construct):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if is_possible(answer) is False:
                answer.pop()
        else:
            answer.remove([x, y, a])
            if is_possible(answer) is False:
                answer.append([x, y, a])
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
