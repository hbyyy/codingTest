# 실패율

def solution(N, stages):
    fails = [-1 for _ in range(N + 1)]
    answer = []

    stages.sort()
    for i in range(len(stages)):
        if stages[i] == (N + 1):
            continue
        if fails[stages[i]] > -1:
            continue

        count = 1
        for j in range(i + 1, len(stages)):
            if stages[j] == stages[i]:
                count += 1

        fails[stages[i]] = count / len(stages[i:])

    for i in range(1, N + 1):
        if fails[i] < 0:
            answer.append((i, 0))
        else:
            answer.append((i, fails[i]))

    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in answer]
    return answer
