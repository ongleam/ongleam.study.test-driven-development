# Chapter 12: Addition, Finally

## 목표

- 덧셈 기능 구현 (`$5 + $5 = $10`)
- Expression 인터페이스 도입
- Sum 클래스 도입 (Composite 패턴)
- Bank.reduce() stub 구현

## TDD 패턴: "Fake It"

이 챕터는 "Fake It" 패턴을 사용합니다:

1. 실패하는 테스트 작성
2. 가장 간단한 방법으로 테스트 통과 (stub/fake)
3. 다음 챕터에서 "Make It" - 실제 구현으로 대체

## 이전 챕터와의 차이

| 항목       | Chapter 11 | Chapter 12                    |
| ---------- | ---------- | ----------------------------- |
| 클래스     | Money만    | Money, Expression, Sum, Bank  |
| 덧셈       | 없음       | `plus()` 메서드               |
| Expression | 없음       | 마커 인터페이스 (reduce 없음) |
| Bank       | 없음       | `reduce()` stub               |

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

### 2. Green: "Fake It" - Stub 구현

**Expression (마커 인터페이스):**

```python
class Expression:
    pass  # reduce() 메서드 아직 없음
```

**Sum (reduce 없음):**

```python
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend
    # reduce() 메서드 아직 없음
```

**Bank.reduce() - Stub:**

```python
class Bank:
    def reduce(self, source, to_currency):
        # isinstance() 체크 - 다형성 없음
        if isinstance(source, Money):
            return source
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)
```

### 3. 문제점 인식 (다음 챕터에서 해결)

현재 Bank.reduce()의 문제:

- Bank가 모든 Expression 타입을 알아야 함
- isinstance() 체크는 OOP 안티패턴
- 새 Expression 타입 추가 시 Bank 수정 필요

## 구현된 기능

- ✅ `Money.plus()` - Sum 반환
- ✅ `Expression` 마커 인터페이스
- ✅ `Sum` 클래스 (augend, addend)
- ✅ `Bank.reduce()` stub (isinstance 체크)

## 미구현 기능 (Chapter 13에서)

- ❌ `Expression.reduce()` 메서드
- ❌ `Money.reduce()` 메서드
- ❌ `Sum.reduce()` 메서드
- ❌ 다형성 기반 Bank.reduce()

## 학습 포인트

1. **Fake It**: 가장 간단한 방법으로 테스트 통과
2. **지연 평가**: plus()는 계산하지 않고 Sum 반환
3. **Composite 패턴**: Sum은 두 Expression을 포함
4. **Code Smell 인식**: isinstance() 체크는 개선 필요

## Kent Beck TDD 패턴

> **Fake It (Till You Make It)**: Return a constant and gradually replace constants with variables until you have the real code.

테스트를 통과시키기 위해 가장 간단한 구현을 먼저 작성하고, 나중에 실제 구현으로 대체합니다.

## Chapter 12 vs Chapter 13

```
Chapter 12 (이번 챕터):
├── Expression: 마커 인터페이스 (pass)
├── Sum: reduce() 없음
├── Money: reduce() 없음
└── Bank.reduce(): isinstance() 체크 (stub)

Chapter 13 (다음 챕터):
├── Expression: reduce() 정의
├── Sum: reduce() 구현
├── Money: reduce() 구현
└── Bank.reduce(): source.reduce() 호출 (다형성)
```
