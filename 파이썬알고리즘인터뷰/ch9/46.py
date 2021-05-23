from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        out = []
        visited = [0] * len(nums)

        def dfs(count):
            if count == len(nums):
                answer.append(out[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    out.append(nums[i])
                    dfs(count + 1)
                    visited[i] = 0
                    out.pop()

        dfs(0)
        return answer


s = Solution()
s.permute([1, 2, 3])
