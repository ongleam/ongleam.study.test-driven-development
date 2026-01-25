# Chapter 2: Degenerate Objects

## 목표

- Side effect 제거
- `times()` 메서드가 새로운 Dollar 객체를 반환하도록 변경

## 이전 챕터와의 차이

| 항목             | Chapter 1        | Chapter 2      |
| ---------------- | ---------------- | -------------- |
| `times()` 반환   | 없음 (void)      | 새 Dollar 객체 |
| Side effect      | 있음 (객체 수정) | 없음           |
| 동일 객체 재사용 | 불가능           | 가능           |

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_multiplication(self):
    five = Dollar(5)
    product = five.times(2)
    assert 10 == product.amount
    product = five.times(3)  # 같은 five로 다시 곱셈!
    assert 15 == product.amount  # side effect 있으면 30이 됨
```

**핵심**: 같은 `five` 객체로 두 번 곱셈. Side effect가 있다면 `five.times(3)`은 `15`가 아닌 `30`이 됨.

### 2. Green: 구현

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # side effect 제거: 새 Dollar 객체 반환
        return Dollar(self.amount * multiplier)
```

### 3. Refactor

- 객체 수정 → 새 객체 생성으로 변경

## 구현된 기능

- ✅ Side effect 제거
- ✅ `times()` 메서드가 새로운 Dollar 객체 반환
- ✅ 동일 객체로 여러 번 연산 가능

## 학습 포인트

1. **값 객체(Value Object)**: 연산 결과는 새 객체로 반환
2. **Side effect 제거**: 메서드 호출이 객체 상태를 변경하지 않음
3. **"feeling → test" 변환**: side effect에 대한 불편함을 테스트로 표현
4. **암묵적 검증**: 별도 immutability 테스트 없이, 같은 객체 재사용으로 검증

## Kent Beck 인용

> "The translation of a feeling (for example, disgust at side effects) into a test (for example, multiply the same Dollar twice) is a common theme of TDD."

## 문제점 (다음 챕터에서 해결)

- ⚠️ 동등성 비교(`==`)가 불가능
- ⚠️ `product.amount`로 직접 비교해야 함
