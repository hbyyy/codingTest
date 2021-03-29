# 정수 삼각형

DP = []
arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

DP.append(arr[0])
DP.append([arr[0][0] + arr[1][0], arr[0][0] + arr[1][1]])

for i in range(2, n):
    tmp = []
    for j in range(len(arr[i])):
        if j == 0:
            v = DP[i - 1][j] + arr[i][j]
        elif j == len(arr[i]) - 1:
            v = DP[i - 1][j - 1] + arr[i][j]
        else:
            v = max(DP[i - 1][j - 1], DP[i - 1][j]) + arr[i][j]
        tmp.append(v)
    DP.append(tmp.copy())
    tmp.clear()
print(max(DP[n - 1]))
