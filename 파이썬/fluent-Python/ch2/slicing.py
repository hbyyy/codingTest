# 반복되는 슬라이스가 있다면. 슬라이스 객체를 만들어 사용할 수 있다

invoice = """
0.....6.....12
1000   one
2000   two
3000   three
"""

ID = slice(0, 6)
NAME = slice(6, 12)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[ID], item[NAME])


# 슬라이스로 할당도 가능하다
L = list(range(10))
print(L)
L[2:5] = [20, 30]
print(L)
del L[5:7]
print(L)

t = (1, 2, [10, 20])
t[2].append(3)
print(t)

t = (1, 2, 3)
t *= 2
print(t)