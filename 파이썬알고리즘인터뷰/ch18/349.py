from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def binary_search(a, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if a[mid] == target:
                    return a[mid]
                elif a[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        nums2.sort()
        answer = set()

        for n in nums1:
            result = binary_search(nums2, n, 0, len(nums2) - 1)
            if result is not None:
                answer.add(result)
        return answer
