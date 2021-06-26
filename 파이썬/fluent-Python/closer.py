def number_coroutine():
    total = 0
    while True:
        x = (yield total)
        if x:
            total += x

co = number_coroutine()
print(co.send(None))

print(co.send(1))
print(co.send(2))
print(co.send(3))
print(next(co))