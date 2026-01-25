# Chapter 7: Apples and Oranges

> "Using classes like this in model code is a bit smelly." - Kent Beck

📌 **패턴**: -

## 목표

- Dollar와 Franc 비교 문제 해결
- `getClass()` (Python: `type()`) 비교 추가
- "사과와 오렌지는 비교할 수 없다"

## 이전 챕터와의 차이

| 항목                    | Chapter 6    | Chapter 7     |
| ----------------------- | ------------ | ------------- |
| `Dollar(5) == Franc(5)` | True (버그!) | False (해결)  |
| `__eq__` 비교           | amount만     | amount + type |

## 핵심 학습 포인트

1. **getClass() 사용**: 정확한 런타임 타입 비교
2. **Code Smell**: "Using classes like this in model code is a bit smelly" - Kent Beck
3. **임시 해결책**: 나중에 통화(currency) 개념으로 대체될 예정

## TDD 사이클

### Red: 실패하는 테스트 발견

```python
def test_different_class_equality(self):
    assert Dollar(5) != Franc(5)  # Chapter 6에서 실패!
```

Kent Beck: "Dollars are Francs" - 이 버그를 발견

### Green: getClass() 비교 추가

```python
class Money:
    def __eq__(self, other):
        # amount와 class가 모두 같아야 동등
        return self._amount == other._amount and type(self) == type(other)
```

Java 원본:

```java
public boolean equals(Object object) {
    Money money = (Money) object;
    return amount == money.amount
        && getClass().equals(money.getClass());
}
```

### Refactor: 개선

- Money 클래스의 `__eq__`만 수정
- Dollar, Franc의 중복 `__eq__` 불필요

## 전체 코드

```python
class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
```

## 구현된 기능

- ✅ `Dollar(5) != Franc(5)` 이제 True
- ✅ `type()` 비교로 클래스 구분
- ✅ Money 상위 클래스에서 통합 관리

## 다음 챕터 예고

- ⚠️ Dollar와 Franc의 times() 중복
- ⚠️ 클래스 대신 통화(currency) 개념 필요
- ⚠️ 팩토리 메서드 필요

## 테스트 실행

```bash
python -m pytest part01/ch07/ -v
```
