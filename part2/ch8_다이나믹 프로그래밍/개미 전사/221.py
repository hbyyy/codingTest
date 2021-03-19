N = int(input())
fw = list(map(int, input().split()))

DP = [0] * N
DP[0] = fw[0]
DP[1] = max(fw[0], fw[1])

for i in range(2, N):
    DP[i] = max(DP[i - 1], DP[i - 2] + fw[i])

print(DP[-1])
