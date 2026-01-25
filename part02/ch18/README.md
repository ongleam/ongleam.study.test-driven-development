# Chapter 18: First Steps to xUnit

> "How do you test a testing framework? You use the framework to test itself." - Kent Beck

📌 **패턴**: Bootstrap

## 목표

- xUnit 테스트 프레임워크의 첫 번째 단계
- 테스트 메서드를 이름으로 호출하는 기본 구조 구현
- "부트스트랩 문제" 해결: 프레임워크로 자기 자신을 테스트

## 이전 챕터와의 차이

| 항목   | Part 1 (Money) | Part 2 Ch18 (xUnit)            |
| ------ | -------------- | ------------------------------ |
| 테스트 | pytest 사용    | 직접 만든 프레임워크           |
| 대상   | 도메인 객체    | 테스트 프레임워크              |
| 특징   | 외부 도구 의존 | 자기 참조적 (self-referential) |

## 핵심 학습 포인트

1. **부트스트랩 문제**: 테스트 프레임워크를 테스트하려면 테스트 프레임워크가 필요
2. **Reflection**: 메서드 이름(문자열)으로 메서드 호출
3. **자기 참조**: 만들고 있는 프레임워크로 자기 자신을 테스트

## TDD 사이클

### Red: 실패하는 테스트

```python
# 테스트가 실행되었는지 확인하는 플래그
test = WasRun("testMethod")
print(test.wasRun)  # None (아직 실행 안 됨)
test.testMethod()
print(test.wasRun)  # True (실행됨)
```

### Green: 최소 구현

```python
class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = True
```

### Refactor: TestCase 추출

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None

    def testMethod(self):
        self.wasRun = True
```

## 전체 코드

```python
class TestCase:
    """xUnit 테스트 케이스 기본 클래스"""

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        """테스트 메서드를 이름으로 찾아서 실행"""
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    """테스트 실행 여부를 확인하는 테스트용 클래스"""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: bool | None = None

    def testMethod(self) -> None:
        """실행되면 wasRun을 True로 설정"""
        self.wasRun = True
```

## 구현된 기능

- ✅ `TestCase` 기본 클래스
- ✅ `__init__(name)` - 테스트 메서드 이름 저장
- ✅ `run()` - 이름으로 메서드 찾아서 실행 (reflection)
- ✅ `WasRun` - 프레임워크 테스트용 클래스

## TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [ ] 나중에 tearDown 호출하기
- [ ] 테스트 메서드가 실패해도 tearDown 호출하기
- [ ] 여러 테스트 실행하기
- [ ] 수집된 결과를 출력하기

## 핵심 기법: Reflection

Python의 `getattr()`을 사용하여 문자열로 메서드를 찾아 호출:

```python
method = getattr(self, self.name)  # "testMethod" → self.testMethod
method()                            # self.testMethod() 호출
```

Java에서는:

```java
Method method = getClass().getMethod(name, null);
method.invoke(this, null);
```

## 다음 챕터 예고

- ⚠️ `setUp()` 메서드 추가 (테스트 픽스처 설정)
- ⚠️ 테스트 실행 전 준비 작업 자동화

## 테스트 실행

```bash
python -m pytest part02/ch18/ -v
```
