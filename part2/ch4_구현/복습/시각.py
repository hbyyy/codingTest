n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count += 1

print(count)
