# """
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["*rodo", "*rodo", "******"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "*rodo", "******", "******"]	3
# """

# 내 풀이 (시간 아슬아슬하다)
from itertools import product


def check(u_id, b_id):
    if len(u_id) != len(b_id):
        return False
    for a, b in zip(u_id, b_id):
        if a != b and b != '*':
            return False
    return True


def solution(user_id, banned_id):
    tmp = {}
    for id in banned_id:
        tmp[id] = []

    for b_id in banned_id:
        if tmp[b_id]:
            continue
        for u_id in user_id:
            if check(u_id, b_id):
                tmp[b_id].append(u_id)

    result = set()
    for i in list(product(*[tmp[b_id] for b_id in banned_id])):
        if len(set(i)) != len(i):
            continue
        result.add(frozenset(i))
    return len(result)


print(solution(["frodo", "fradi", "crodo", "abc23", "frodc", "croda", "abc41", "frod2"],
               ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "*****"]))

# 모범 답안
# def combi(temp, number, calculate):
#     global result
#     if len(temp) == len(calculate):
#         temp = set(temp)
#         if temp not in result:
#             result.append(temp)
#         return
#     else:
#         for j in range(len(calculate[number])):
#             if calculate[number][j] not in temp:
#                 temp.append(calculate[number][j])
#                 combi(temp, number+1, calculate)
#                 temp.pop()
# result = []
# def solution(user_id, banned_id):
#     global result
#     calculate = []
#     for ban in banned_id:
#         possible=[]
#         for user in user_id:
#             if len(ban) != len(user):
#                 continue
#             else:
#                 count = 0
#                 for i in range(len(ban)):
#                     if user[i] == ban[i]:
#                         count+=1
#                 if count == len(ban)-ban.count('*'):
#                     possible.append(user)
#         calculate.append(possible)
#
#     combi([], 0, calculate)
#     return len(result)
#
# print(solution(["frodo", "fradi", "crodo", "abc23", "frodc", "croda", "abc41", "frod2"], ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "*****"]))
