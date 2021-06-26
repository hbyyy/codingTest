def solution(answers):
    answer = [[1, 0], [2, 0], [3, 0]]
    one = '12345' * ((5 // len(answer)) + 1)
    two = '21232425' * ((8 // len(answer)) + 1)
    three = '3311224455' * ((10 // len(answer)) + 1)

    for a, b, c, d in zip(answers, one, two, three):
        if a == int(b):
            answer[0][1] += 1
        if a == int(c):
            answer[1][1] += 1
        if a == int(d):
            answer[2][1] += 1

    result = []
    cnt = 0
    answer.sort(key=lambda x:x[1], reverse=True)
    return answer
#     for i in range(1, 3):
#         if answer[i][1] == answer[0][1]:
#             cnt += 1

#     result = [answer[i][0] for i in range(cnt)]
#     return result

solution([1,2,3,4,5])