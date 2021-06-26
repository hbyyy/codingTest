from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        result = 0
        task_counter = Counter(tasks)

        while task_counter:
            sub_count = 0
            for k, c in task_counter.most_common(n + 1):
                sub_count += 1
                result += 1
                task_counter[k] -= 1
                task_counter += Counter()

            if not task_counter:
                break
            result += n - sub_count + 1

        return result


# 내가 의도한 풀이
from collections import Counter


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        result = []
        task_counter = Counter(tasks)

        while task_counter:
            out = []
            for k, c in task_counter.most_common(n + 1):
                out.append(k)
                task_counter[k] -= 1
                task_counter += Counter()

            result += out
            if not task_counter:
                break
            else:
                # 리스트 * 음수는 빈 리스트를 반환한다!
                # if len(out) < (n + 1):
                result += [''] * (n - len(out) + 1)

        return len(result)
