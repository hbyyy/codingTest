import sys
input = sys.stdin.readline

n = int(input())
scores = []
for _ in range(n):
    scores.append(input().split())

scores.sort(key=lambda data: (-int(data[1]), int(data[2]), -int(data[3]), data[0]))

for score in scores:
    print(score[0])
