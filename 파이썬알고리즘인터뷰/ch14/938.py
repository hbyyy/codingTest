"""
938. Range Sum of BST
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            self.rangeSumBST(root.left, low, high)
            if low <= root.val <= high:
                self.result += root.val
            self.rangeSumBST(root.right, low, high)

        return self.result


class Solution2:
    result = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return
        if root.val >= low:
            self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            self.result += root.val
        if root.val <= high:
            self.rangeSumBST(root.right, low, high)
        return self.result
