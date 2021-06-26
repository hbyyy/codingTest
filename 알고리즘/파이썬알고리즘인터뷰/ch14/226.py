"""
226. Invert Binary Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()


from collections import deque


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def bfs(start_node):
            if not start_node:
                return

            queue = deque([start_node])

            while queue:
                node = queue.popleft()

                node.left, node.right = node.right, node.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        bfs(root)
        return root


# 재귀로 구현하면 코드가 간단
# 이해, 설명이 어려움
class Solution2:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
            return root
        return None


tree_val = [4, 2, 7, 1, 3, 6, 9]
tree_root = TreeNode(tree_val.pop(0))
queue = [tree_root]
while tree_val:
    node = queue.pop(0)
    a, b = TreeNode(tree_val.pop(0)), TreeNode(tree_val.pop(0))
    queue.append(a)
    queue.append(b)
    node.left = a
    node.right = b

s = Solution2()
s.invert_tree(root=tree_root)
tree_root.print_tree()
