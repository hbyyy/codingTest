"""
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language.
"""


## 연결 리스트를 이용해 구현
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class MyCircularQueueUseLinkedList:

    def __init__(self, k: int):
        self.front = Node()

        now = self.front
        for i in range(k - 1):
            now.next = Node()
            now = now.next

        now.next = self.front

        self.rear = now

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = self.rear.next
        self.rear.item = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.item = None
        self.front = self.front.next
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.item

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.item

    def isEmpty(self) -> bool:
        return self.rear.next == self.front and not (self.rear.item and self.front.item)

    def isFull(self) -> bool:
        return self.rear.next == self.front and (self.rear.item and self.front.item)


## 배열을 이용해 구현
class MyCircularQueueUserArray:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_len = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.max_len
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue[self.front] is None:
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_len
        return True

    def Front(self) -> int:
        return -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.queue[self.rear - 1] is None else self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None
