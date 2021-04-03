#베스트앨범

def solution(genres, plays):
    tmp = {}
    for i in range(len(genres)):
        if not tmp.get(genres[i]):
            tmp[genres[i]] = [plays[i], [(i, plays[i]), ], ]
        else:
            tmp[genres[i]][0] += plays[i]
            tmp[genres[i]][1].append((i, plays[i]))

    result = [x for x in tmp.values()]

    answer = []
    result.sort()
    for i in result:
        i[1].sort(key=lambda x: x[1], reverse=True)
        if len[i[1]] < 2:
            answer.append(i[1][1])
        else:
            answer.append(i[1][1])
            answer.append(i[1][2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))