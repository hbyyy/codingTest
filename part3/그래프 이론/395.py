# 탑승구
# 이 코드는 O(n2) 이라 100000 * 100000 -> 해결 불가능할듯

g = [*range(int(input()) + 1)]
p = int(input())

count = 0
for i in range(p):
    gi = int(input())
    for j in range(gi, 0, -1):
        if isinstance(g[j], int):
            count += 1
            g[j] = (g[j], 1)
            break
    else:
        break
print(count)


