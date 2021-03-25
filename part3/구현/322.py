# 문자열 재정렬

S = list(input())

c_list = []
numbers = 0

for c in S:
    if ord(c) < ord('A'):
        numbers += int(c)
    else:
        c_list.append(c)

c_list.sort()
print(f'{"".join(c_list)}{numbers}')
