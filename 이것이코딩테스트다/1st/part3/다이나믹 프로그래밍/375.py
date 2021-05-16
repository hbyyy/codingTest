t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    DP = [[0] * m for _ in range(n)]
    arr = [[0] * m for _ in range(n)]
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        arr[i // m][i % m] = tmp[i]

    for i in range(n):
        DP[i][0] = arr[i][0]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                DP[j][i] = max(DP[j][i - 1], DP[j + 1][i - 1]) + arr[j][i]
            elif j == (n - 1):
                DP[j][i] = max(DP[j - 1][i - 1], DP[j][i - 1]) + arr[j][i]
            else:
                DP[j][i] = max(DP[j][i - 1], DP[j + 1][i - 1], DP[j - 1][i - 1]) + arr[j][i]

    result = 0
    for i in range(n):
        for j in range(m):
            result = max(result, DP[i][j])
    print(result)
