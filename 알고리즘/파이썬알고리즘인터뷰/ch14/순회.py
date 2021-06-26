class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node('F',
            Node('B',
                 Node('A'),
                 Node('D',
                      Node('C'), Node('E'))
                 ),
            Node('G',
                 None,
                 Node('I', Node('H'))
                 )
            )


def pre_order(node):
    if not node:
        return
    print(node.val, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.val, end=' ')
    in_order(node.right)


def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val, end=' ')


def pre_order_without_recursion(node):
    stack = [node]

    while stack:
        now = stack.pop()
        if now:
            print(now.val, end=' ')
            stack.append(now.right)
            stack.append(now.left)


def in_order_without_recursion(node):
    stack = []
    now = node
    while stack or now:
        while now:
            stack.append(now)
            now = now.left
        now = stack.pop()
        print(now.val, end=' ')
        now = now.right


# def post_order_wde]
#
# while stack:
#     now = stack.pop()
# ithout_recursion(node):
#     stack = [no


print('\npre-------------')
pre_order(root)
print('\nin--------------')
in_order(root)
print('\npost-------------')
post_order(root)
print()

print('\npre2-------------')
pre_order_without_recursion(root)
print('\nin2--------------')
in_order_without_recursion(root)
print('\npost2-------------')
# post_order_without_recursion(root)
print()
