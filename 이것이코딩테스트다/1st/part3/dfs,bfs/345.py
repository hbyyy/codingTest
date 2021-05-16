import heapq


def bfs(q):
    while q:
        v, x, y = heapq.heappop(q)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if origin_arr[nx][ny] == 0:
                    origin_arr[nx][ny] = v


n, k = map(int, input().split())
origin_arr = []
queue = []

for i in range(n):
    row = list(map(int, input().split()))
    origin_arr.append(row)

s, x, y = map(int, input().split())

for _ in range(s):
    for i in range(n):
        for j in range(n):
            if origin_arr[i][j] != 0:
                heapq.heappush(queue, (origin_arr[i][j], i, j))
    bfs(queue)

print(origin_arr[x - 1][y - 1])

# 모범 답안
# bfs 에서 시간 관련 (s 초까지 bfs 돌린 결과) 해결하는 팁
# queue 에 s 값을 같이 넣어주고, 큐에서 pop한 원소의 s 값이 target_s 라면 중지시겨면 된다.
from collections import deque

n, k = map(int, input().split())
viruses = []
origin_arr = []


def bfs(q, target_s):
    while q:
        virus, s, x, y = q.popleft()
        if s == target_s:
            # 이 시점에서 target_s 인 값을 가진 노드까지 처리가 완료된 것
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if origin_arr[nx][ny] == 0:
                    origin_arr[nx][ny] = virus
                    queue.append((virus, s + 1, nx, ny))


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            viruses.append((row[j], 0, i, j))
    origin_arr.append(row)

viruses.sort()
queue = deque(viruses)

s, x, y = map(int, input().split())

bfs(queue, s)
print(origin_arr[x - 1][y - 1])
