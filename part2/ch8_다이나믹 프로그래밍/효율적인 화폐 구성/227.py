N, M = map(int, input().split())
DP = [10001] * (M + 1)
DP[0] = 0

for _ in range(N):
    value = int(input())
    for i in range(value, M + 1):
        DP[i] = min(DP[i - value] + 1, DP[i])

result = -1 if DP[M] == 10001 else DP[M]

print(result)
