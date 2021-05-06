n = int(input())

coins = list(map(int, input().split()))

target = 1

coins.sort()

for i in coins:
    if target < i:
        break
    target += i

print(target)