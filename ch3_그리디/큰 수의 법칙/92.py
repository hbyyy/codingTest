"""
배열의 크기 N, 숫자가 더해지는 횟수 M, 최대 반복 사용 수 K 가 주어질 때 주어진 수를 더하여 가장 큰 수를 구해라

2 <= N <= 1000 , 1 <= M <= 10000 , 1 <= K <= 10000
K <= M
"""

# n, m, k = map(int, input().split())
# nums = list(map(int, input().split()))
# answer = 0
# nums.sort(reverse=True)
#
# while m:
#     if m // k:
#         answer += nums[0] * k
#         m -= k
#     if m:
#         answer += nums[1]
#         m -= 1
# print(answer)

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

answer = (nums[0] * k + nums[1]) * (m // (k + 1)) + (nums[0] * (m % (k + 1)))
print(answer)
