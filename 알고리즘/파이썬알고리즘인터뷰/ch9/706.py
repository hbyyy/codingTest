"""
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    # self.data 를 defaultdict(ListNode) 로 바꿔도 똑같이 동작한다
    # size = 1000 일 때 동작 시간은 data 가 list, dict 일 경우 비슷하게 나온다
    def __init__(self):
        self.size = 1000
        self.data = [ListNode() for _ in range(self.size)]

    def _get_index(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)
        if self.data[index].key is None:
            self.data[index] = ListNode(key, value)
        else:
            now = self.data[index]
            while now:
                if now.key == key:
                    now.value = value
                    break
                if now.next is None:
                    now.next = ListNode(key, value)
                    break
                now = now.next

    def get(self, key: int) -> int:
        index = self._get_index(key)
        now = self.data[index]

        while now:
            if now.key == key:
                return now.value
            now = now.next

        return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key)

        if self.data[index].value is None:
            return

        now = self.data[index]
        if now.key == key:
            self.data[index] = now.next if self.data[index].next is not None else ListNode()
        else:
            prev = now
            while now:
                if now.key == key:
                    prev.next = now.next
                    break
                prev, now = now, now.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
