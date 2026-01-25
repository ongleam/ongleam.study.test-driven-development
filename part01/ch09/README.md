# Chapter 9: Times We're Livin' In

> "We want to get to a common times() implementation, but we need to know which class to return." - Kent Beck

📌 **패턴**: -

## 목표

- 통화(currency) 개념 도입
- Dollar는 "USD", Franc은 "CHF"
- 추상 클래스 Money 유지 (ch08에서 계속)

## 이전 챕터와의 차이

| 항목          | Chapter 8          | Chapter 9                         |
| ------------- | ------------------ | --------------------------------- |
| Money 필드    | `_amount`          | `_amount`, `_currency`            |
| currency()    | 없음               | 추가                              |
| Dollar 생성자 | `__init__(amount)` | `super().__init__(amount, "USD")` |
| Franc 생성자  | `__init__(amount)` | `super().__init__(amount, "CHF")` |

## 핵심 학습 포인트

1. **도메인 개념 추가**: 통화라는 현실 세계의 개념을 코드로 표현
2. **생성자 체이닝**: `super().__init__()`로 부모 초기화
3. **점진적 진화**: 기존 구조(추상 클래스, 팩토리 메서드) 유지하면서 기능 추가

## TDD 사이클

### Red: 통화 테스트 작성

```python
def test_currency(self):
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()
```

### Green: currency 구현

```python
class Money(ABC):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")

class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount, "CHF")
```

Java 원본:

```java
abstract class Money {
    protected int amount;
    protected String currency;

    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    String currency() {
        return currency;
    }
}

class Dollar extends Money {
    Dollar(int amount) {
        super(amount, "USD");
    }
}
```

### Refactor: 개선

- 통화를 생성자에서 부모로 전달
- 하위 클래스가 자신의 통화 코드를 알고 있음

## 전체 코드

```python
from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))

    @abstractmethod
    def times(self, multiplier):
        pass

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount, "CHF")

    def times(self, multiplier):
        return Franc(self._amount * multiplier)
```

## 구현된 기능

- ✅ Money 추상 클래스 유지 (ch08 계승)
- ✅ `Money.dollar()`, `Money.franc()` 팩토리 메서드 유지
- ✅ 통화(currency) 필드 추가
- ✅ `currency()` 메서드 추가
- ✅ Dollar는 "USD", Franc은 "CHF"

## 다음 챕터 예고

- ⚠️ times() 메서드가 여전히 중복
- ⚠️ Dollar와 Franc 클래스가 거의 동일
- ⚠️ times()에서 통화를 사용하여 통합 가능?

## 테스트 실행

```bash
python -m pytest part01/ch09/ -v
```
