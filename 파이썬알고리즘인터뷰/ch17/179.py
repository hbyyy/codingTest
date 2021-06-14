from functools import cmp_to_key
from typing import List


# 내장 sort 이용
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def f(x1, x2):
            return int(x2 + x1) - int(x1 + x2)

        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(f))

        answer = ''.join(nums)
        return str(int(''.join(nums)))


# 정렬 구현해 이용
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(n) for n in nums]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        answer = ''.join(nums)
        return str(int(''.join(answer)))
