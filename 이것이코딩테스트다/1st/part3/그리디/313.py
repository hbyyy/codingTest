# 문자열 뒤집기
# 내 풀이

S = input()


def f(s, target):
    i = 0
    j = i
    result = 0

    while j < len(s):
        if s[i] == target:
            while True:
                j += 1
                if j < len(s) and s[j] == s[i]:
                    continue
                else:
                    result += 1
                    i = j
                    break
            j = i
        else:
            i += 1
            j = i

    return result


result1 = f(S, '0')
result2 = f(S, '1')

print(result1 if result1 < result2 else result2)

# 모범 답안

S = input()

zero = 0
one = 0
if S[0] == '0':
    zero += 1
else:
    one += 1

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '0':
            zero += 1
        else:
            one += 1

print(min(zero, one))
