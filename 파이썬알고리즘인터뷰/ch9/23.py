"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# heap을 이용하지 않은 풀이
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        answer = ListNode()
        tail = answer
        lists = [n for n in lists if n is not None]
        while lists:
            min_node = min(lists, key=lambda x: x.val)
            min_node_idx = lists.index(min_node)

            tail.next = min_node
            tail = tail.next
            if lists[min_node_idx].next is None:
                lists.pop(min_node_idx)
            else:
                lists[min_node_idx] = lists[min_node_idx].next

        return answer.next


# heap을 이용

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        answer = ListNode()
        tail = answer
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            val, idx, node = heapq.heappop(heap)
            tail.next = ListNode(val)
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return answer.next
