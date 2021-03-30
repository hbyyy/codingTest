# 정수 삼각형

DP = []
arr = []
n = int(input())
for _ in range(n):
    DP.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(DP[i])):
        if j == 0:
            v = DP[i - 1][j] + DP[i][j]
        elif j == len(DP[i]) - 1:
            v = DP[i - 1][j - 1] + DP[i][j]
        else:
            v = max(DP[i - 1][j - 1], DP[i - 1][j]) + DP[i][j]
        DP[i][j] = v
print(max(DP[n - 1]))
