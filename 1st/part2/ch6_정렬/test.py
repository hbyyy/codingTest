## 선택 정렬
import random
import sys
import time


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    example = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    example2 = [random.randint(1, 150) for _ in range(1000)]

    insert_example = example2.copy()
    quick_example = example2.copy()

    print('insert_example : ', insert_sort(example.copy()))
    print('--------------insert sort ----------------')
    time1 = time.time()
    insert_sort(insert_example)
    time2 = time.time()
    print(f'1 ----- {time2 - time1}')

    time1 = time.time()
    insert_sort(insert_example)
    time2 = time.time()
    print(f'2 ----- {time2 - time1}')

    quick_ex = example.copy()
    quick_ex2 = quick_example.copy()
    quick_sort(quick_ex, 0, len(quick_ex) - 1)
    print('quick_example : ', quick_ex)
    quick_sort([5, 1, 2, 3, 5, 6, 7, 8], 0, 7)
    print('--------------quick sort ----------------')
    time1 = time.time()
    quick_sort(quick_ex2, 0, len(quick_ex2) - 1)
    time2 = time.time()
    print(f'1 ----- {time2 - time1}')

    time1 = time.time()
    quick_sort(quick_ex2, 0, len(quick_ex2) - 1)
    time2 = time.time()
    print(f'2 ----- {time2 - time1}')

    quick_ex = example.copy()
    quick_ex2 = [random.randint(1, 150) for _ in range(1000)]
    print('quick_example 2 : ', quick_sort2(quick_ex))
    print('quick_example 2 : ', quick_sort2([5, 1, 2, 3, 5, 6, 7, 8]))
    print('--------------quick sort ----------------')
    time1 = time.time()
    quick_ex3 = quick_sort2(quick_ex2)
    time2 = time.time()
    print(f'1 ----- {time2 - time1}')
    time1 = time.time()
    quick_sort2(quick_ex3)
    time2 = time.time()
    print(f'2 ----- {time2 - time1}')

    sort_ex = example.copy()
    sort_ex2 = [random.randint(1, 150) for _ in range(1000)]
    sort_ex.sort()
    print('sort_example 2 : ', sort_ex)
    print('--------------sort ----------------')
    time1 = time.time()
    sort_ex2.sort()
    time2 = time.time()
    print(f'1 ----- {time2 - time1}')
    time1 = time.time()
    sort_ex2.sort()
    time2 = time.time()
    print(f'2 ----- {time2 - time1}')
