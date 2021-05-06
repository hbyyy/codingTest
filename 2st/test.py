answer = 0

def calculate(count, total, n, target):
    global answer

    if count == n:
        print(output)
        if eval(output) == target:
            print('------correct!------')
            answer += 1
    else:
        output = output + '+1'
        calculate(count + 1, output, n, target)
        output = output[:-2]
        output = output + '-1'
        calculate(count + 1, output, n, target)
        output = output[:-2]


def solution(numbers, target):
    global answer
    calculate(1, f'+1', len(numbers), target)
    calculate(1, f'-1', len(numbers), target)
    return answer


if __name__ == '__main__':
    result = solution([1, 1, 1, 1, 1], 3)
    print(result)