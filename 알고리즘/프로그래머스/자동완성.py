def solution(words):
    dic = {words[0]: words[0]}
    for word in words[1:]:
        for i in range(1, len(word) + 1):
            possible = False
            for k in dic.keys():
                if k.startswith(word[:i]):
                    continue
                else:
                    possible = True
            if possible:
                dic[word[:i]] = word
                break
    print(dic)
    answer = 0

    for word in words:
        for i in range(1, len(word) + 1):
            answer += 1
            if word[:i] in dic:
                if dic[word[:i]] == word:
                    break

    return answer

solution(["go", "gone", "guild"])