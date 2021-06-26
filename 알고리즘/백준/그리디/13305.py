n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
result = 0

# 1
for i in range(1, len(prices)):
    if prices[i] <= min_price:
        result += roads[i - 1] * min_price
        min_price = prices[i]
    else:
        result += roads[i - 1] * min_price
print(result)

# 2
all_min_price = min(prices)
for i in range(1, n):
    result += roads[i - 1] * min_price
    if prices[i] == all_min_price:
        result += sum(roads[i:]) * all_min_price
        break
    if prices[i] < min_price:
        min_price = prices[i]
print(result)
