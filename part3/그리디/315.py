# n, m = map(int, input().split())
#
# balls = list(map(int, input().split()))
# result = 0
#
# for i in range(len(balls)):
#     for j in range(i + 1, len(balls)):
#         if balls[i] != balls[j]:
#             result += 1
#
# print(result)


n, m = map(int, input().split())

balls = list(map(int, input().split()))
weight = [0] * (m + 1)
result = 0

for x in balls:
    weight[x] += 1

for i in range(1, m + 1):
    n -= weight[i]
    result += weight[i] * n

print(result)
