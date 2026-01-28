# Chapter 22: Dealing with Failure

> "실패를 다루는 것은 성공만큼 중요하다." - Kent Beck

📌 **패턴**: Fake It ('Til You Make It)

## 목표

- 실패한 테스트 결과 포맷팅
- `failureCount`와 `testFailed` 메서드 추가
- `testFailedResultFormatting` 테스트로 포맷 검증
- setUp 실패 시에도 실패로 카운트

## 이전 챕터와의 차이

| 항목      | Chapter 21       | Chapter 22                      |
| --------- | ---------------- | ------------------------------- |
| 실패 추적 | testFailedResult | testFailedResultFormatting 추가 |
| 포맷 검증 | 통합 테스트만    | 단위 테스트 추가                |

## 핵심 학습 포인트

1. **testFailedResultFormatting**: TestResult 자체의 포맷팅 테스트
2. **Fake It**: 먼저 하드코딩 후 점진적 일반화
3. **작은 단계**: 실패 메커니즘을 별도로 테스트

## TDD 사이클

### Red: 실패하는 테스트

```python
def testFailedResultFormatting(self) -> None:
    result = TestResult()
    result.testStarted()
    result.testFailed()
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
    def run(self) -> TestResult:
        result = TestResult()
        result.testStarted()
        try:
            self.setUp()  # setUp도 try 블록 안에서 실행
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result


class WasRunWithBrokenSetUp(TestCase):
    """setUp에서 실패하는 테스트용 클래스"""

    def setUp(self) -> None:
        raise Exception

    def testMethod(self) -> None:
        pass
```

## 테스트 코드

```python
class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        test = WasRun("testMethod")
        result = test.run()
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

    def testFailedSetUpResult(self) -> None:
        test = WasRunWithBrokenSetUp("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"
```

## 구현된 기능

- ✅ `failureCount`로 실패 횟수 추적
- ✅ `testFailed()` 메서드
- ✅ `summary()`에서 실패 수 포함
- ✅ `testFailedResultFormatting` 테스트
- ✅ setUp 실패 시에도 실패로 카운트
- ✅ `WasRunWithBrokenSetUp` 클래스
- ✅ `testFailedSetUpResult` 테스트

## TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [ ] 테스트 메서드가 실패해도 tearDown 호출하기
- [ ] 여러 테스트 실행하기
- [x] 수집된 결과를 출력하기
- [x] 실패한 테스트 수 추적하기

## 다음 챕터 예고

- ⚠️ `TestSuite` 클래스로 여러 테스트 실행
- ⚠️ Composite 패턴 적용

## 테스트 실행

```bash
python -m pytest part02/ch22/ -v
```
