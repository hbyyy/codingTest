# def solution(n, k, cmd):
#     answer = ''
#     deleted = []
#     current_num = k
#
#     origin_table = {
#         0:'무지',
#         1:'콘',
#         2:'어피치',
#         3:'제이지',
#         4:'프로도',
#         5:'네오',
#         6:'튜브',
#         7:'라이언',
#
#     }
#     table = origin_table.copy()
#
#     for c in cmd:
#         if c[0] == 'D':
#             current_num += int(c[2])
#         elif c[0] == 'U':
#             current_num -= int(c[2])
#         elif c[0] == 'C':
#             if table.get(current_num + 1):
#                 tmp = current_num
#                 deleted.append([tmp, table[tmp]])
#                 while table.get(tmp + 1):
#                     table[tmp] = table[tmp + 1]
#                     tmp += 1
#                 del table[tmp]
#             else:
#                 deleted.append([current_num, table[current_num]])
#                 del table[current_num]
#                 current_num -= 1
#         else:
#             row, name = deleted.pop()
#             if table.get(row):
#                 table[len(table)] = ''
#                 tmp = table[row]
#                 for i in range(row + 1, len(table)):
#                     table[i], tmp = tmp, table[i]
#                 table[row] = name
#                 if current_num >= row:
#                     current_num += 1
#             else:
#                 table[len(table)] = name
#
#
#     deleted = [x[1] for x in deleted]
#     for i in range(n):
#         if origin_table[i] in deleted:
#             answer += 'X'
#         else:
#             answer += 'O'
#     return answer


def solution(n, k, cmd):
    answer = ''
    deleted = []
    current_num = k

    origin_table = {
        0: '무지',
        1: '콘',
        2: '어피치',
        3: '제이지',
        4: '프로도',
        5: '네오',
        6: '튜브',
        7: '라이언',

    }
    table = origin_table.copy()

    for c in cmd:
        if c[0] == 'D':
            k += int(c[2])
        elif c[0] == 'U':
            k -= int(c[2])
        elif c[0] == 'C':
            deleted.append([k, table[k]])
            if k == len(table) - 1:
                table.pop(k)
                k -= 1
            else:
                for i in range(k + 1, len(table)):
                    table[i - 1] = table[i]
                table.pop(len(table) - 1)
        else:
            row, name = deleted.pop()
            if table.get(row):
                table[len(table)] = ''
                tmp = table[row]
                for i in range(row + 1, len(table)):
                    table[i], tmp = tmp, table[i]
                table[row] = name
                if k >= row:
                    k += 1
            else:
                table[row] = name

    deleted = [x[1] for x in deleted]
    for i in range(n):
        if origin_table[i] in deleted:
            answer += 'X'
        else:
            answer += 'O'
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
