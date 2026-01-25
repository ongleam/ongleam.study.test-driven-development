# Chapter 14: Change

## 핵심 개념

**환율 변환 기능 추가**

Bank에 환율을 등록하고, Money.reduce()에서 통화 변환을 수행한다.

> "2 CHF = 1 USD" - Kent Beck

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

## 핵심 변경사항

### 1. Pair 클래스 - 환율 키

```python
class Pair:
    def __init__(self, from_currency: str, to_currency: str):
        self._from = from_currency
        self._to = to_currency

    def __eq__(self, other): ...
    def __hash__(self): ...
```

### 2. Bank.add_rate() - 환율 등록

```python
class Bank:
    def __init__(self):
        self._rates: dict[Pair, int] = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: int):
        self._rates[Pair(from_currency, to_currency)] = rate
```

### 3. Bank.rate() - 환율 조회

```python
def rate(self, from_currency: str, to_currency: str) -> int:
    if from_currency == to_currency:
        return 1  # 같은 통화
    return self._rates[Pair(from_currency, to_currency)]
```

### 4. Money.reduce() - 통화 변환

```python
# Chapter 13
def reduce(self, bank, to_currency):
    return self  # 변환 없음

# Chapter 14
def reduce(self, bank, to_currency):
    rate = bank.rate(self._currency, to_currency)
    return Money(self._amount // rate, to_currency)
```

## 테스트

```bash
python -m pytest part01/ch14/ -v
```

## TDD 사이클

1. **Red**: `test_reduce_money_different_currency` - 2 CHF → 1 USD
2. **Green**: Bank.add_rate(), Bank.rate(), Money.reduce() 수정
3. **Refactor**: Pair 클래스로 환율 키 추상화

## 배운 점

- **해시 테이블 키** - Pair 객체를 키로 사용하려면 `__eq__`와 `__hash__` 필요
- **Identity Rate** - 같은 통화 변환은 항상 1 (USD → USD)
- **Bank의 책임** - 환율 관리는 Bank의 역할
