from typing import List


class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        to_dict = defaultdict(list)
        for ticket in sorted(tickets):
            to_dict[ticket[0]].append(ticket[1])
        answer = []

        def dfs(a):
            while to_dict[a]:
                dfs(to_dict[a].pop(0))
            answer.append(a)

        dfs('JFK')

        return answer[::-1]


from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        to_dict = defaultdict(list)
        for ticket in sorted(tickets):
            to_dict[ticket[0]].append(ticket[1])

        route, stack = [], ['JFK']

        while stack:
            while to_dict[stack[-1]]:
                stack.append(to_dict[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


s = Solution()
s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
