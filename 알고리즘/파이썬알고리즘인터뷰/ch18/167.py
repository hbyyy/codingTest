"""
167. Two Sum II - Input array is sorted
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            expected = target - n

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]
