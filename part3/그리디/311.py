# 모험가 길드

# 내 풀이
n = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

i = 0
j = 0

result = 0
while j < len(adventurers):
    if adventurers[j] == j - i + 1:
        result += 1
        i = j + 1
        j = i
    else:
        j += 1

print(result)

# 모범 답안
n = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

count = 0
result = 0

for i in adventurers:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
