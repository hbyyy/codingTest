"""
147. Insertion Sort List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        answer = ListNode(next=ListNode(head.val))
        node = head.next
        root = answer
        while node:
            prev, now = root, root.next
            while now and node.val > now.val:
                prev = now
                now = now.next
            if not now:
                prev.next = ListNode(node.val)
            else:
                prev.next = ListNode(node.val, now)
            node = node.next
        return answer.next


# 최적화 풀이

class Solution2:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = ListNode(0)
        root = cur
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = root
        return root.next
