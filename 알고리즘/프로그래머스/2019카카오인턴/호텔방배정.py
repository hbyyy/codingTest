from collections import defaultdict

# def solution(k, room_number):
#     answer = []
#     count_dict = defaultdict(int)
#     for i in room_number:
#         tmp = i
#         if not count_dict[tmp]:
#             answer.append(tmp)
#         else:
#             tmp += count_dict[tmp]
#             while True:
#                 if tmp not in answer:
#                     answer.append(tmp)
#                     break
#                 tmp += 1
#
#         count_dict[i] += 1
#
#     return answer

from collections import defaultdict

def solution(k, room_number):
    answer = []
    count_dict = defaultdict(int)
    for i in room_number:
        number = i
        if not count_dict[number]:
            answer.append(number)
            count_dict[i] = i + 1
        else:
            temp = [number]
            while True:
                number = count_dict[number]
                if not count_dict[number]:
                    answer.append(number)
                    count_dict[number] = number + 1
                    for j in temp:
                        count_dict[j] = number + 1
                    break
                else:
                    temp.append(number)
    return answer
solution(10	,[1,3,4,1,3,1])