"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

ex :
    Input: s = "()"
    Output: true

    Input: s = "()[]{}"
    Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c not in table:
                stack.append(c)
            else:
                if not stack or stack.pop() != table[c]:
                    return False
        return not stack


s = Solution()
assert s.isValid("()") is True
assert s.isValid("()[]{}") is True
assert s.isValid("(]") is False
assert s.isValid("([)]") is False
