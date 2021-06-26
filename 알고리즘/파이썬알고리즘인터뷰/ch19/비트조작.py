nums = [2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7]
MASK = 0xFFFF
result = 0
for n in nums:
    print(n)
    result ^= n
    print(bin(result))

