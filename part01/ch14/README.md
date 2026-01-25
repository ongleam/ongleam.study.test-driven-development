# Chapter 14: Change

## 목표

- 환율 변환 기능 구현
- Bank가 환율 관리

## 이전 챕터와의 차이

- `Bank` 클래스에 `_rates` 딕셔너리 추가
- `Bank.add_rate()` 메서드로 환율 등록
- `Bank.rate()` 메서드로 환율 조회
- `Money.reduce()`가 환율 적용하여 변환

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_reduce_money_different_currency(self):
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(franc(2), "USD")
    assert dollar(1) == result
```

### 2. Green: 구현

```python
class Bank:
    def __init__(self):
        self._rates = {}

    def add_rate(self, from_currency, to_currency, rate):
        key = (from_currency, to_currency)
        self._rates[key] = rate

    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        key = (from_currency, to_currency)
        return self._rates.get(key, 1)

class Money(Expression):
    def reduce(self, bank, to_currency):
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount / rate, to_currency)
```

### 3. Refactor

- 딕셔너리로 환율 저장
- 튜플 키 사용
- Identity rate (같은 통화 = 1)

## 구현된 기능

- ✅ 환율 등록 (add_rate)
- ✅ 환율 조회 (rate)
- ✅ 통화 간 변환
- ✅ Identity rate (USD->USD = 1)

## 학습 포인트

1. **환율 관리**: 딕셔너리로 from-to 쌍 저장
2. **Identity 처리**: 같은 통화는 환율 1
3. **책임 분리**: Bank가 환율 관리, Money가 변환 수행
4. **점진적 기능 추가**: 기존 테스트 깨지지 않음

## 문제점 (다음 챕터에서 해결)

- 다른 통화 간 덧셈 미지원
- Sum이 다중 통화 처리 못함
