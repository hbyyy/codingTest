# 이진 탐색

arr = [1, 2, 4, 5, 7, 8, 15, 36, 39]


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


print(binary_search(arr, 5, 0, len(arr) - 1))


def binary_search2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


print(binary_search2(arr, 5, 0, len(arr) - 1))
