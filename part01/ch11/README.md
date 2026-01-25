# Chapter 11: The Root of All Evil

## 목표

- Dollar와 Franc 서브클래스 제거
- Money 클래스만으로 모든 기능 구현
- 통화 기반으로 구분

## 이전 챕터와의 차이

- `Dollar`와 `Franc` 클래스 완전 제거
- `__eq__`에서 `type()` 대신 `_currency` 비교
- `times()`에서 조건문 제거, Money 직접 반환
- 팩토리 함수가 Money 객체 직접 생성

## Red-Green-Refactor 사이클

### 1. Red: 기존 테스트 유지

- 모든 테스트가 여전히 통과해야 함

### 2. Green: 구현

```python
class Money:
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def __eq__(self, other):
        return (self._amount == other._amount and
                self._currency == other._currency)

def dollar(amount):
    return Money(amount, "USD")
```

### 3. Refactor

- 서브클래스 완전 제거
- 통화 기반 동등성 비교
- 간결한 코드

## 구현된 기능

- ✅ Money 클래스만 존재
- ✅ 통화 기반 비교
- ✅ 조건문 없는 times()
- ✅ 팩토리 함수로 간단한 생성

## 학습 포인트

1. **중복의 악**: 불필요한 서브클래스 제거
2. **데이터 주도**: 타입이 아닌 데이터(통화)로 구분
3. **단순화**: 복잡한 상속 계층 제거
4. **리팩토링의 힘**: 테스트 덕분에 안전한 대규모 변경

## 문제점 (다음 챕터에서 해결)

- 아직 덧셈 기능 없음
- 다중 통화 계산 필요
