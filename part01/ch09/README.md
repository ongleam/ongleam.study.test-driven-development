# Chapter 9: Times We're Livin' In

## 목표

- 통화(currency) 개념 도입
- Dollar는 USD, Franc은 CHF

## 이전 챕터와의 차이

- Money 클래스에 `_currency` 필드 추가
- `currency()` 메서드 추가
- Dollar와 Franc의 생성자에서 통화 설정

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_currency(self):
    assert "USD" == dollar(1).currency()
    assert "CHF" == franc(1).currency()
```

### 2. Green: 구현

```python
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")
```

### 3. Refactor

- 통화를 생성자에서 부모로 전달

## 구현된 기능

- ✅ 통화 개념 도입
- ✅ Dollar는 "USD"
- ✅ Franc은 "CHF"
- ✅ currency() 메서드

## 학습 포인트

1. **도메인 개념 추가**: 현실 세계의 개념을 코드로
2. **생성자 체이닝**: super().**init**()로 부모 초기화
3. **상수 값**: 통화 코드를 문자열 상수로

## 문제점 (다음 챕터에서 해결)

- times() 메서드가 여전히 중복
- 통화를 사용하여 times()를 통합 가능
