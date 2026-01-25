# Chapter 13: Make It

> "We have duplication between the data in the test and the data in the code. We have to eliminate it." - Kent Beck

📌 **패턴**: Triangulation, Polymorphism

## 목표

- "Fake It"에서 실제 구현으로 전환
- 테스트 데이터($5 + $5 = **$10**)와 코드 데이터(**10**)의 중복 제거
- 다형성으로 Bank.reduce() 단순화

## 이전 챕터와의 차이

| 항목           | Chapter 12      | Chapter 13           |
| -------------- | --------------- | -------------------- |
| Bank.reduce()  | 하드코딩 (Fake) | 다형성 (실제 구현)   |
| Sum.reduce()   | 없음            | 실제 덧셈 구현       |
| Money.reduce() | 없음            | 자기 자신 반환       |
| Expression     | 마커 인터페이스 | reduce() 추상 메서드 |

## 핵심 학습 포인트

1. **"Fake It"은 임시**: 빨리 테스트를 통과시키기 위한 전략
2. **데이터 중복 제거**: 테스트와 코드의 중복된 상수 제거
3. **다형성**: Bank가 Sum인지 Money인지 알 필요 없음

## TDD 사이클

### Red: 새 테스트로 하드코딩 깨뜨리기

```python
def test_reduce_sum(self):
    sum_result = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum_result, "USD")
    assert Money.dollar(7) == result  # 하드코딩 $10으로는 실패!
```

### Green: 실제 구현

```python
# Chapter 12 (Fake It)
class Bank:
    def reduce(self, source, to_currency):
        return Money.dollar(10)  # 하드코딩!

# Chapter 13 (Make It)
class Sum(Expression):
    def reduce(self, bank, to_currency):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to_currency)
```

### Refactor: 다형성 활용

```python
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        pass

class Money(Expression):
    def reduce(self, bank, to_currency):
        return self  # 자기 자신 반환

class Bank:
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)  # 다형성!
```

## 전체 코드

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        pass


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def reduce(self, bank, to_currency):
        return self

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

    def reduce(self, bank, to_currency):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to_currency)


class Bank:
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)
```

## 구현된 기능

- ✅ Expression에 reduce() 추상 메서드
- ✅ Sum.reduce() 실제 구현
- ✅ Money.reduce() 자기 자신 반환
- ✅ Bank.reduce() 다형성 활용

## TODO 리스트

- [x] $5 + 10 CHF = $10 (환율이 2:1일 경우)
- [x] **$5 + $5 = $10**
- [x] **$5 + $5가 Sum을 반환**
- [x] **Bank.reduce(Sum)**
- [x] **Money.reduce (같은 통화)**
- [ ] Reduce Money with conversion
- [ ] Reduce(Bank, String)

## 다음 챕터 예고

- ⚠️ 환율 변환 기능 필요
- ⚠️ Bank에 환율 등록 필요
- ⚠️ Money.reduce()에서 통화 변환

## 테스트 실행

```bash
python -m pytest part01/ch13/ -v
```
