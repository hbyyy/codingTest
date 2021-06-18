"""
406. Queue Reconstruction by Height

풀이 : 각 사람을 키카 큰 순, 앞의 사람 수가 적은 순 (-x[0], x[1]) 로 정렬한 후
      왼쪽부터 하나씩 pop 후 인덱스에 맞게 넣어 주면 된다
      - > 키가 큰 순으로 정렬한 후 큰 순으로 하나씩 뽑아 넣기 때문에
          해당 사람을 결과물에 넣을 때 그 사람보다 작은 사람은 결과물에 없다!
          그러므로 바로 인덱스로 넣어 주면 된다.
"""

from collections import deque
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        people = deque(people)
        out = []

        while people:
            p = people.popleft()
            out.insert(p[1], p)

        return out
