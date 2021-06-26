"""
3. Longest Substring Without Repeating Characters


Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        start, end = 0, 1
        if len(s) == 1 or len(set(s)) == 1:
            return 1

        while end < len(s):
            sub_s = s[start: end]
            if s[end] in sub_s:
                start += 1
                if start == end:
                    end += 1
            else:
                answer = max(answer, len(sub_s) + 1)
                end += 1

        return answer


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
