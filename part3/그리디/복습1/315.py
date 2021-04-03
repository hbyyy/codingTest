n, m = map(int, input().split())

w = [0 for _ in range(m + 1)]

balls = list(map(int, input().split()))

for b in balls:
    w[b] += 1

result = 0
for i in range(1, m + 1):
    n -= w[i]
    result += w[i] * n

print(result)