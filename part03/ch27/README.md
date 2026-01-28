# Chapter 27: Testing Patterns

> "Mock Object와 Self Shunt는 테스트의 강력한 도구이며, 의존성을 대체할 수 있게 되면 설계가 영원히 바뀐다." - Kent Beck

## 개요

더 상세한 테스트 작성 기법들을 다룬다. 이 패턴들은 느슨하게 결합된, 테스트하기 쉽고 재사용하기 쉬운 객체를 만들도록 유도한다.

## 패턴 목록

### 1. Child Test (자식 테스트)

**문제**: 테스트가 너무 커서 실패할 때 어떻게 하는가?

**해결**: 원래 테스트의 일부분만 테스트하는 더 작은 테스트를 작성한다.

```python
# 원래 테스트 (너무 큼)
def test_complete_order(self):
    order = Order()
    order.add_item(Item("A", 100))
    order.add_item(Item("B", 200))
    order.apply_discount(10)
    order.calculate_shipping()
    order.process_payment()
    assert order.total == 270
    assert order.status == "completed"

# Child Test로 분리
def test_add_item(self):
    order = Order()
    order.add_item(Item("A", 100))
    assert order.subtotal == 100

def test_apply_discount(self):
    order = Order()
    order.add_item(Item("A", 100))
    order.apply_discount(10)
    assert order.subtotal == 90
```

- 작은 테스트가 통과하면 큰 테스트 다시 시도
- 문제를 격리하여 디버깅 용이

### 2. Mock Object (모의 객체)

**문제**: 비용이 많이 들거나 복잡한 리소스에 의존하는 객체를 어떻게 테스트하는가?

**해결**: 해당 리소스를 시뮬레이션하는 가짜 객체를 사용한다.

```python
# 실제 DB 대신 Mock 사용
class MockDatabase:
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

def test_user_repository():
    db = MockDatabase()  # 실제 DB 대신
    repo = UserRepository(db)

    repo.save(User("alice"))

    assert db.data["alice"] is not None
```

**Mock의 가치**:

- **성능**: 실제 DB 연결 불필요
- **신뢰성**: 외부 시스템 장애에 영향받지 않음
- **가독성**: 테스트 의도가 명확

**설계에 미치는 영향**:

- 의존성 주입 촉진
- 결합도 감소
- 인터페이스 추출 유도

### 3. Self Shunt (자기 분로)

**문제**: 한 객체가 다른 객체와 올바르게 통신하는지 어떻게 테스트하는가?

**해결**: 테스트 케이스 자체를 mock으로 사용한다.

```python
class ResultListener:
    """인터페이스"""
    def on_result(self, result):
        pass

class Calculator:
    def __init__(self, listener: ResultListener):
        self.listener = listener

    def calculate(self, a, b):
        result = a + b
        self.listener.on_result(result)

# Self Shunt: 테스트 자체가 리스너 역할
class TestCalculator(TestCase, ResultListener):
    def __init__(self, name):
        super().__init__(name)
        self.result = None

    def on_result(self, result):
        self.result = result  # 테스트가 직접 수신

    def test_calculate(self):
        calc = Calculator(self)  # self를 전달
        calc.calculate(2, 3)
        assert self.result == 5
```

- 테스트 케이스가 Mock Object 역할
- 별도의 Mock 클래스 불필요
- 인터페이스 추출을 자연스럽게 유도

### 4. Log String (로그 문자열)

**문제**: 메시지 호출 순서를 어떻게 테스트하는가?

**해결**: 문자열에 로그를 기록하고 메시지가 호출될 때마다 추가한다.

```python
class TestObserver(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def on_start(self):
        self.log += "start "

    def on_process(self):
        self.log += "process "

    def on_end(self):
        self.log += "end "

    def test_workflow_order(self):
        workflow = Workflow(self)
        workflow.execute()
        assert self.log == "start process end "
```

**Part 2에서의 사용 예**:

```python
# xUnit에서 Log String 사용
class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "

def test_template_method():
    test = WasRun("testMethod")
    test.run()
    assert test.log == "setUp testMethod tearDown "
```

- Self Shunt와 함께 사용하면 효과적
- Observer 패턴 테스트에 특히 유용
- 순서가 중요하지 않으면 집합 비교 사용

### 5. Crash Test Dummy (충돌 테스트 더미)

**문제**: 발생하기 어려운 에러 상황을 어떻게 테스트하는가?

**해결**: 예외만 던지는 특수 객체를 사용한다.

```python
class CrashTestFile:
    """항상 예외를 던지는 파일 객체"""
    def write(self, data):
        raise IOError("Disk full")

def test_handles_write_error():
    crash_file = CrashTestFile()
    logger = FileLogger(crash_file)

    # 에러가 적절히 처리되는지 확인
    result = logger.log("message")
    assert result == False
    assert logger.error_count == 1
```

- 디스크 풀, 네트워크 오류 등 시뮬레이션
- 에러 처리 로직 테스트
- Mock Object의 특수한 형태

### 6. Broken Test (깨진 테스트)

**문제**: 혼자 프로그래밍할 때 세션을 어떻게 끝내는가?

**해결**: 마지막에 의도적으로 실패하는 테스트를 남겨둔다.

```python
def test_next_feature(self):
    # TODO: 내일 이어서 구현
    assert False, "Implement currency conversion"
```

- 다음 날 시작점이 명확
- 어디서 멈췄는지 즉시 알 수 있음
- "빨간 막대"로 시작

### 7. Clean Check-in (깨끗한 체크인)

**문제**: 팀으로 프로그래밍할 때 세션을 어떻게 끝내는가?

**해결**: 모든 테스트가 통과하는 상태로 체크인한다.

- Broken Test와 반대
- 팀원이 깨진 테스트를 받으면 혼란
- CI/CD 파이프라인 유지

## 패턴 조합 예시

Self Shunt + Log String:

```python
class TestSubject(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def notify(self, event):
        self.log += f"{event} "

    def test_observer_pattern(self):
        subject = Subject()
        subject.add_observer(self)  # Self Shunt

        subject.do_something()
        subject.do_another()

        assert self.log == "something another "  # Log String
```

## 핵심 원칙

1. **격리**: 외부 의존성을 제거하여 테스트 독립성 확보
2. **제어**: 테스트가 모든 상황을 제어할 수 있어야 함
3. **단순화**: 복잡한 테스트는 작은 테스트로 분리

## 다음 챕터 예고

- Chapter 28: Green Bar Patterns
- Fake It, Triangulate, Obvious Implementation
