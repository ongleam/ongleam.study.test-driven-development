# Chapter 15: Mixed Currencies

> "$5 + 10 CHF = $10 if rate is 2:1" - Kent Beck

📌 **패턴**: Composite

## 목표

- 서로 다른 통화의 덧셈 + Expression 일반화
- Part 1의 최종 목표 달성!

## 이전 챕터와의 차이

| 항목                | Chapter 14 | Chapter 15 |
| ------------------- | ---------- | ---------- |
| Sum.plus()          | 없음       | 구현       |
| Expression.times()  | 없음       | 구현       |
| Sum의 augend/addend | Money      | Expression |
| 다중 통화 덧셈      | 지원 안함  | 완전 지원  |

## 핵심 학습 포인트

1. **Expression 일반화**: Money와 Sum 모두 동일한 인터페이스
2. **Composite 패턴**: Sum이 Expression을 포함, 재귀적 구조
3. **다형성의 힘**: reduce(), plus(), times() 모두 다형적 호출

## TDD 사이클

### Red: 다중 통화 덧셈 테스트

```python
def test_mixed_addition(self):
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert Money.dollar(10) == result  # $5 + 10 CHF = $10
```

### Green: Expression 인터페이스 확장

```python
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        pass
```

### Refactor: Sum.plus()와 Sum.times() 구현

```python
class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend = augend
        self.addend = addend

    def plus(self, addend: Expression) -> Expression:
        """Sum + Expression = 새로운 Sum"""
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        """Sum의 각 피연산자에 배수 적용"""
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def reduce(self, bank, to_currency):
        amount = self.augend.reduce(bank, to_currency)._amount + \
                 self.addend.reduce(bank, to_currency)._amount
        return Money(amount, to_currency)
```

## 전체 코드

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        pass


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank, to_currency):
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount // rate, to_currency)


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend = augend
        self.addend = addend

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def reduce(self, bank, to_currency):
        amount = self.augend.reduce(bank, to_currency)._amount + \
                 self.addend.reduce(bank, to_currency)._amount
        return Money(amount, to_currency)
```

## 구현된 기능

- ✅ **$5 + 10 CHF = $10** (환율 2:1)
- ✅ Sum.plus() - Sum + Expression
- ✅ Sum.times() - Sum \* multiplier
- ✅ Expression 완전 일반화

## 새 테스트 케이스

```python
def test_mixed_addition(self):
    """$5 + 10 CHF = $10 (rate 2:1)"""

def test_sum_plus_money(self):
    """($5 + 10 CHF) + $5 = $15"""

def test_sum_times(self):
    """($5 + 10 CHF) * 2 = $20"""
```

## TODO 리스트 (모두 완료!)

- [x] $5 + 10 CHF = $10 (환율이 2:1일 경우) ← **완료!**
- [x] $5 + $5 = $10
- [x] $5 + $5가 Sum을 반환
- [x] Bank.reduce(Sum)
- [x] Money.reduce (같은 통화)
- [x] Reduce Money with conversion
- [x] Reduce(Bank, String)
- [x] **Sum.plus**
- [x] **Expression.times**

## Part 1 완료!

Chapter 1에서 시작한 "$5 + 10 CHF = $10" 테스트가 완전히 통과!
Sum.plus, Expression.times까지 모두 구현 완료.

## 테스트 실행

```bash
python -m pytest part01/ch15/ -v
```
