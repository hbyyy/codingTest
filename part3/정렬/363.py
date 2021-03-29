import heapq

n = int(input())
decks = []
result = 0

for _ in range(n):
    decks.append(int(input()))

heapq.heapify(decks)

while len(decks) != 1:
    l = heapq.heappop(decks)
    r = heapq.heappop(decks)
    result += l + r
    heapq.heappush(decks, l + r)
print(result)
