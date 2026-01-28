# Chapter 23: How Suite It Is

> "테스트와 테스트 모음을 동일하게 다룰 수 있어야 한다." - Kent Beck

📌 **패턴**: Composite

## 목표

- `TestSuite` 클래스 도입
- 여러 테스트를 함께 실행
- `TestCase`와 `TestSuite`를 동일하게 다루기 (Composite 패턴)

## 이전 챕터와의 차이

| 항목           | Chapter 22           | Chapter 23                       |
| -------------- | -------------------- | -------------------------------- |
| 테스트 실행    | 개별 테스트만        | TestSuite로 여러 테스트 실행     |
| run() 시그니처 | run() -> TestResult  | run(result=None) -> TestResult   |
| 결과 공유      | 테스트마다 새 result | 여러 테스트가 하나의 result 공유 |

## 핵심 학습 포인트

1. **Composite 패턴**: TestCase와 TestSuite를 동일하게 다룸
2. **Collecting Parameter**: TestResult를 파라미터로 전달
3. **run() 시그니처 변경**: 외부에서 TestResult를 주입 가능

## TDD 사이클

### Red: 실패하는 테스트

```python
def testSuite(self) -> None:
    suite = TestSuite()
    suite.add(WasRun("testMethod"))
    suite.add(WasRun("testBrokenMethod"))
    result = suite.run()
    assert result.summary() == "2 run, 1 failed"
```

### Green: 최소 구현

```python
class TestSuite:
    def __init__(self) -> None:
        self.tests: list[TestCase] = []

    def add(self, test: TestCase) -> None:
        self.tests.append(test)

    def run(self, result: TestResult | None = None) -> TestResult:
        if result is None:
            result = TestResult()
        for test in self.tests:
            test.run(result)
        return result
```

## 전체 코드

```python
class TestResult:
    """테스트 결과를 수집하는 클래스"""

    def __init__(self) -> None:
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self) -> None:
        self.runCount = self.runCount + 1

    def testFailed(self) -> None:
        self.failureCount = self.failureCount + 1

    def summary(self) -> str:
        return f"{self.runCount} run, {self.failureCount} failed"


class TestCase:
    """xUnit 테스트 케이스 기본 클래스"""

    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self, result: TestResult | None = None) -> TestResult:
        """setUp -> 테스트 메서드 -> tearDown 순서로 실행"""
        if result is None:
            result = TestResult()
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result


class TestSuite:
    """여러 테스트를 함께 실행하는 테스트 스위트"""

    def __init__(self) -> None:
        self.tests: list[TestCase] = []

    def add(self, test: TestCase) -> None:
        self.tests.append(test)

    def run(self, result: TestResult | None = None) -> TestResult:
        if result is None:
            result = TestResult()
        for test in self.tests:
            test.run(result)
        return result
```

## 테스트 코드

```python
class TestCaseTest(TestCase):
    def setUp(self) -> None:
        self.result = TestResult()

    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        test = WasRun("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self) -> None:
        self.result.testStarted()
        self.result.testFailed()
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedSetUpResult(self) -> None:
        test = WasRunWithBrokenSetUp("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testSuite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed"
```

## 구현된 기능

- ✅ `TestSuite` 클래스 추가
- ✅ `add()` 메서드로 테스트 추가
- ✅ `run()` 메서드로 모든 테스트 실행
- ✅ `TestCase.run()`이 `TestResult`를 파라미터로 받음
- ✅ `testSuite` 테스트

## TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [x] 테스트 메서드가 실패해도 tearDown 호출하기
- [x] 여러 테스트 실행하기
- [x] 수집된 결과를 출력하기
- [x] 실패한 테스트 수 추적하기

## 다음 챕터 예고

- ⚠️ xUnit Retrospective (회고)
- ⚠️ Part 2 완료

## 테스트 실행

```bash
python -m pytest part02/ch23/ -v
```
