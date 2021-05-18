"""
641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not.
isFull(): Checks whether Deque is full or not.
"""


class ListNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k
        self.len = 0
        self.head.right = self.tail
        self.tail.left = self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.head, ListNode(value))
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.tail.left, ListNode(value))
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        n = self.head.right.right
        self.head.right, n.left = n, self.head
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        n = self.tail.left.left
        self.tail.left, n.right = n, self.tail
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.len == 0:
            return -1

        return self.head.right.item

    def getRear(self) -> int:
        if self.len == 0:
            return -1

        return self.tail.left.item

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
