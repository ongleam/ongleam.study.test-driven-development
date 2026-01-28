# Chapter 20: Cleaning Up After

> "테스트가 서로 영향을 미치지 않도록 각 테스트 후에 정리 작업이 필요하다." - Kent Beck

📌 **패턴**: Template Method (확장)

## 목표

- `tearDown()` 메서드 도입
- 테스트 후 정리 작업 자동화
- 테스트 메서드 실행 후 tearDown() 호출

## 이전 챕터와의 차이

| 항목      | Chapter 19       | Chapter 20                          |
| --------- | ---------------- | ----------------------------------- |
| 정리 작업 | 없음             | tearDown() 자동 호출                |
| 추적 방식 | wasRun, wasSetUp | wasRun, wasSetUp, wasTornDown + log |

## 핵심 학습 포인트

1. **tearDown**: 테스트 후 리소스 정리 (파일 닫기, DB 연결 해제 등)
2. **Template Method 확장**: setUp -> testMethod -> tearDown 순서
3. **wasTornDown 플래그**: tearDown 호출 여부 확인
4. **log 문자열**: 호출 순서를 문자열로 추적 (리팩토링)

## TDD 사이클

### Red: 실패하는 테스트

```python
def testTearDown(self) -> None:
    self.test.run()
    assert self.test.wasTornDown  # wasTornDown 속성이 없음 - 실패!
```

### Green: 최소 구현

```python
class TestCase:
    def tearDown(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: int | None = None
        self.wasSetUp: int | None = None
        self.wasTornDown: int | None = None

    def tearDown(self) -> None:
        self.wasTornDown = 1
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

    def tearDown(self) -> None:
        """테스트 후 정리 작업 (서브클래스에서 오버라이드)"""
        pass

    def run(self) -> None:
        """setUp -> 테스트 메서드 -> tearDown 순서로 실행"""
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    """테스트 실행 여부와 setUp/tearDown 호출을 확인하는 테스트용 클래스"""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: int | None = None
        self.wasSetUp: int | None = None
        self.wasTornDown: int | None = None
        self.log = ""

    def setUp(self) -> None:
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "

    def testMethod(self) -> None:
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def tearDown(self) -> None:
        self.wasTornDown = 1
        self.log = self.log + "tearDown "
```

## 테스트 코드

```python
class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "
```

## 구현된 기능

- ✅ `tearDown()` 메서드 추가
- ✅ `run()`에서 tearDown() 마지막에 호출
- ✅ `wasTornDown` 플래그로 호출 여부 추적
- ✅ `log` 문자열로 호출 순서 추적

## TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [ ] 테스트 메서드가 실패해도 tearDown 호출하기
- [ ] 여러 테스트 실행하기
- [ ] 수집된 결과를 출력하기

## 다음 챕터 예고

- ⚠️ 테스트 결과 수집 (`TestResult`)
- ⚠️ 실행된 테스트 수, 실패한 테스트 수 추적

## 테스트 실행

```bash
python -m pytest part02/ch20/ -v
```
