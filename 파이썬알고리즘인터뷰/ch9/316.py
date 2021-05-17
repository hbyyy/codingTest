"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once.
 You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


ex )
    Input: s = "bcabc"
    Output: "abc"

    Input: s = "cbacdcbc"
    Output: "acdb"
    
    
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = list(s)
        letters.sort(reverse=True)

        answer = []
        while letters:
            c = letters.pop()
            if not answer:
                answer.append(c)
            else:
                if answer[-1] != c:
                    answer.append(c)

        return ''.join(answer)


s = Solution()

print(s.removeDuplicateLetters("bcabc"), "abc")
print(s.removeDuplicateLetters("cbacdcbc"), "acdb")
