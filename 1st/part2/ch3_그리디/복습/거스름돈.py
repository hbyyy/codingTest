n = 1260
count = 0

for coin in [500, 100, 50, 10]:
    count += n // coin
    n %= coin

print(count)