N, M = map(int, input().split())
tteoks = list(map(int, input().split()))

# tteoks.sort()
# H = (1 + tteoks[-1]) // 2
# def binary_search(start, end, h):
#     cuts = 0
#     while start <= end:
#         mid = (start + end) // 2
#         cuts = sum([i - mid for i in tteoks if i - mid > 0])
#         if cuts == M:
#             h = mid
#             return h
#         elif cuts > M:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return cuts
#
#
# print(binary_search(1, 1000000000, H))


start = 0
end = max(tteoks)
result = 0
while start <= end:
    mid = (start + end) // 2
    cuts = sum([i - mid for i in tteoks if i - mid > 0])

    if cuts < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
