n = int(input())

numbers = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9


def dfs(i, now):
    global plus, minus, mul, div, min_value, max_value
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, now + numbers[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - numbers[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, (abs(now) // numbers[i]) if now >= 0 else -(abs(now) // numbers[i]))
            div += 1


dfs(1, numbers[0])
print(max_value)
print(min_value)

#조합 써서 해보자 1

from itertools import permutations

n = int(input())

numbers = list(map(int, input().split()))

operator_numbers = list(map(int, input().split()))
operators = []

operators.extend(operator_numbers[0] * ['+'])
operators.extend(operator_numbers[1] * ['-'])
operators.extend(operator_numbers[2] * ['*'])
operators.extend(operator_numbers[3] * ['//'])


op_list = list(permutations(operators, n - 1))

min_value = 1e9
max_value = -1e9

for op in op_list:
    result = 0
    for i in range(n - 1):
        if i == 0:
            result = eval(f'{numbers[i]}{op[i]}{numbers[i+1]}') if op[i] != '//' else eval(f'int({numbers[i]}/{numbers[i+1]})')
        else:
            result = eval(f'{result}{op[i]}{numbers[i + 1]}') if op[i] != '//' else eval(f'int({result}/{numbers[i + 1]})')

    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)

#조합 써서 해보자 2
from itertools import permutations

n = int(input())

numbers = list(map(int, input().split()))

operator_numbers = list(map(int, input().split()))
operators = []

operators.extend(operator_numbers[0] * [0])
operators.extend(operator_numbers[1] * [1])
operators.extend(operator_numbers[2] * [2])
operators.extend(operator_numbers[3] * [3])


op_list = list(permutations(operators, n - 1))

min_value = 1e9
max_value = -1e9

for op in op_list:
    result = numbers[0]
    for i in range(n - 1):
        if op[i] == 0:
            result += numbers[i+1]
        if op[i] == 1:
            result -= numbers[i+1]
        if op[i] == 2:
            result *= numbers[i+1]
        if op[i] == 3:
            result = int(result / numbers[i+1])
    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)