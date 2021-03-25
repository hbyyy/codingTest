# 럭키 스트레이트

score = input()

max_len = len(score)

left = 0
right = 0

for i in range(max_len // 2):
    left += int(score[i])

for i in range(max_len // 2, max_len):
    right += int(score[i])

if left == right:
    print('LUCKY')
else:
    print('READY')
