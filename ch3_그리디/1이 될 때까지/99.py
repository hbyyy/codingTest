n, k = map(int, input().split())
result = 0

while n >= k:
    t = (n // k) * k
    result += n - t
    n = t

    n //= k
    result += 1

print(result + (n - 1))
