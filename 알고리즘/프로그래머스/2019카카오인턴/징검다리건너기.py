def find_zeroblock(tmp, k):
    zero_count = 0
    for i in tmp:
        if i == 0:
            zero_count += 1

            if zero_count == k:
                return True
        else:
            zero_count = 0
    return False


def solution(stones, k):
    answer = 0
    start, end = 1, 200000000

    while start <= end:
        mid = (start + end) // 2

        tmp = [0 if i - mid < 0 else i - mid for i in stones]
        check = find_zeroblock(tmp, k)
        if check:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
