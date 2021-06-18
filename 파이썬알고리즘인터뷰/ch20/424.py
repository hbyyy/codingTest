"""
424. Longest Repeating Character Replacement
"""

from collections import Counter


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = Counter()
        answer = 0
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
            answer = max(answer, right - left)
        return answer
