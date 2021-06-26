"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)

        result = 0
        for jewel in jewels:
            if s.get(jewel):
                result += s.get(jewel)

        return result

    ## 한줄풀이!
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)
