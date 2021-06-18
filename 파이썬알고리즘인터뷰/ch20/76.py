"""
76. Minimum Window Substring
"""


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         def check(sub_s: str, target: str) -> bool:
#             t_counter = Counter(target)
#             sub_counter = Counter(sub_s)
#             for c in set(target):
#                 try:
#                     if sub_counter[c] < t_counter[c]:
#                         return False
#                 except KeyError:
#                     return False
#             return True
#
#         i, j = 0, 0
#         answer = ''
#         while j <= len(s):
#             if j - i < len(t):
#                 j += 1
#                 continue
#
#             substring = s[i:j]
#             if check(substring, t):
#                 if not answer or len(substring) < len(answer):
#                     answer = substring
#                 i += 1
#             else:
#                 j += 1
#
#         return answer
# from collections import Counter
#
#
# def minWindow(s: str, t: str) -> str:
#     need = Counter(t)
#     missing = len(t)
#     left = start = end = 0
#
#     for right, char in enumerate(s, 1):
#         missing -= need[char] > 0
#         need[char] -= 1
#
#         if missing == 0:
#             while left < right and need[s[left]] != 0:
#                 need[s[left]] += 1
#                 left += 1
#
#             if not end or right - left <= end - start:
#                 start, end = left, right
#             need[s[left]] += 1
#             missing += 1
#             left += 1
#
    # return s[start:end]
from collections import Counter


def minWindow(s: str, t: str) -> str:
    def check(i, j, target: str) -> bool:
        t_counter = Counter(target)
        sub_counter = Counter(s[i:j])
        return t_counter & sub_counter == t_counter

    i, j = 0, 0
    answer = ''
    while j <= len(s):
        if j - i < len(t):
            j += 1
            continue

        # substring = s[i:j]
        if check(i, j, t):
            while i < j:
                if s[i] not in t:
                    i += 1
                else:
                    break
            if not answer or j - i < answer[j] - answer[i]:
                answer = (i, j)
            i += 1
        else:
            j += 1

    return s[answer[0]:answer[1]]

minWindow("ADOBECODEBANC",
          "ABC")