def is_correct(s):
    check = 0
    if s[0] == ")":
        return False

    for c in s:
        if c == '(':
            check += 1
        else:
            if check == 0:
                return False
    return True


def separate(s):
    check = 0
    for i in range(len(s)):
        if s[i] == '(':
            check += 1
        else:
            check -= 1
        if check == 0:
            return (s[:i + 1], s[i + 1:])


def f(s):
    if not s:
        return ''
    u, v = separate(s)

    if is_correct(u):
        result = u + f(v)
    else:
        result = '('
        result += f(v)
        result += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        result += ''.join(u)
    return result


def solution(p):
    answer = f(p)
    return answer