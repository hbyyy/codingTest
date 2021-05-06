n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
for row in arr:
    min_value = min(row)
    result = max(result, min_value)

print(result)