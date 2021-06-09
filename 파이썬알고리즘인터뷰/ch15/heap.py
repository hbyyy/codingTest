class BinaryHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2

        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i // 2

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[smallest], self.items[idx] = self.items[idx], self.items[smallest]
            self._percolate_down(smallest)

    def _percolate_down2(self):
        idx = 1
        left, right = 2, 3

        while left <= len(self):
            if right <= len(self):
                smallest = left if self.items[left] < self.items[right] else right
            else:
                smallest = left

            if self.items[smallest] > self.items[idx]:
                break
            self.items[smallest], self.items[idx] = self.items[idx], self.items[smallest]
            idx = smallest
            left, right = idx * 2, idx * 2 + 1



    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        item = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down2()
        return item

    def print_heap(self):
        print(*self.items[1:])


h = BinaryHeap()
h.insert(5)
h.insert(7)
h.insert(10)
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(102)
h.insert(424)
h.insert(8)
h.insert(9)
h.insert(15)

h.print_heap()

print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
print(h.extract())
