### 위에서 아래로 (계수정렬로 해보자)

arr = [0 for _ in range(100000 + 1)]

N = int(input())
for i in range(N):
    arr[int(input())] += 1

for i in range(len(arr) - 1, 0, -1):
    if arr[i]:
        print(f'{i} ' * arr[i])
print()

# 성적이 낮은 순서로 학생 출력하기

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(input().split()))

arr.sort(key=lambda data: int(data[1]))
for name, grade in arr:
    print(name, end=' ')

# 두 배열의 원소 교체

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))



A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))
