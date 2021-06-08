"""
783. Minimum Distance Between BST Nodes
0 <= Node.val <= 105
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 10 ** 6
    prev = -(10 ** 6)

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):

            if node.left:
                dfs(node.left)
            self.result = min(self.result, abs(node.val - self.prev))
            self.prev = node.val
            if node.right:
                dfs(node.right)

        dfs(root)
        return self.result


class Solution2:

    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -(10 ** 6)
        result = 10 ** 6
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
