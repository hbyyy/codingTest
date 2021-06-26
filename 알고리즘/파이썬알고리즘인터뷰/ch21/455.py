"""
455. Assign Cookies
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        if len(g) < len(s):
            s.sort()
            g.sort()

            while g and s:
                if g[-1] <= s[-1]:
                    s.pop()
                    result += 1
                g.pop()
        else:
            s.sort(reverse=True)
            g.sort(reverse=True)
            while g and s:
                if g[-1] <= s[-1]:
                    g.pop()
                    result += 1
                s.pop()
        return result


