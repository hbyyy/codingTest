n = int(input())
coins = list(map(int, input().split()))
coins.sort()
target = 1

for i in coins:
    if target < i:
        break
    target += i

print(target)

"""
참고 https://plplim.tistory.com/59
이해가 쉽지 않다
"""

