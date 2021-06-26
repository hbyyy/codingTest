# from itertools import permutations
#
# def ex_parse(expression):
#     parsed_ex = ['']
#     for c in expression:
#         if c.isdigit():
#             if parsed_ex[-1].isdigit():
#                 parsed_ex[-1] += c
#             else:
#                 parsed_ex.append(c)
#         elif c in '*+-':
#             parsed_ex.append(c)
#
#     return parsed_ex[1:]
#
#
# def solution(expression):
#     answer = 0
#     op_list = []
#     for ex in ['-', '*', '+']:
#         if expression.find(ex) >= 0:
#             op_list.append(ex)
#
#     for operators in permutations(op_list):
#         tmp = ex_parse(expression)
#         for operator in operators:
#             while True:
#                 try:
#                     idx = tmp.index(operator)
#                     print(tmp, idx, operator)
#                     tmp = tmp[:idx - 1] + [eval(f'{tmp[idx-1]}{operator}{tmp[idx+1]}')] + tmp[idx + 2:]
#                 except ValueError:
#                     break
#         return tmp
#
#
#
#     return answer
from itertools import permutations


def ex_parse(expression):
    parsed_ex = ['']
    for c in expression:
        if c.isdigit():
            if parsed_ex[-1].isdigit():
                parsed_ex[-1] += c
            else:
                parsed_ex.append(c)
        elif c in '*+-':
            parsed_ex.append(c)

    return parsed_ex[1:]


def solution(expression):
    answer = 0
    op_list = []
    for ex in ['-', '*', '+']:
        if expression.find(ex) >= 0:
            op_list.append(ex)

    for operators in permutations(op_list):
        tmp = ex_parse(expression)
        for i in range(len(operators) - 1):
            while True:
                try:
                    idx = tmp.index(operators[i])
                    tmp = tmp[:idx - 1] + [str(eval(f'{tmp[idx - 1]}{operators[i]}{tmp[idx + 1]}'))] + tmp[idx + 2:]
                    # print(tmp)
                except ValueError:
                    break
        answer = max(answer, abs(eval(''.join(tmp))))

    return answer


print(solution("100-200*300-500+20"))
