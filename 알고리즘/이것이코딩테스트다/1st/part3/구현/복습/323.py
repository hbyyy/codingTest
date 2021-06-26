def solution2(s):
    result = []

    for i in range(1, len(s) // 2 + 1):
        count = 1
        comp_len = 0
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+i+i]:
                count += 1
            else:
                comp_len += len(s[j:j+i])
                if count > 1:
                    comp_len += len(str(count))
                count = 1
        result.append(comp_len)
    return min(result, default=1)


solution2("abcabcdede")


# 모범 답안