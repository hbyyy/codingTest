from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        out = []

        def dfs(idx, count):
            if len(out) == count:
                answer.append(out[:])
                return
            for i in range(idx, len(nums)):
                out.append(nums[i])
                dfs(i + 1, count)
                out.pop()

        for i in range(len(nums) + 1):
            out.clear()
            dfs(0, i)
        return answer


## 빠른 풀이
## 조합을 구하면서 out 을 매번 answer 에 넣어주면 된다

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        out = []

        def dfs(idx):
            if len(out) == len(nums):
                return
            for i in range(idx, len(nums)):
                out.append(nums[i])
                answer.append(out[:])
                dfs(i + 1)
                out.pop()

        dfs(0)
        return answer


s = Solution()
s.subsets([1, 2, 3])
