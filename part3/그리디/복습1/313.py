s = input()

turn_one = 0
turn_zero = 0

if s[0] == '0':
    turn_one = 1
else:
    turn_zero = 1

for i in range(0, len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            turn_one += 1
        else:
            turn_zero += 1

print(min(turn_zero, turn_one))