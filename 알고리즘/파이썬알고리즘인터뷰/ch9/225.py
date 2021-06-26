"""
225. Implement Stack using Queues
Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.
"""
import collections


class MyStack:

    def __init__(self):
        self.items = collections.deque()

    # x 값을 먼저 넣고, 현재 있는 item들 중 맨 뒤 값만 빼고 deQueue 후 enQueue 해줌
    # ex : 1. [3, 2, 1] <- 5 //  2. [3, 2, 1, 5] //  3. [5, 3, 2, 1]
    def push(self, x: int) -> None:
        self.items.append(x)
        for i in range(len(self.items) - 1):
            self.items.append(self.items.popleft())

    def pop(self) -> int:
        return self.items.popleft()

    def top(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        return len(self.items) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
