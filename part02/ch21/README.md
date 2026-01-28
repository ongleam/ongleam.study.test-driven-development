# Chapter 21: Counting

> "테스트 결과를 수집하여 몇 개의 테스트가 실행되었는지 알아야 한다." - Kent Beck

📌 **패턴**: Collecting Parameter

## 목표

- `TestResult` 클래스 도입
- 실행된 테스트 수 추적
- 실패한 테스트 수 추적
- 테스트 결과 요약 출력

## 이전 챕터와의 차이

| 항목      | Chapter 20    | Chapter 21                  |
| --------- | ------------- | --------------------------- |
| 결과 반환 | 없음          | TestResult 반환             |
| 결과 추적 | 개별 플래그만 | runCount, failureCount 추적 |
| 요약 출력 | 없음          | summary() 메서드            |
| 예외 처리 | 없음          | try/except로 실패 캐치      |

## 핵심 학습 포인트

1. **Collecting Parameter**: 결과를 수집하는 객체를 전달
2. **TestResult**: 테스트 실행 결과를 캡슐화
3. **runCount/failureCount**: 실행/실패 테스트 수 추적

## TDD 사이클

### Red: 실패하는 테스트

```python
def testResult(self) -> None:
    result = self.test.run()
    assert result.summary() == "1 run, 0 failed"

def testFailedResult(self) -> None:
    test = WasRun("testBrokenMethod")
    result = test.run()
    assert result.summary() == "1 run, 1 failed"
```

### Green: 최소 구현

```python
class TestResult:
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
    def run(self) -> TestResult:
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
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

    def run(self) -> TestResult:
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result


class WasRun(TestCase):
    # ... (기존 메서드들)

    def testBrokenMethod(self) -> None:
        """실패하는 테스트 메서드"""
        raise Exception
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

    def testTearDown(self) -> None:
        self.test.run()
        assert self.test.wasTornDown

    def testTemplateMethod(self) -> None:
        self.test.run()
        assert self.test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        result = self.test.run()
        assert result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"
```

## 구현된 기능

- ✅ `TestResult` 클래스 추가
- ✅ `runCount`로 실행 횟수 추적
- ✅ `failureCount`로 실패 횟수 추적
- ✅ `testStarted()` 메서드
- ✅ `testFailed()` 메서드
- ✅ `summary()` 메서드로 결과 출력
- ✅ `run()`이 `TestResult` 반환
- ✅ 예외 발생 시 `testFailed()` 호출

## TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [x] 테스트 메서드가 실패해도 tearDown 호출하기
- [ ] 여러 테스트 실행하기
- [x] 수집된 결과를 출력하기
- [x] 실패한 테스트 수 추적하기

## 다음 챕터 예고

- ⚠️ `TestSuite` 클래스로 여러 테스트 실행
- ⚠️ setUp 실패 시 처리

## 테스트 실행

```bash
python -m pytest part02/ch21/ -v
```
