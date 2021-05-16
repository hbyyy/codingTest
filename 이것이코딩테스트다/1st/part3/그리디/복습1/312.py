numbers = list(map(int, input()))

result = 0

for n in numbers:
    if result <= 1 or n <= 1:
        result += n
    else:
        result *= n

print(result)
