# Chapter 19: Set the Table

> "테스트를 작성할 때 공통 패턴: 준비(Arrange), 행동(Act), 확인(Assert)" - Kent Beck

📌 **패턴**: Template Method

## 목표

- `setUp()` 메서드 도입
- 테스트 픽스처(fixture) 설정 자동화
- 테스트 메서드 실행 전 공통 준비 작업 처리

## 이전 챕터와의 차이

| 항목      | Chapter 18         | Chapter 19        |
| --------- | ------------------ | ----------------- |
| 초기화    | 각 테스트에서 직접 | setUp()에서 자동  |
| 추적 방식 | wasRun 플래그      | wasRun + wasSetUp |
| 패턴      | Bootstrap          | Template Method   |

## 핵심 학습 포인트

1. **Template Method 패턴**: run()이 고정된 순서로 메서드 호출
2. **테스트 픽스처**: 테스트에 필요한 객체들의 초기 상태
3. **플래그 추적**: wasSetUp으로 setUp 호출 여부 확인

## TDD 사이클

### Red: 실패하는 테스트

```python
def testSetUp(self) -> None:
    self.test.run()
    assert self.test.wasSetUp  # wasSetUp 속성이 없음 - 실패!
```

### Green: 최소 구현

```python
class TestCase:
    def setUp(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def setUp(self) -> None:
        self.wasRun = None
        self.wasSetUp = 1
```

## 전체 코드

```python
class TestCase:
    """xUnit 테스트 케이스 기본 클래스"""

    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        """테스트 픽스처 설정 (서브클래스에서 오버라이드)"""
        pass

    def run(self) -> None:
        """setUp을 먼저 호출한 후 테스트 메서드 실행"""
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    """테스트 실행 여부와 setUp 호출을 확인하는 테스트용 클래스"""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: int | None = None
        self.wasSetUp: int | None = None

    def setUp(self) -> None:
        """setUp 호출 기록"""
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self) -> None:
        """테스트 메서드 호출 기록"""
        self.wasRun = 1
```

## 테스트 코드

```python
class TestCaseTest(TestCase):
    def setUp(self) -> None:
        self.test = WasRun("testMethod")

    def testRunning(self) -> None:
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self) -> None:
        self.test.run()
        assert self.test.wasSetUp
```

## 구현된 기능

- ✅ `setUp()` 메서드 추가
- ✅ `run()`에서 setUp() 먼저 호출
- ✅ `wasSetUp` 플래그로 호출 여부 추적

## TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [ ] 나중에 tearDown 호출하기
- [ ] 테스트 메서드가 실패해도 tearDown 호출하기
- [ ] 여러 테스트 실행하기
- [ ] 수집된 결과를 출력하기

## Template Method 패턴

`run()` 메서드가 알고리즘의 골격을 정의하고, 일부 단계를 서브클래스에 위임:

```python
def run(self) -> None:
    self.setUp()      # 1. 준비 (서브클래스에서 오버라이드)
    method()          # 2. 테스트 실행
    # self.tearDown() # 3. 정리 (다음 챕터에서 추가)
```

## 다음 챕터 예고

- ⚠️ `tearDown()` 메서드 추가
- ⚠️ 테스트 후 정리 작업 자동화
- ⚠️ 예외가 발생해도 tearDown 호출 보장

## 테스트 실행

```bash
python -m pytest part02/ch19/ -v
```
