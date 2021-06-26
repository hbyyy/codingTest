"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        out = []

        def dfs(idx, result):
            if result >= target:
                if result == target:
                    answer.append(out[:])
                return
            for i in range(idx, len(candidates)):
                out.append(candidates[i])
                dfs(i, result + candidates[i])
                out.pop()

        dfs(0, 0)
        return answer


# 책 풀이
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(csum, idx, result):
            if csum < 0:
                return
            elif csum == 0:
                answer.append(result)
                return

            for i in range(idx, len(candidates)):
                dfs(csum - candidates[i], i, result + [candidates[i]])

        dfs(target, 0, [])
        return answer
