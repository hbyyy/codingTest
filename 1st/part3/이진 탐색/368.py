# 고정점 찾기


def search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


n = int(input())
numbers = list(map(int, input().split()))

result = search(numbers, 0, n - 1)

print(result) if result >= 0 else print(-1)
