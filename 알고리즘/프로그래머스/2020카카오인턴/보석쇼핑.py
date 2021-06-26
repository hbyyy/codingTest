# def solution(gems):
#     all_gem = set(gems)
#     answer = []
#     min_range = 1e9
#
#     for i in range(len(gems) - len(all_gem) + 1):
#         tmp = [i]
#         buy_gems = {gems[i]}
#         for j in range(i, len(gems)):
#             buy_gems.add(gems[j])
#             if len(buy_gems) == len(all_gem):
#                 tmp.append(j)
#                 break
#         if len(tmp) < 2:
#             break
#         else:
#             if tmp[1] - tmp[0] < min_range:
#                 answer = tmp
#                 min_range = tmp[1] - tmp[0]
#             else:
#                 continue
#
#
#     return [i + 1 for i in answer]


def solution(gems):
    all_gems = set(gems)
    answer = []

    start, end = 0, 0

    if len(all_gems) == 1:
        return [1, 1]
    else:
        while end < len(gems) - len(all_gems) + 1:
            tmp = set()
            while end < len(gems):
                tmp.add(gems[end])
                if len(tmp) == len(all_gems):
                    break
                else:
                    end += 1

            if end == len(gems):
                break

            while start < end:
                if len(set(gems[start + 1: end + 1])) == len(all_gems):
                    start += 1
                else:
                    break

            if answer:
                if answer[1] - answer[0] > end - start:
                    answer = [start, end]
            else:
                answer = [start, end]
            start += 1
            end = start
        return [answer[0] +1, answer[1] + 1]



print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
