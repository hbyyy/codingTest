# 곱하기 혹은 더하기


result, *numbers = list(map(int, input()))
for c in numbers:
    if c <= 1 or result <= 1:
        result += c
    else:
        result *= c

print(result)

"""
    처음엔 숫자나 결과값이 0일 때만 + 해주도록 함
    - > 1일 경우도 더해야 한다!
"""