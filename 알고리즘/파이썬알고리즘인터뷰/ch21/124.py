from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check_travel(start_idx):
            tank = 0
            for i in range(len(gas)):
                idx = (start_idx + i) % len(gas)
                tank += gas[idx]
                tank -= cost[idx]
                if tank < 0:
                    return False
            return True

        for i, (g, c) in enumerate(zip(gas, cost)):
            if g >= c:
                if check_travel(i):
                    return i

        return -1

"""
gas의 총 합이 비용의 총 합보다 작다면 불가능하다
문제에 정답은 유일하다고 되어 있기 때문에, 밑의 풀이가 가능 (시작 지점이 안 되면 다음으로 넘어감
성립되지 않는 지점이 있다면, 그 앞은 다 출발점이 될 수 없다.
"""
class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        start, tank = 0, 0

        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]

        return start