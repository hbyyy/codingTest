nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
left, right = 0, len(nums) - 1

while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

pivot = left
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    mid_pivot = (pivot + mid) % len(nums)
    if nums[mid_pivot] < target:
        left = mid + 1
    elif nums[mid_pivot] > target:
        right = mid - 1
    else:
        print(mid_pivot)
        break
# print(-1)
