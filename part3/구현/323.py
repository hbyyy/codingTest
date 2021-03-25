def solution(s):
    i = 1
    result = []

    while i <= len(s) // 2:
        j = 0
        comp_s_len = 0
        count = 1
        while j <= len(s):
            if s[j:j + i] == s[j + i:j + i + i]:
                count += 1
            else:
                comp_s_len += len(s[j:j + i])
                if count > 1:
                    comp_s_len += len(str(count))
                    count = 1
            j += i
        result.append(comp_s_len)
        i += 1

    return min(result, default=1)


# 문자열 확인 가능

def solution2(s):
    i = 1
    result = []

    while i <= len(s) // 2:
        j = 0
        tmp = []
        count = 1
        while j <= len(s):
            if s[j:j + i] == s[j + i:j + i + i]:
                count += 1
            else:
                tmp.append(s[j:j + i])
                if count > 1:
                    tmp.append(str(count))
                    count = 1
            j += i
        result.append(len(''.join(tmp)))
        i += 1

    return min(result, default=1)


# 모범 답