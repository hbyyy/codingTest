# 2.1 시퀀스

## 1. 내장 시퀀스

- 파이썬은 C로 구현된 다음과 같은 시퀀스형을 제공한다

1. 컨데이너 시퀀스
   - 서로 다른 자료형의 항목들을 담을 수 있다
   - list, tuple, collections.deque 등등
   - **객체에 대한 참조**를 담고 있다
2. 균일 시퀀스
   - 단 하나의 자료형만 담을 수 있다
   - str, bytes, bytearray, memoryview, array.array
   - 자신의 메모리 공간에 각 항목의 값을 직접 담는다.



## 2. 지능형 리스트와 제너레이터 표현식 (list comprehension)

- List comprehension
  - 오로지 리스트를 만들 뿐이다
  - 다른 종류의 시퀀스를 채우려면 **제너레이터 표현식** 을 사용해야 한다

### 주의점

- List comprehension 은 남용 시에는 정말 이해하기 어려운 코드가 나올 수 있다
- 일반적으로 두 줄 이상 넘어간다면, for 문을 이용하는게 가독성에서 좋다



### 제너레이터 표현식

- 대괄호 대신 **소괄호**를 사용한다 

```python
color = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in color for s in sizes):
    print(tshirt)
    
black S
black M
black L
white S
white M
white L
```

- 위 예제처럼 제너레이터 표현식을 사용한다면, 각각 티셔츠 리스트 목록을 메모리에 모두 저장하지 않는다.
- 제너레이터는 한번에 한 항목씩 생성할 수 있도록 for 루프에 데이터를 전달하기 때문



## 3. 튜플은 단순한 불변 리스트가 아니다

- 튜플은 불변 리스트로 사용할 수도 있찌만, 필드명이 없는 레코드? 로 사용할 수도 있다

- **언패킹** 매커니즘 덕분에

```python
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in traveler_ids:
    print('%s/%s' % passport)
    
USA/31195855
BRA/CE342567
ESP/XDA205856
```

### 튜플 언패킹

#### 내포된 튜플 언패킹 하기

```python
tmp_tuple = [
    (1, 2, 3, ('A', 'B')),
    (4, 5, 6, ('C', 'D')),
    (7, 8, 9, ('E', 'F'))]
for n1, n2, n3, (c1, c2) in tmp_tuple:
    print(n1, n2, n3, c1, c2)
    
1 2 3 A B
4 5 6 C D
7 8 9 E F
```

### NamedTuple

- 메서드 없는 클래스라고 생각할 수 있다
- 튜플의 레코드로써의 기능을 확장해 사용할 수 있다 (필드명 지정 가능)
- pydantic package
    - 파이썬 데이터 타입 설정, validation 을 위한 패키지
    - 좀 더 강력한 타입지정이 필요하다면, 이 패키지를 이용하면 좋다
    - [pydantic](https://pydantic-docs.helpmanual.io/)

```python
# 2번째 인자는 필드값인데, 반복형 값이나 공백으로 구분된 하나의 문자열을 사용한다
City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.993, (35.689722, 139.691667))
tokyo
Out[20]: City(name='Tokyo', country='JP', population=36.993, coordinates=(35.689722, 139.691667))

```





## 4. 슬라이싱

### 슬라이스에 할당하기

- 할당문의 **왼쪽**에 슬라이스 표기법을 사용하거나 del 문의 대상으로 지정하면 가변 시퀀스를 연결하거나, 잘라내거나, 값을 변경할 수 있다.

```python
l = list(range(10))
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20, 30]
l
[0, 1, 20, 30, 5, 6, 7, 8, 9]

del l[5:7]
l
[0, 1, 20, 30, 5, 8, 9]

l2 = list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

l2[3::2] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
l2
[0, 1, 2, 11, 4, 22, 6, 33, 8, 44, 10, 55, 12, 66, 14, 77, 16, 88, 18, 99]
```



## 5. 시퀀스의 복합 할당

### a += b  와 a = a + b

- `a = a + b` 표현식은 오른쪽의 `a + b` 가 먼저 평가되어 객체를 **새로** 할당한 후 a 에 할당된다

### `__iadd__()`

- `__iadd__()` 특별 메서드가 += 복합 할당 연산자가 작동하도록 만든다. 만약 `_iadd__()` 메서드가 구현되어 있지 않다면, 대신 `__add__()` 메서드를 호출하여 위와 같이 `a = a + b` 처럼 수행이 될 것이다. 즉, `__iadd__()` 메서드 구현 여부에 따라 a 변수가 가리키는 객체의 **정체성** 이 바뀔 수도 있고 아닐 수도 있다

**불변 시퀀스** 에 반복적인 연결 연산을 수행하는 것은 비효율적이다
- 불변 시퀀스에는 `__iadd__()` method 가 구현되어 있지 않으므로, 항목이 추가된 시퀀스를 새로 만들어 저장하는 식으로 수행된다
- 계속 새로운 것을 만들고, gc 를 수행하게 되므로 효율적이지 않다.
### 퀴즈

```python
t = (1, 2, [30, 40])
t[2] += [10, 20]
```

- 위 코드를 실행하면, t[2] 에 [10, 20] 이 추가된 후에 튜플의 TypeError 가 발생한다(튜플은 불변 객체이므로)



## 6. 정렬된 시퀀스를 bisect 로 관리하기

### bisect 모듈?

- 이진 검색 알고리즘을 제공한다
- 정렬된 시퀀스와 사용하면 아주 효율적으로 검색할 수 있다.

## deque 
- deque 클래스는 큐의 양쪽에서 O(1) 의 시간에 원소를 삽입, 삭제할 수 있도록 설계된 양방향 큐이다
- deque 는 thread-safe 하므로 lock 을 사용하지 않고 사용이 가능하다
    - append, popleft 등의 추가, 삭제 메서드는 원자성을 가짐
    
```python
from collections import deque
# maxlen 을 이용하면, 최대 길이를 지정할 수 있다. 만약 maxlen을 넘는 원소가 추가되면, 추가되는 쪽의 반대쪽 원소가 삭제된다
dq = deque(range(10), maxlen=10)

# rotate 를 이용해 원소를 이동시킬 수 있다 (+ -> 오른쪽 - -> 왼쪽)
dq.rotate(3)

# 왼쪽에 원소를 추가하거나, 삭제할 수 있다.
# 오른쪽에 추가하는 법은 기존 list 의 방식과 동일
dq.extendleft([10, 20, 30])
dq.appendleft((3))
dq.popleft(1)

```