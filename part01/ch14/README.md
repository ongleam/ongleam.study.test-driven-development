# Chapter 14: Change

> "2 CHF = 1 USD" - Kent Beck

📌 **패턴**: -

## 목표

- 환율 변환 기능 추가
- Bank에 환율을 등록하고, Money.reduce()에서 통화 변환을 수행

## 이전 챕터와의 차이

| 항목           | Chapter 13     | Chapter 14              |
| -------------- | -------------- | ----------------------- |
| Money.reduce() | 자기 자신 반환 | 환율 적용 후 반환       |
| Bank           | reduce()만     | add_rate(), rate() 추가 |
| 환율 저장      | 없음           | Pair 클래스 + dict      |

## 핵심 학습 포인트

1. **해시 테이블 키**: Pair 객체를 키로 사용하려면 `__eq__`와 `__hash__` 필요
2. **Identity Rate**: 같은 통화 변환은 항상 1 (USD → USD)
3. **Bank의 책임**: 환율 관리는 Bank의 역할

## TDD 사이클

### Red: 환율 변환 테스트

```python
def test_reduce_money_different_currency(self):
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result  # 2 CHF → 1 USD
```

### Green: 환율 구현

```python
class Pair:
    def __init__(self, from_currency: str, to_currency: str):
        self._from = from_currency
        self._to = to_currency

    def __eq__(self, other):
        return self._from == other._from and self._to == other._to

    def __hash__(self):
        return hash((self._from, self._to))


class Bank:
    def __init__(self):
        self._rates: dict[Pair, int] = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: int):
        self._rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency:
            return 1  # 같은 통화
        return self._rates[Pair(from_currency, to_currency)]
```

### Refactor: Money.reduce() 통화 변환

```python
# Chapter 13
def reduce(self, bank, to_currency):
    return self  # 변환 없음

# Chapter 14
def reduce(self, bank, to_currency):
    rate = bank.rate(self._currency, to_currency)
    return Money(self._amount // rate, to_currency)
```

## 전체 코드

```python
class Pair:
    def __init__(self, from_currency: str, to_currency: str):
        self._from = from_currency
        self._to = to_currency

    def __eq__(self, other):
        return self._from == other._from and self._to == other._to

    def __hash__(self):
        return hash((self._from, self._to))


class Bank:
    def __init__(self):
        self._rates: dict[Pair, int] = {}

    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)

    def add_rate(self, from_currency: str, to_currency: str, rate: int):
        self._rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency:
            return 1
        return self._rates[Pair(from_currency, to_currency)]


class Money(Expression):
    def reduce(self, bank, to_currency):
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount // rate, to_currency)
```

## 구현된 기능

- ✅ Pair 클래스 - 환율 키
- ✅ Bank.add_rate() - 환율 등록
- ✅ Bank.rate() - 환율 조회
- ✅ Money.reduce() - 통화 변환
- ✅ Identity Rate (같은 통화 = 1)

## TODO 리스트

- [x] $5 + 10 CHF = $10 (환율이 2:1일 경우)
- [x] $5 + $5 = $10
- [x] $5 + $5가 Sum을 반환
- [x] Bank.reduce(Sum)
- [x] Money.reduce (같은 통화)
- [x] **Reduce Money with conversion**
- [x] **Reduce(Bank, String)**
- [ ] Sum.plus
- [ ] Expression.times

## 다음 챕터 예고

- ⚠️ Sum.plus() 필요
- ⚠️ Expression.times() 필요
- ⚠️ 다중 통화 덧셈 완성

## 테스트 실행

```bash
python -m pytest part01/ch14/ -v
```
