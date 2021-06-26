# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build_tree(data):
            if not data:
                return
            mid = len(data) // 2
            node = TreeNode(data[mid])
            node.left = build_tree(data[:mid])
            node.right = build_tree(data[mid + 1:])
            return node

        tree = build_tree(nums)
        return tree
