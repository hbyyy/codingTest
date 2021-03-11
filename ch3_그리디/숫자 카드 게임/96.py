"""
    선택한 행의 카드 중 가장 낮은 수의 카드를 뽑아야 한다
    이 값의 최댓값을 구해라!
    (처음에 문제 이해 못함)
"""

n, m = map(int, input().split())
result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
