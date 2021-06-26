"""
297. Serialize and Deserialize Binary Tree
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                result.append('null')
            else:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        data = deque(data)
        tree = TreeNode(data.popleft())
        queue = deque([tree])
        while data:
            node = queue.popleft()
            a, b = data.popleft(), data.popleft()
            if a is not None:
                node.left = TreeNode(a)
                queue.append(node.left)
            if b is not None:
                node.right = TreeNode(b)
                queue.append(node.right)

        return tree
