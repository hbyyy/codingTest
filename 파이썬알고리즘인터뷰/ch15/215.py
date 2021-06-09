# import heapq
#
#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = [-n for n in nums]
#         heapq.heapify(nums)
#         for _ in range(k):
#             r = heapq.heappop(nums)
#         return -r

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(heapq.nlargest(k, nums))


s = Solution()
s.findKthLargest(
    [3, 2, 1, 5, 6, 4, 6, 6, 6, 6], 2)
