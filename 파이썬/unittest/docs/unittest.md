# unittest

>  JUnit (자바 테스트 프레임워크) 에서 영감을 받아 만들어진 단위 테스트 프레임워크다.
>
> 테스트 자동화, 테스트를 위한 사전 설정(setup)과 종료(shutdown) 코드 공유, 테스트를 컬렉션에 종합하기, 테스트와 리포트 프레임워크의 분리를 지원한다.
>
> 더 보면 좋은 모듈, 프레임워크
>
> - [pytest](https://docs.pytest.org/en/6.2.x/)
>   - [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/)

## 중요 개념

### Test Fixture

- 테스트를 수행할 때 필요한 준비와 그와 관련된 정리 동작
  - 임시, 프록시 데이터베이스 생성다
  - 서버 프로세스를 시작

### Test Case

- 테스트의 개별 단위이다

### Test Suite

- 여러 테스트 케이스의 묶음이다. 서로 관계가 있는 테스트들을 같이 실행할 때 사용한다

### Test runner

- 테스트 실행을 조율하고, 테스트 결과를 사용자에게 제공한다.



### 기본적인 테스트 코트 작성 방법

```python
import unittest


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

# 테스트를 실행
if __name__ == '__main__':
    unittest.main()
```

- 기본적으로, unittest.TestCase 를 상속받아 테스트 케이스를 만들 수 있다. TestCase 에는 테스트를 위한 여러 도구들이 구현되어 있다.
  - assertFalse, assertTrue, assertEqual 등 많은 케이스가 있다
  - assert 문을 대신해서 사용하면, 테스트 러너가 모든 테스트 결과를 취합해 리포트를 생성할 수 있다.
- unittest.main()으로 코드 안에서 실행시키지 않고, 명령행 인터페이스를 사용할 수도 있다



### 명령행 인터페이스

- 명령행을 사용해 모듈, 클래스, 각 테스트 메서드의 테스트들을 실행할 수 있다

```
# 테스트를 실행한다. 아무 인자 없이 실행하면 테스트 탐색을 실행한다
python -m unittest

# 테스트를 모듈 별, 클래스 별, 메서드 별로 실행할 수 있다.
python -m unittest test_module1
python -m unittest test_module1.TestStringMethod
python -m unittest test_module1.TestStringMethod.test_isupper
```



### 테스트 코드 구조 잡기

- 기본 구성 블록은 TestCase
  - 하나의 시나리오이다



#### setUp()

- 테스트들을 위한 사전 설정을 할 수 있다
- 1개의 테스트마다 반복되어 호출된다

```python
import unittest

from widget import Widget

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("the Widget")

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), "incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')

```

> self.assertEquel() 의 인자는, **객체의 값**, **기대하는 값**, **에러 메시지** 순으로 넣는다



#### tearDown()

- 테스트 메서드 실행 후 정리를 위한 메서드
- 마찬가지로 1개의 테스트마다 반복되어 호출

```python
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("the Widget")
        
    def tearDown(self):
    	self.widget.dispose()
```

- 테스트의 성공, 실패와 관계 없이, **setUp()** 이 실행되었다면 tearDown() 도 실행된다.



#### 테스트 건너뛰기

> python 3.2 부터 추가된 기능입니다. python 2 에서 사용하기를 원한다면,
>
> [unittest2](https://pypi.org/project/unittest2/) 라이브러리를 이용하는 방법이 있다.

- 기본적으로 `unittest.skip()` decorator 를 사용합니다

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")
    # reason 을 안 넣어도 작동한다.    
    @unittest.skip
    def test_nothing2(self):
        self.fail("shouldn't happen22")

        
# Class 에도 사용이 가능합니다.
@unittest.skip("showing class skipping") 
ClassMyTestCase2(unittest.TestCase):
    ...
```

