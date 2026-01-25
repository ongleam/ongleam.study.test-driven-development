# Chapter 12: Addition, Finally

## 목표

- 덧셈 기능 시작 (`$5 + $5 = $10`)
- Expression, Sum, Bank 도입
- "Fake It" 패턴으로 테스트 통과

## TDD 패턴: "Fake It"

Kent Beck:

> "Return a constant and gradually replace constants with variables until you have the real code."

이 챕터에서는 **진짜로 하드코딩**합니다:

```python
class Bank:
    def reduce(self, source, to_currency):
        return Money.dollar(10)  # 하드코딩!
```

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

### 2. Green: "Fake It" - 하드코딩

가장 빠르게 테스트를 통과시키는 방법: **하드코딩**

```python
class Bank:
    def reduce(self, source, to_currency):
        return Money.dollar(10)  # $5 + $5 = $10이니까!
```

### 3. 문제 인식

이 구현은 명백히 잘못되었습니다:

- `source`를 전혀 사용하지 않음
- `to_currency`도 무시
- 항상 `Dollar(10)` 반환

하지만 **테스트는 통과**합니다! 이것이 "Fake It"의 핵심입니다.

## 전체 코드

```python
class Expression:
    pass


class Money(Expression):
    def plus(self, addend):
        return Sum(self, addend)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend


class Bank:
    def reduce(self, source, to_currency):
        return Money.dollar(10)  # Fake It!
```

## 구현된 기능

- ✅ `Money.plus()` - Sum 반환
- ✅ `Expression` 마커 인터페이스
- ✅ `Sum` 클래스
- ✅ `Bank.reduce()` - **하드코딩** (Fake)

## 테스트

Chapter 12에서는 **오직 하나의 새 테스트**만 있습니다:

- `test_simple_addition`

## 학습 포인트

1. **Fake It**: 테스트를 통과시키는 가장 간단한 방법
2. **중복 = 미완성**: 테스트와 코드 사이의 중복(10)이 문제를 나타냄
3. **작은 단계**: 큰 도약 대신 작은 단계로 진행
4. **자신감**: 테스트가 통과하면 리팩토링 가능

## Kent Beck 인용

> "Fake It (Till You Make It): Return a constant and gradually replace constants with variables until you have the real code."

> "Duplication between test and code is a symptom of incomplete implementation."

## 다음 챕터에서 해결할 문제

Chapter 13 "Make It"에서:

- ❌ 하드코딩 제거
- ❌ 실제 계산 구현
- ❌ `test_plus_returns_sum` 추가
- ❌ `test_reduce_sum` 추가
- ❌ `test_reduce_money` 추가
- ❌ 다형성 도입
