# Chapter 12: Addition, Finally

## 목표

- 덧셈 기능 구현 (`$5 + $5 = $10`)
- Expression 인터페이스 도입
- Bank와 reduce 개념 도입
- Sum 클래스 (Composite 패턴)

## 이전 챕터와의 차이

| 항목       | Chapter 11 | Chapter 12                   |
| ---------- | ---------- | ---------------------------- |
| 클래스     | Money만    | Money, Expression, Sum, Bank |
| 덧셈       | 없음       | `plus()` 메서드              |
| Expression | 없음       | 마커 인터페이스              |
| Bank       | 없음       | `reduce()` 메서드            |

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_simple_addition(self):
    five = Money.dollar(5)
    sum_result = five.plus(Money.dollar(5))
    bank = Bank()
    reduced = bank.reduce(sum_result, "USD")
    assert Money.dollar(10) == reduced
```

### 2. Green: 구현

**Expression 인터페이스:**

```python
class Expression:
    """금액 계산을 나타내는 인터페이스"""
    pass
```

**Money.plus():**

```python
class Money(Expression):
    def plus(self, addend):
        return Sum(self, addend)  # 지연 평가
```

**Sum 클래스 (Composite 패턴):**

```python
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend  # 피가산수
        self.addend = addend  # 가산수
```

**Bank.reduce():**

```python
class Bank:
    def reduce(self, source, to_currency):
        if isinstance(source, Money):
            return source
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)
```

### 3. Refactor

- Expression 계층 구조 정립
- Bank를 통한 변환 책임 분리

## 전체 코드

```python
class Expression:
    pass


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend


class Bank:
    def reduce(self, source, to_currency):
        if isinstance(source, Money):
            return source
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)
```

## 구현된 기능

- ✅ `Money.plus()` - 덧셈 (Sum 반환)
- ✅ `Expression` 인터페이스 (마커 클래스)
- ✅ `Sum` 클래스 - 두 Expression의 합
- ✅ `Bank.reduce()` - Expression을 Money로 변환

## 학습 포인트

1. **Expression 패턴**: 계산을 객체로 표현 (표현식 트리)
2. **지연 평가**: `plus()`는 즉시 계산하지 않고 Sum 반환
3. **Composite 패턴**: Sum은 두 Expression을 포함
4. **Bank의 역할**: 환율 변환 책임을 Bank에 위임

## Kent Beck 인용

> "Beck notes in passing as he is working towards an implementation of a Sum class that it looks like a Composite pattern."

Sum 클래스는 Composite 패턴의 예시입니다. 단순한 Money도, 복합적인 Sum도 모두 Expression으로 표현됩니다.

## 핵심 개념: 지연 평가

```python
five = Money.dollar(5)
sum_result = five.plus(Money.dollar(5))  # 아직 계산 안 함!
# sum_result는 Sum(Money(5, "USD"), Money(5, "USD"))

bank = Bank()
reduced = bank.reduce(sum_result, "USD")  # 이제 계산!
# reduced는 Money(10, "USD")
```

## 문제점 (다음 챕터에서 해결)

- ⚠️ `reduce()`가 같은 통화만 처리
- ⚠️ 환율 변환 미지원 (`$5 + 10 CHF`)
- ⚠️ `Sum.reduce()` 메서드 필요
- ⚠️ `Money.reduce()` 메서드 필요

## Sources

- [Money monoid](https://blog.ploeh.dk/2017/10/16/money-monoid/) - Expression 패턴 설명
- [Kent Beck's Money example](https://aftabquraishi.wordpress.com/2012/07/01/kent-becks-money-example-using-csharp-and-visual-studio-unit-testing-framework/) - C# 구현 예제
