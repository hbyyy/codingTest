def trace(func):
    # print(locals())

    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 완료')

    return wrapper


@trace
def hello():
    print('hello')


@trace
def world():
    print('world')


def decorator1(func):
    print(locals())

    def wrapper():
        print('decorator1')
        func()

    return wrapper


def decorator2(func):
    print(locals())

    def wrapper():
        print('decorator2')
        func()

    return wrapper


# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')


hello()
