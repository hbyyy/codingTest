"""
56. Merge Intervals
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = []

        for i in intervals:
            if answer and i[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], i[1])
            else:
                answer += i,
        return answer
