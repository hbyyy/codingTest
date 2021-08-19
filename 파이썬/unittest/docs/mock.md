# unittest.mock

> mock 은 테스트 대상 시스템의 일부를 mock 객체로 교체하고, 테스트 가능하게 합니다.
>
> 파이썬 3.2 부터 unittest 에 추가되었습니다. 이전 버전의 파이썬에서는 mock 패키지를 설치해야 합니다
>
> `pip install mock`



## 기본 사용법

```python
from unittest.mock import MagicMock
thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')

thing.method.assert_called_with(3, 4, 5, key='value')
```

### MasicMock vs Mock

- MasicMock 은 Mock 의 서브클래스이다
- Masic method 들이 모두 Mocking 되어 있는 편리한 클래스

### side effect

- side_effect 를 사용하면 mock 이 호출될 때 예외를 발생시키는 걸 포함해 side effect 를 미리 정해줄 수 있다.

```python
mock = Mock(side_effect=KeyError('foo'))
mock()

Traceback (most recent call last):
 ...
KeyError: 'foo'
```



### 참고

기본적으로, 존재하지 않는 모듈의 함수(또는 클래스의 메서드나 어트리뷰트)를 패치하려고 시도하면 [`AttributeError`](https://docs.python.org/ko/3/library/exceptions.html#AttributeError)로 실패합니다:

\>>>

```
>>> @patch('sys.non_existing_attribute', 42)
... def test():
...     assert sys.non_existing_attribute == 42
...
>>> test()
Traceback (most recent call last):
  ...
AttributeError: <module 'sys' (built-in)> does not have the attribute 'non_existing'
```

그러나 [`patch()`](https://docs.python.org/ko/3/library/unittest.mock.html#unittest.mock.patch) 호출에 `create=True`를 추가하면 이전 예제가 기대한 대로 작동합니다:

\>>>

```
>>> @patch('sys.non_existing_attribute', 42, create=True)
... def test(mock_stdout):
...     assert sys.non_existing_attribute == 42
...
>>> test()
```



