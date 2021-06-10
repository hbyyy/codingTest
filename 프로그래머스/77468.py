"""
다단계 칫솔 판매
https://programmers.co.kr/learn/courses/30/lessons/77486
"""


def solution(enroll, referral, seller, amount):
    result = {'center': 0}
    parents = {}

    for i in range(len(enroll)):
        result[enroll[i]] = 0
        if referral[i] == '-':
            parents[enroll[i]] = 'center'
        else:
            parents[enroll[i]] = referral[i]

    for i in range(len(seller)):
        money = amount[i] * 100
        now = seller[i]
        while True:
            fees = int(money * 0.1)
            money -= fees
            if now == 'center' or fees < 1:
                result[now] += money + fees
                break
            else:
                result[now] += money
                now = parents[now]
                money = fees

    answer = [result[e] for e in enroll]
    return answer


# 재귀 이용 풀이


def solution2(enroll, referral, seller, amount):
    def pyramid(money, name):
        fees = int(money * 0.1)
        money -= fees
        if fees < 1 or name == 'center':
            result[name] += money + fees
            return
        result[name] += money
        pyramid(fees, parents[name])

    result = {'center': 0}
    parents = {}

    for e, r in zip(enroll, referral):
        result[e] = 0
        parents[e] = 'center' if r == '-' else r

    for s, a in zip(seller, amount):
        pyramid(a * 100, s)

    return [result[e] for e in enroll]
