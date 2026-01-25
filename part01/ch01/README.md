# Chapter 1: Multi-Currency Money

## 목표

- TDD의 기본 사이클(Red-Green-Refactor) 시작
- 가장 간단한 곱셈 기능 구현

## 이전 챕터와의 차이

- 첫 번째 챕터 (시작점)

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_multiplication(self):
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount
```

### 2. Green: 최소 구현

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier  # side effect: 객체 자체를 수정
```

### 3. Refactor

- 이 단계에서는 리팩토링 없음 (최소 구현)

## 구현된 기능

- ✅ Dollar 클래스
- ✅ times() 메서드로 곱셈 (side effect 방식)

## 학습 포인트

1. **테스트 먼저**: 실패하는 테스트부터 시작
2. **가장 간단한 구현**: 테스트를 통과하는 최소한의 코드
3. **작은 단계**: 한 번에 하나씩

## 문제점 (다음 챕터에서 해결)

- ⚠️ **Side Effect**: `times()` 호출 시 객체 자체가 변경됨
- ⚠️ 같은 Dollar 객체로 여러 번 곱셈 불가능
- ⚠️ 동등성 비교 불가능
