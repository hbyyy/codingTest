def rotate(arr):
    tmp = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            tmp[j][m - 1 - i] = arr[i][j]

    return tmp


m = 3
arr = [[0, 0, 0],
       [1, 1, 1],
       [2, 2, 2]]

tmp = rotate(arr)
print(rotate(tmp))

