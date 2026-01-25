# Chapter 8: Makin' Objects

## 목표

- Money를 추상 클래스로 변환
- 팩토리 메서드로 객체 생성 추상화
- 하위 클래스(Dollar, Franc)를 숨기고 Money 인터페이스로 통일

## 이전 챕터와의 차이

| 항목           | Chapter 7       | Chapter 8               |
| -------------- | --------------- | ----------------------- |
| Money 클래스   | 일반 클래스     | 추상 클래스 (ABC)       |
| times() 메서드 | 하위 클래스에만 | 추상 메서드 + 하위 구현 |
| 객체 생성      | `Dollar(5)`     | `Money.dollar(5)`       |
| 테스트 의존성  | Dollar, Franc   | Money만                 |

## Red-Green-Refactor 사이클

### 1. Red: 팩토리 메서드 테스트

```python
def test_multiplication(self):
    five = Money.dollar(5)  # 팩토리 메서드 사용
    assert Money.dollar(10) == five.times(2)
```

### 2. Green: 추상 클래스 + 팩토리 메서드

```python
from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def times(self, multiplier):
        pass

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)
```

Java 원본:

```java
abstract class Money {
    protected int amount;

    abstract Money times(int multiplier);

    static Money dollar(int amount) {
        return new Dollar(amount);
    }

    static Money franc(int amount) {
        return new Franc(amount);
    }
}
```

### 3. Refactor

- 테스트에서 Dollar, Franc 직접 참조 제거
- Money 팩토리 메서드만 사용
- 하위 클래스 구현 세부사항 숨김

## 전체 코드

```python
from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount):
        self._amount = amount

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
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
```

## 구현된 기능

- ✅ Money 추상 클래스 (ABC)
- ✅ `@abstractmethod times()` 추상 메서드
- ✅ `Money.dollar()`, `Money.franc()` 팩토리 메서드
- ✅ 테스트에서 하위 클래스 직접 참조 제거

## 학습 포인트

1. **추상 클래스**: 인스턴스화 불가, 서브클래스 강제
2. **팩토리 메서드 패턴**: 객체 생성 로직 캡슐화
3. **정보 은닉**: 클라이언트 코드가 구체 클래스를 몰라도 됨
4. **테스트 독립성**: Money 인터페이스에만 의존

## Kent Beck 인용

> "The two subclasses are subclasses of `Money`. If we can make `Dollar` and `Franc` disappear by providing the common functionality in `Money`, no one will have to know."

하위 클래스를 숨기면 클라이언트 코드가 구체적인 구현에 의존하지 않게 됩니다.

## 문제점 (다음 챕터에서 해결)

- ⚠️ times() 메서드가 여전히 중복
- ⚠️ 통화(currency) 개념 부재
- ⚠️ Dollar와 Franc 클래스 제거 가능?
