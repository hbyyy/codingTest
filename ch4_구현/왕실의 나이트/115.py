"""
왕실의 나이트
    풀이 시간 20분
    예시
    input: a1   output: 2
"""

x, y = list(input())
x = ord(x) - ord('a') + 1
y = int(y)

dxdy_types = [[-2, -1], [-2, 1], [2, -1], [2, 1], [1, -2], [-1, -2], [1, 2], [-1, 2]]
result = 0

for dx, dy in dxdy_types:
    nx, ny = x + dx, x + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        result += 1

print(result)
