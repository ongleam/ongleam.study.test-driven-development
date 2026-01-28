# Chapter 30: Design Patterns

> "TDD에서 자주 등장하는 디자인 패턴들의 베스트 셀렉션" - Kent Beck

## 개요

TDD와 함께 사용되는 디자인 패턴들을 다룬다. Part 1, 2에서 사용한 패턴들을 정리하고 새로운 패턴들도 소개한다.

## 패턴 목록

### 1. Command (명령)

**문제**: 계산 작업의 호출을 어떻게 표현하는가?

**해결**: 계산 작업을 객체로 만들어 메시지로 전달한다.

```python
# command.py
from abc import ABC, abstractmethod


class Command(ABC):
    """명령 인터페이스"""

    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    """전등 켜기 명령"""

    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class LightOffCommand(Command):
    """전등 끄기 명령"""

    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        self.light.off()


class Light:
    """전등"""

    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False


class RemoteControl:
    """리모컨 - 명령 실행기"""

    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
```

**테스트**:

```python
def test_command():
    light = Light()
    remote = RemoteControl()

    # 전등 켜기
    remote.set_command(LightOnCommand(light))
    remote.press_button()
    assert light.is_on == True

    # 전등 끄기
    remote.set_command(LightOffCommand(light))
    remote.press_button()
    assert light.is_on == False
```

**TDD에서의 활용**: 테스트 실행 자체가 Command 패턴 (TestCase.run())

---

### 2. Value Object (값 객체)

**문제**: 객체를 값처럼 사용하려면 어떻게 하는가?

**해결**: 불변 객체로 만들고 동등성 비교를 구현한다.

```python
# value_object.py
class Money:
    """불변 값 객체"""

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self) -> int:
        return hash((self._amount, self._currency))

    def __repr__(self) -> str:
        return f"Money({self._amount}, '{self._currency}')"

    def times(self, multiplier: int) -> "Money":
        """새로운 Money 객체 반환 (불변성 유지)"""
        return Money(self._amount * multiplier, self._currency)

    def plus(self, other: "Money") -> "Money":
        """같은 통화끼리 덧셈"""
        if self._currency != other._currency:
            raise ValueError("Currency mismatch")
        return Money(self._amount + other._amount, self._currency)
```

**테스트**:

```python
def test_value_object():
    # 동등성
    five_a = Money(5, "USD")
    five_b = Money(5, "USD")
    assert five_a == five_b
    assert five_a is not five_b  # 다른 객체

    # 불변성 - times는 새 객체 반환
    ten = five_a.times(2)
    assert ten == Money(10, "USD")
    assert five_a == Money(5, "USD")  # 원본 불변

    # 해시 가능 (딕셔너리 키로 사용 가능)
    prices = {Money(5, "USD"): "five dollars"}
    assert prices[Money(5, "USD")] == "five dollars"
```

**Part 1에서의 사용**: Dollar, Franc, Money 클래스

---

### 3. Null Object (널 객체)

**문제**: 객체의 부재를 어떻게 표현하는가?

**해결**: 아무것도 하지 않는 특수 객체를 사용한다.

```python
# null_object.py
from abc import ABC, abstractmethod


class Logger(ABC):
    """로거 인터페이스"""

    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    """콘솔 로거"""

    def __init__(self):
        self.messages = []

    def log(self, message: str) -> None:
        self.messages.append(message)
        print(message)


class NullLogger(Logger):
    """널 로거 - 아무것도 하지 않음"""

    def log(self, message: str) -> None:
        pass  # 의도적으로 아무것도 안 함


class Calculator:
    """로거를 사용하는 계산기"""

    def __init__(self, logger: Logger = None):
        self.logger = logger or NullLogger()  # None이면 NullLogger

    def add(self, a: int, b: int) -> int:
        result = a + b
        self.logger.log(f"add({a}, {b}) = {result}")
        return result
```

**테스트**:

```python
def test_null_object():
    # NullLogger 사용 - if 체크 불필요
    calc = Calculator()  # logger=None
    result = calc.add(2, 3)
    assert result == 5  # 로깅 없이 정상 동작

    # ConsoleLogger 사용
    logger = ConsoleLogger()
    calc_with_log = Calculator(logger)
    calc_with_log.add(2, 3)
    assert "add(2, 3) = 5" in logger.messages
```

**장점**: `if logger is not None` 체크 불필요

---

### 4. Template Method (템플릿 메서드)

**문제**: 작업의 순서는 같지만 세부 구현이 다를 때 어떻게 하는가?

**해결**: 상위 클래스에서 순서를 정의하고, 하위 클래스에서 세부 구현한다.

```python
# template_method.py
from abc import ABC, abstractmethod


class TestCase(ABC):
    """템플릿 메서드 패턴 - xUnit"""

    def __init__(self, name: str):
        self.name = name

    def setUp(self) -> None:
        """하위 클래스에서 오버라이드"""
        pass

    def tearDown(self) -> None:
        """하위 클래스에서 오버라이드"""
        pass

    def run(self) -> str:
        """템플릿 메서드 - 순서 정의"""
        log = ""
        self.setUp()
        log += "setUp "
        method = getattr(self, self.name)
        method()
        log += f"{self.name} "
        self.tearDown()
        log += "tearDown"
        return log


class DataProcessor(ABC):
    """데이터 처리 템플릿"""

    def process(self, data):
        """템플릿 메서드"""
        validated = self.validate(data)
        transformed = self.transform(validated)
        result = self.save(transformed)
        return result

    @abstractmethod
    def validate(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def save(self, data):
        pass


class JSONProcessor(DataProcessor):
    """JSON 데이터 처리"""

    def __init__(self):
        self.saved_data = None

    def validate(self, data):
        if not isinstance(data, dict):
            raise ValueError("Must be dict")
        return data

    def transform(self, data):
        return {k.upper(): v for k, v in data.items()}

    def save(self, data):
        self.saved_data = data
        return data
```

**테스트**:

```python
def test_template_method():
    processor = JSONProcessor()
    result = processor.process({"name": "alice", "age": 30})

    assert result == {"NAME": "alice", "AGE": 30}
    assert processor.saved_data == {"NAME": "alice", "AGE": 30}
```

**Part 2에서의 사용**: TestCase.run() (setUp → testMethod → tearDown)

---

### 5. Pluggable Object (플러거블 객체)

**문제**: 조건문 대신 다형성을 어떻게 사용하는가?

**해결**: 조건에 따라 다른 객체를 플러그인한다.

```python
# pluggable_object.py
from abc import ABC, abstractmethod


class SelectionMode(ABC):
    """선택 모드 인터페이스"""

    @abstractmethod
    def select(self, items: list, start: int, end: int) -> list:
        pass


class SingleSelection(SelectionMode):
    """단일 선택"""

    def select(self, items: list, start: int, end: int) -> list:
        return [items[start]] if start < len(items) else []


class RangeSelection(SelectionMode):
    """범위 선택"""

    def select(self, items: list, start: int, end: int) -> list:
        return items[start:end + 1]


class Editor:
    """에디터 - 선택 모드를 플러그인"""

    def __init__(self, mode: SelectionMode = None):
        self.mode = mode or SingleSelection()
        self.items = []

    def set_mode(self, mode: SelectionMode):
        self.mode = mode

    def select(self, start: int, end: int) -> list:
        # if-else 없이 다형성으로 처리
        return self.mode.select(self.items, start, end)
```

**테스트**:

```python
def test_pluggable_object():
    editor = Editor()
    editor.items = ["a", "b", "c", "d", "e"]

    # 단일 선택 모드
    editor.set_mode(SingleSelection())
    assert editor.select(1, 3) == ["b"]

    # 범위 선택 모드로 교체
    editor.set_mode(RangeSelection())
    assert editor.select(1, 3) == ["b", "c", "d"]
```

**장점**: 조건문 제거, 새 모드 추가 용이

---

### 6. Pluggable Selector (플러거블 셀렉터)

**문제**: 인스턴스별로 다른 메서드를 호출하려면 어떻게 하는가?

**해결**: 메서드 이름을 저장하고 동적으로 호출한다.

```python
# pluggable_selector.py
class Report:
    """리포트 - 플러거블 셀렉터"""

    def __init__(self, format_name: str = "text"):
        self.format_name = format_name
        self.data = {}

    def set_data(self, data: dict):
        self.data = data

    def output(self) -> str:
        """저장된 메서드 이름으로 동적 호출"""
        method_name = f"format_{self.format_name}"
        method = getattr(self, method_name)
        return method()

    def format_text(self) -> str:
        lines = [f"{k}: {v}" for k, v in self.data.items()]
        return "\n".join(lines)

    def format_html(self) -> str:
        lines = [f"<li>{k}: {v}</li>" for k, v in self.data.items()]
        return "<ul>" + "".join(lines) + "</ul>"

    def format_json(self) -> str:
        import json
        return json.dumps(self.data)
```

**테스트**:

```python
def test_pluggable_selector():
    data = {"name": "Alice", "age": 30}

    # 텍스트 포맷
    report = Report("text")
    report.set_data(data)
    assert "name: Alice" in report.output()

    # HTML 포맷
    report = Report("html")
    report.set_data(data)
    assert "<li>name: Alice</li>" in report.output()

    # JSON 포맷
    report = Report("json")
    report.set_data(data)
    assert '"name": "Alice"' in report.output()
```

**Part 2에서의 사용**: `getattr(self, self.name)` - 테스트 메서드 동적 호출

---

### 7. Factory Method (팩토리 메서드)

**문제**: 객체 생성을 유연하게 하려면 어떻게 하는가?

**해결**: 객체 생성을 별도 메서드로 분리한다.

```python
# factory_method.py
from abc import ABC, abstractmethod


class Money(ABC):
    """통화 추상 클래스"""

    def __init__(self, amount: int):
        self._amount = amount

    @property
    def amount(self) -> int:
        return self._amount

    @abstractmethod
    def currency(self) -> str:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> "Money":
        pass

    # 팩토리 메서드
    @staticmethod
    def dollar(amount: int) -> "Money":
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> "Money":
        return Franc(amount)


class Dollar(Money):
    def currency(self) -> str:
        return "USD"

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def currency(self) -> str:
        return "CHF"

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
```

**테스트**:

```python
def test_factory_method():
    # 팩토리 메서드로 생성 - 구체 클래스 은닉
    five_dollars = Money.dollar(5)
    ten_francs = Money.franc(10)

    assert five_dollars.currency() == "USD"
    assert ten_francs.currency() == "CHF"

    # 클라이언트는 Dollar, Franc을 직접 알 필요 없음
    assert five_dollars.times(2).amount == 10
```

**Part 1에서의 사용**: `Money.dollar()`, `Money.franc()`

---

### 8. Imposter (사칭꾼)

**문제**: 기존 코드를 변경하지 않고 새로운 변형을 도입하려면?

**해결**: 기존 객체처럼 행동하는 다른 객체를 만든다.

```python
# imposter.py
from abc import ABC, abstractmethod


class Expression(ABC):
    """표현식 인터페이스"""

    @abstractmethod
    def reduce(self, bank, to_currency: str):
        pass

    @abstractmethod
    def plus(self, addend: "Expression") -> "Expression":
        pass


class Money(Expression):
    """단일 금액 - 표현식처럼 행동"""

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    def currency(self):
        return self._currency

    def reduce(self, bank, to_currency: str):
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount // rate, to_currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)


class Sum(Expression):
    """합계 - Money처럼 행동하는 사칭꾼"""

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to_currency: str):
        amount = (
            self.augend.reduce(bank, to_currency).amount +
            self.addend.reduce(bank, to_currency).amount
        )
        return Money(amount, to_currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)


class Bank:
    """환율 관리"""

    def __init__(self):
        self.rates = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: int):
        self.rates[(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency:
            return 1
        return self.rates.get((from_currency, to_currency), 1)
```

**테스트**:

```python
def test_imposter():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    # Money와 Sum 모두 Expression처럼 행동
    five_dollars = Money(5, "USD")
    ten_francs = Money(10, "CHF")

    # Sum은 Money를 사칭
    sum_expr = five_dollars.plus(ten_francs)
    result = sum_expr.reduce(bank, "USD")

    assert result.amount == 10  # 5 + 10/2
```

**Part 1에서의 사용**: Sum 클래스 (Money처럼 Expression 구현)

---

### 9. Composite (복합체)

**문제**: 하나의 객체와 객체의 컬렉션을 동일하게 다루려면?

**해결**: 컬렉션을 개별 객체와 같은 인터페이스로 만든다.

```python
# composite.py
from abc import ABC, abstractmethod


class Component(ABC):
    """컴포넌트 인터페이스"""

    @abstractmethod
    def run(self, result: "TestResult") -> "TestResult":
        pass


class TestResult:
    """테스트 결과"""

    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, {self.failure_count} failed"


class TestCase(Component):
    """개별 테스트 케이스"""

    def __init__(self, name: str):
        self.name = name

    def run(self, result: TestResult = None) -> TestResult:
        result = result or TestResult()
        result.test_started()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        return result


class TestSuite(Component):
    """테스트 스위트 - 컴포지트"""

    def __init__(self):
        self.tests: list[Component] = []

    def add(self, test: Component):
        self.tests.append(test)

    def run(self, result: TestResult = None) -> TestResult:
        result = result or TestResult()
        for test in self.tests:
            test.run(result)  # TestCase든 TestSuite든 동일하게 호출
        return result
```

**테스트**:

```python
class SampleTest(TestCase):
    def test_pass(self):
        assert True

    def test_fail(self):
        raise Exception("fail")


def test_composite():
    # 개별 테스트
    single = SampleTest("test_pass")
    result = single.run()
    assert result.summary() == "1 run, 0 failed"

    # 스위트 (복합체)
    suite = TestSuite()
    suite.add(SampleTest("test_pass"))
    suite.add(SampleTest("test_fail"))

    result = suite.run()
    assert result.summary() == "2 run, 1 failed"

    # 스위트 안에 스위트 (재귀 구조)
    outer_suite = TestSuite()
    outer_suite.add(suite)
    outer_suite.add(SampleTest("test_pass"))

    result = outer_suite.run()
    assert result.summary() == "3 run, 1 failed"
```

**Part 2에서의 사용**: TestSuite (TestCase와 동일 인터페이스)

---

### 10. Collecting Parameter (수집 매개변수)

**문제**: 여러 객체에 걸친 결과를 어떻게 수집하는가?

**해결**: 결과를 수집할 객체를 매개변수로 전달한다.

```python
# collecting_parameter.py
class TestResult:
    """수집 매개변수"""

    def __init__(self):
        self.run_count = 0
        self.failure_count = 0
        self.errors = []

    def test_started(self):
        self.run_count += 1

    def test_failed(self, error: str = None):
        self.failure_count += 1
        if error:
            self.errors.append(error)

    def summary(self) -> str:
        return f"{self.run_count} run, {self.failure_count} failed"


class TestCase:
    def __init__(self, name: str):
        self.name = name

    def run(self, result: TestResult) -> TestResult:
        """result를 수집 매개변수로 받음"""
        result.test_started()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.test_failed(str(e))
        return result


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result: TestResult) -> TestResult:
        """동일한 result를 모든 테스트에 전달"""
        for test in self.tests:
            test.run(result)  # 결과가 누적됨
        return result
```

**테스트**:

```python
class MyTest(TestCase):
    def test_one(self):
        pass

    def test_two(self):
        raise Exception("error in two")


def test_collecting_parameter():
    result = TestResult()  # 수집 매개변수

    # 여러 테스트가 동일한 result에 결과 누적
    suite = TestSuite()
    suite.add(MyTest("test_one"))
    suite.add(MyTest("test_two"))
    suite.run(result)

    assert result.run_count == 2
    assert result.failure_count == 1
    assert "error in two" in result.errors
```

**Part 2에서의 사용**: TestResult를 run() 매개변수로 전달

---

### 11. Singleton (싱글톤)

**문제**: 전역 변수의 이점을 얻으면서 단점을 피하려면?

**해결**: 클래스의 인스턴스가 하나만 존재하도록 한다.

```python
# singleton.py
class Configuration:
    """싱글톤 설정 관리자"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.settings = {}

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str, default=None):
        return self.settings.get(key, default)


# 대안: 모듈 수준 싱글톤 (더 파이썬다운 방식)
class _ConfigModule:
    def __init__(self):
        self.settings = {}

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str, default=None):
        return self.settings.get(key, default)


config = _ConfigModule()  # 모듈 임포트 시 한 번만 생성
```

**테스트**:

```python
def test_singleton():
    # 클래스 기반 싱글톤
    config1 = Configuration()
    config2 = Configuration()

    assert config1 is config2  # 동일 인스턴스

    config1.set("debug", True)
    assert config2.get("debug") == True  # 상태 공유


def test_module_singleton():
    # 모듈 기반 싱글톤
    from singleton import config

    config.set("env", "test")
    assert config.get("env") == "test"
```

**주의**: 싱글톤은 전역 상태를 만들어 테스트를 어렵게 할 수 있음

---

## 패턴 요약

| 패턴                 | 목적                      | Part 1/2 사용            |
| -------------------- | ------------------------- | ------------------------ |
| Command              | 계산을 객체로 표현        | TestCase.run()           |
| Value Object         | 불변 값 객체              | Money, Dollar            |
| Null Object          | 객체 부재 표현            | -                        |
| Template Method      | 순서 정의, 세부 구현 위임 | setUp → test → tearDown  |
| Pluggable Object     | 조건문 대신 다형성        | -                        |
| Pluggable Selector   | 동적 메서드 호출          | getattr(self, self.name) |
| Factory Method       | 객체 생성 캡슐화          | Money.dollar()           |
| Imposter             | 기존 객체 사칭            | Sum (Money처럼 행동)     |
| Composite            | 개별/컬렉션 동일 취급     | TestSuite                |
| Collecting Parameter | 결과 수집 객체 전달       | TestResult               |
| Singleton            | 유일 인스턴스             | -                        |

## 다음 챕터 예고

- Chapter 31: Refactoring
- 리팩토링 기법들 (Extract Method, Move Method 등)
