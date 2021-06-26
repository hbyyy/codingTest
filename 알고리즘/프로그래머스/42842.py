def solution(brown, yellow):
    m, n = 3, 3
    while True:
        b = (m * 2 + (n - 2) * 2)
        y = m * n - b

        if b == brown and y == yellow:
            answer = [m, n]
            break
        else:
            if 4*y <= yellow:
                n += 1
                m = 1
            elif y + 2*(n-2) <= yellow:
                m += 1
            elif b <= brown and y <= yellow:
                m += 1
            elif b >= brown and y <= yellow:
                n += 1
                m = n

    return answer


print(solution(24, 24))