# Chapter 1: Multi-Currency Money

> "Test-driven development is a way of managing fear during programming." - Kent Beck

📌 **패턴**: -

## 목표

- TDD의 기본 사이클(Red-Green-Refactor) 시작
- 가장 간단한 곱셈 기능 구현

## 이전 챕터와의 차이

| 항목   | 이전     | Chapter 1                 |
| ------ | -------- | ------------------------- |
| -      | (시작점) | Dollar 클래스             |
| 메서드 | -        | times() (side effect)     |
| 개념   | -        | Red-Green-Refactor 사이클 |

## 핵심 학습 포인트

1. **테스트 먼저**: 실패하는 테스트부터 시작
2. **가장 간단한 구현**: 테스트를 통과하는 최소한의 코드
3. **작은 단계**: 한 번에 하나씩

## TDD 사이클

### Red: 실패하는 테스트

```python
def test_multiplication(self):
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount
```

### Green: 최소 구현

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier  # side effect: 객체 자체를 수정
```

### Refactor: 개선

- 이 단계에서는 리팩토링 없음 (최소 구현)

## 전체 코드

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
```

## 구현된 기능

- ✅ Dollar 클래스
- ✅ times() 메서드로 곱셈 (side effect 방식)

## 다음 챕터 예고

- ⚠️ **Side Effect**: `times()` 호출 시 객체 자체가 변경됨
- ⚠️ 같은 Dollar 객체로 여러 번 곱셈 불가능
- ⚠️ 동등성 비교 불가능

## 테스트 실행

```bash
python -m pytest part01/ch01/ -v
```
