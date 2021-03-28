# 안테나
# 중간값이 답이다. 써보면 항상 성립한다는 걸 알수 있음

n = int(input())
towns = list(map(int, input().split()))

towns.sort()
print(towns[(n - 1) // 2])



#출력해보자
n = int(input())
towns = list(map(int, input().split()))
towns.sort()

for i in range(n):
    sum_num = 0
    for j in range(n):
        sum_num += abs(towns[i] - towns[j])
    print(sum_num, end=' ')