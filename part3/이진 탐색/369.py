# 공유기 설치

def solve(arr, start, end):
    global result
    while start <= end:
        mid = (start + end) // 2
        count = 1
        value = arr[0]

        for i in range(1, n):
            if arr[i] >= value + mid:
                value = arr[i]
                count += 1

        if count < c:
            end = mid - 1
        else:
            result = mid
            start = mid + 1


n, c = map(int, input().split())
towns = []

for _ in range(n):
    towns.append(int(input()))

towns.sort()

result = 0
max_distance = towns[-1] - towns[0]
min_distance = 0

solve(towns, min_distance, max_distance)
print(result)
