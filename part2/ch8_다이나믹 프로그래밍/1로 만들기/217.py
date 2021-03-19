# 책 풀이

N = int(input())

DP = [0] * (N + 1)
for i in range(2, N + 1):
    DP[i] = DP[i - 1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    if i % 5 == 0:
        DP[i] = min(DP[i], DP[i // 5] + 1)

print(DP[N])
