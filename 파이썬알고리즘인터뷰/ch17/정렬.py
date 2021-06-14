import copy


class Sort:
    def __init__(self, origin_data):
        self.origin_data = origin_data

    def bubble_sort(self):
        data = copy.deepcopy(self.origin_data)
        for i in range(1, len(data)):
            for j in range(len(data) - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


data = [70, 8, 4, 6, 2, 3, 1]
s = Sort(data)
print(s.bubble_sort())

data = [70, 8, 4, 6, 2, 3, 1]

def quick_sort(items, lo, hi):
    def partition(lo, hi):
        pivot = items[hi]
        left = lo
        for right in range(lo, hi):
            if items[right] < pivot:
                items[left], items[right] = items[right], items[left]
                left += 1
        items[left], items[hi] = items[hi], items[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(items, lo, pivot - 1)
        quick_sort(items, pivot + 1, hi)

quick_sort(data, 0, len(data) - 1)
print(data)