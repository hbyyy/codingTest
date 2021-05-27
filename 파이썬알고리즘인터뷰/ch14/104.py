"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def bfs(root_node):
            depth = 0
            queue = deque()

            if root_node:
                queue.append((root_node, 0))

            while queue:
                now, depth = queue.popleft()

                if now.left:
                    queue.append((now.left, depth + 1))
                if now.right:
                    queue.append((now.right, depth + 1))

            return depth

        return bfs(root)


# 이런 식으로도 가능
# 트리의 한 레벨씩 체크
class Solution2:
    def maxDepth2(self, root: TreeNode) -> int:

        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth
