# Chapter 13: Make It

## 목표

- Expression에 `reduce()` 메서드 추가
- 다형성을 활용한 reduce 구현
- `isinstance()` 체크 제거

## 이전 챕터와의 차이

| 항목           | Chapter 12        | Chapter 13               |
| -------------- | ----------------- | ------------------------ |
| Bank.reduce()  | isinstance() 체크 | 다형성 (source.reduce()) |
| Expression     | 마커 클래스       | reduce() 메서드 정의     |
| Money.reduce() | 없음              | self 반환                |
| Sum.reduce()   | 없음              | 재귀적 합산              |

## Red-Green-Refactor 사이클

### 1. Red: reduce 테스트 작성

```python
def test_reduce_money(self):
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result
```

### 2. Green: 다형성 구현

**Expression 인터페이스:**

```python
class Expression:
    def reduce(self, bank, to_currency):
        raise NotImplementedError
```

**Money.reduce():**

```python
class Money(Expression):
    def reduce(self, bank, to_currency):
        return self  # 같은 통화면 자기 자신 반환
```

**Sum.reduce():**

```python
class Sum(Expression):
    def reduce(self, bank, to_currency):
        amount = (self.augend.reduce(bank, to_currency)._amount +
                  self.addend.reduce(bank, to_currency)._amount)
        return Money(amount, to_currency)
```

**Bank.reduce() - isinstance() 제거:**

```python
class Bank:
    def reduce(self, source, to_currency):
        # 다형성: 타입 체크 없이 동작
        return source.reduce(self, to_currency)
```

### 3. Refactor

- isinstance() 체크 제거 → 다형성
- 각 클래스가 자신의 reduce() 구현

## 전체 코드

```python
class Expression:
    def reduce(self, bank, to_currency):
        raise NotImplementedError


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def reduce(self, bank, to_currency):
        return self

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

    def reduce(self, bank, to_currency):
        amount = (self.augend.reduce(bank, to_currency)._amount +
                  self.addend.reduce(bank, to_currency)._amount)
        return Money(amount, to_currency)


class Bank:
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)
```

## 구현된 기능

- ✅ `Expression.reduce()` 인터페이스
- ✅ `Money.reduce()` - 자기 자신 반환
- ✅ `Sum.reduce()` - 재귀적 합산
- ✅ `Bank.reduce()` - isinstance() 제거, 다형성 활용

## 학습 포인트

1. **다형성 (Polymorphism)**: 각 클래스가 자신의 reduce() 구현
2. **캡슐화**: Bank가 타입을 알 필요 없음
3. **재귀적 구조**: Sum.reduce()가 augend, addend의 reduce() 호출
4. **Double Dispatch**: Bank → Expression.reduce() → 각 구현

## Kent Beck 인용

> "Eliminating explicit class checks by leveraging polymorphism."

instanceof/isinstance 체크는 OOP의 안티패턴입니다. 다형성을 활용하면 새로운 Expression 타입 추가 시 Bank 수정이 필요 없습니다.

## Chapter 12 vs Chapter 13 비교

```python
# Chapter 12: Bank.reduce() with isinstance()
class Bank:
    def reduce(self, source, to_currency):
        if isinstance(source, Money):
            return source
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)

# Chapter 13: Bank.reduce() with polymorphism
class Bank:
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)  # 깔끔!
```

## 문제점 (다음 챕터에서 해결)

- ⚠️ 환율 변환 미지원
- ⚠️ `Money.reduce()`가 통화 변환 안 함
- ⚠️ `$5 + 10 CHF` 계산 불가

## Sources

- [Test-Driven Development by Example - Bookey](https://www.bookey.app/book/test-driven-development)
