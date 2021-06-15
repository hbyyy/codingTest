a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# left = 0
# right = len(a) - 1
# target = 11

def binary_search(items, target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            print(f'index : {mid} : {items[mid]}')
            return
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print('not fount')


binary_search(a, 11, 0, len(a) - 1)
