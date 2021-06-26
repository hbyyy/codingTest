# N과 M (2)
n, m = map(int, input().split())
numbers = [*range(1, n + 1)]
visited = [0] * (n + 1)


def f(count, idx, tmp):
    if count == m:
        for num in tmp:
            print(num, end=' ')
        print()
    else:
        for i in range(idx, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                tmp.append(i)
                f(count + 1, i, tmp)
                visited[i] = 0
                tmp.pop()


f(0, 1, [])
