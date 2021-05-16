# 찾으려는 수의 첫 점과 끝 점을 찾으면 된다.
# 수 찾아 그 위치부터 왼쪽, 오른쪽 끝 점 검색 -> O(N) 일 수 있어서 안됨

def search_left(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            if mid == 0:
                return mid
            else:
                if arr[mid - 1] != arr[mid]:
                    return mid
                else:
                    end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def search_right(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            if mid == len(arr) - 1:
                return mid
            else:
                if arr[mid + 1] != arr[mid]:
                    return mid
                else:
                    start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


n, t = map(int, input().split())
numbers = list(map(int, input().split()))

l = search_left(numbers, t, 0, len(numbers) - 1)
r = search_right(numbers, t, 0, len(numbers) - 1)
print(r - l + 1) if r >= 0 and l >= 0 else print(-1)