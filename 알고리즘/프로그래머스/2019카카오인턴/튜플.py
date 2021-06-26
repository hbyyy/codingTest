def solution(s):
    tmp_s = s.lstrip('{').rstrip('}').split('},{')
    new_s = [list(map(int, c.split(','))) for c in tmp_s]
    new_s.sort(key=len)

    answer = [new_s[0][0]]
    for i in range(1, len(new_s)):
        for item in new_s[i]:
            if item not in new_s[i - 1]:
                answer.append(item)

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))