# 다이나믹 프로그래밍 이용 피보나치 수열


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(10))

d = [0] * (100 + 1)


# 탑다운 (재귀를 사용)
# 재귀함수와 구현 비슷, 계산한 결과를 저장해 놓고 나중에 다시 사용해야 할 때 다시 사
def fibo2(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo2(x - 1) + fibo2(x - 2)
    return d[x]


d2 = [0] * (100 + 1)


# 바텀업
# 반복문 사용, 작은 계산부터 이뤄나감용
# 주로 많이 사용한다.
def fibo3(x):
    d2[1], d2[2] = 1, 1
    n = 3
    while n <= x:
        d2[n] = d2[n - 1] + d2[n - 2]
        n += 1


fibo2(100)
print(d)
fibo3(100)
print(d2)
