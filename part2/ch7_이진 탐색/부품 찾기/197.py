N = int(input())
stuffs = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

stuffs.sort()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for order in orders:
    check = binary_search(stuffs, order, 0, N - 1)
    if check:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수 정렬로도 가능하다

N = int(input())
stuffs = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

arr = [0 for _ in range(1000000 + 1)]

for stuff in stuffs:
    arr[stuff] += 1

for order in orders:
    if arr[order] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# set 으로도 간단히 가능

N = int(input())
stuffs_set = set(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if order not in stuffs_set:
        print('no', end=' ')
    else:
        print('yes', end=' ')


