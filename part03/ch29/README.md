# Chapter 29: xUnit Patterns

> "xUnit 아키텍처는 많은 프로그래머 지향 테스트 도구의 핵심이다." - Kent Beck

## 개요

xUnit 프레임워크의 사용 패턴들을 다룬다. Part 2에서 직접 구현한 xUnit의 핵심 개념들을 패턴 관점에서 정리한다.

## 패턴 목록

### 1. Assertion (단언)

**문제**: 테스트 결과가 올바른지 어떻게 확인하는가?

**해결**: Boolean 표현식을 작성하고 프로그램이 자동으로 검증하게 한다.

```python
# 기본 Assertion
assert result == expected
assert result is not None
assert len(items) > 0

# 메시지 포함
assert result == 10, f"Expected 10, got {result}"

# xUnit 스타일
self.assertEqual(result, expected)
self.assertTrue(condition)
self.assertRaises(Exception, dangerous_function)
```

**Assertion의 종류**:

- `assertEqual(a, b)`: 동등성 검사
- `assertTrue(x)`: 참인지 검사
- `assertFalse(x)`: 거짓인지 검사
- `assertRaises(E, f)`: 예외 발생 검사
- `assertIsNone(x)`: None인지 검사

**핵심 원칙**:

- 하나의 테스트에 하나의 개념
- Assertion 실패 시 명확한 메시지
- 테스트 독립성 유지

### 2. Fixture (픽스처)

**문제**: 여러 테스트가 동일한 객체 집합을 사용할 때 어떻게 하는가?

**해결**: 각 테스트의 실행 전에 생성되는 공통 객체 집합을 사용한다.

```python
class TestCalculator(TestCase):
    def setUp(self):
        # Fixture 생성
        self.calculator = Calculator()
        self.result = TestResult()

    def test_add(self):
        assert self.calculator.add(2, 3) == 5

    def test_subtract(self):
        assert self.calculator.subtract(5, 3) == 2
```

**Part 2에서의 사용**:

```python
class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()  # Fixture

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown "
```

**Fixture vs 로컬 변수**:

- Fixture: 여러 테스트가 공유하는 객체
- 로컬 변수: 해당 테스트에서만 사용
- 과도한 Fixture는 테스트 가독성 저하

### 3. External Fixture (외부 픽스처)

**문제**: 테스트 간에 공유되는 외부 리소스를 어떻게 해제하는가?

**해결**: `tearDown()`에서 리소스를 해제한다.

```python
class TestDatabase(TestCase):
    def setUp(self):
        # External Fixture 생성
        self.db = Database.connect("test_db")
        self.db.begin_transaction()

    def tearDown(self):
        # 반드시 해제
        self.db.rollback()
        self.db.close()

    def test_insert(self):
        self.db.insert({"name": "Alice"})
        assert self.db.count() == 1
```

**외부 리소스 예시**:

- 데이터베이스 연결
- 파일 핸들
- 네트워크 소켓
- 임시 파일/디렉토리

**Part 2에서의 구현**:

```python
class TestCase:
    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()  # 항상 호출
        return result
```

### 4. Test Method (테스트 메서드)

**문제**: 테스트를 어떻게 나타내는가?

**해결**: `test`로 시작하는 메서드로 표현한다.

```python
class TestMoney(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        assert five.times(2) == Dollar(10)

    def testEquality(self):
        assert Dollar(5) == Dollar(5)
        assert not Dollar(5) == Dollar(6)

    def testCurrency(self):
        assert Money.dollar(1).currency() == "USD"
```

**명명 규칙**:

- `test_` 또는 `test` 접두사
- 테스트 대상과 상황을 명확히
- 예: `test_multiplication_with_zero`, `test_invalid_input_raises_error`

**하나의 테스트, 하나의 개념**:

```python
# 좋은 예: 분리된 테스트
def test_equality_same_amount(self):
    assert Dollar(5) == Dollar(5)

def test_equality_different_amount(self):
    assert not Dollar(5) == Dollar(6)

# 나쁜 예: 여러 개념 혼합
def test_everything(self):
    assert Dollar(5) == Dollar(5)
    assert Dollar(5).times(2) == Dollar(10)
    assert Dollar(5).currency() == "USD"
```

### 5. Exception Test (예외 테스트)

**문제**: 예외가 올바르게 발생하는지 어떻게 테스트하는가?

**해결**: 예상되는 예외를 잡아서 검증한다.

```python
# 방법 1: try-except 직접 사용
def test_division_by_zero(self):
    try:
        calculator.divide(1, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass  # 예상대로 예외 발생

# 방법 2: assertRaises 사용 (권장)
def test_division_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        calculator.divide(1, 0)

# 방법 3: pytest 스타일
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)
```

**Part 2에서의 사용**:

```python
class WasRun(TestCase):
    def testBrokenMethod(self):
        raise Exception  # 의도적 예외

def testFailedResult(self):
    test = WasRun("testBrokenMethod")
    test.run(self.result)
    assert self.result.summary() == "1 run, 1 failed"
```

### 6. All Tests (모든 테스트)

**문제**: 모든 테스트를 한 번에 어떻게 실행하는가?

**해결**: 모든 테스트 스위트를 포함하는 스위트를 만든다.

```python
# TestSuite 사용
def all_tests():
    suite = TestSuite()
    suite.add(TestMoney("testMultiplication"))
    suite.add(TestMoney("testEquality"))
    suite.add(TestExchange("testConversion"))
    return suite

# Part 2에서의 구현
class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result
```

**현대적인 방식 (pytest)**:

```bash
# 모든 테스트 실행
pytest

# 특정 디렉토리
pytest part01/

# 특정 패턴
pytest -k "test_money"
```

## xUnit 아키텍처 요약

```
TestCase
├── setUp()      # Fixture 생성
├── testMethod() # 테스트 실행 + Assertion
└── tearDown()   # External Fixture 해제

TestSuite
├── add(test)    # 테스트 추가
└── run(result)  # 모든 테스트 실행

TestResult
├── testStarted()  # 실행 카운트
├── testFailed()   # 실패 카운트
└── summary()      # 결과 요약
```

## Part 2 구현과의 연결

| 패턴             | Part 2 챕터 | 구현                     |
| ---------------- | ----------- | ------------------------ |
| Fixture          | ch19, ch23  | setUp(), self.result     |
| External Fixture | ch20        | tearDown()               |
| Test Method      | ch18        | testMethod(), run()      |
| Exception Test   | ch21, ch22  | try-except, testFailed() |
| All Tests        | ch23        | TestSuite                |

## 핵심 원칙

1. **격리**: 각 테스트는 독립적
2. **반복 가능**: 같은 결과 보장
3. **자가 검증**: 자동으로 성공/실패 판단
4. **적시성**: 빠른 피드백

## 다음 챕터 예고

- Chapter 30: Design Patterns
- TDD와 함께 사용되는 디자인 패턴들
