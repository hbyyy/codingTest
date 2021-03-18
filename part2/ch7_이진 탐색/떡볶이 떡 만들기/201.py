N, M = map(int, input().split())
tteoks = list(map(int, input().split()))

s = 1
e = max(tteoks)


def binary_search(arr, start, end, m):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cuts = sum([i - mid for i in arr if i - mid > 0])
        if cuts == m:
            result = mid
            break
        elif cuts < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


print(binary_search(tteoks, s, e, M))

# start = 0
# end = max(tteoks)
# result = 0
# while start <= end:
#     mid = (start + end) // 2
#     cuts = sum([i - mid for i in tteoks if i - mid > 0])
#
#     if cuts < M:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
#
# print(result)
