# Chapter 6: Equality for All, Redux

> "We want common equals code, so we'll move it to the common superclass." - Kent Beck

📌 **패턴**: Pull Up Method

## 목표

- Dollar와 Franc의 중복 코드 제거
- 공통 상위 클래스 `Money` 도입
- `__eq__` 메서드를 상위 클래스로 이동

## 이전 챕터와의 차이

| 항목          | Chapter 5          | Chapter 6                  |
| ------------- | ------------------ | -------------------------- |
| 클래스 구조   | Dollar, Franc 독립 | Money ← Dollar, Franc 상속 |
| `__eq__` 위치 | 각 클래스에 중복   | Money에 통합               |
| 코드 중복     | 있음               | 제거됨                     |

## 핵심 학습 포인트

1. **상속을 통한 중복 제거**: 공통 코드를 상위 클래스로 이동
2. **점진적 리팩토링**: 테스트가 통과하는 상태 유지하면서 변경
3. **리스코프 치환 원칙**: 하위 클래스는 상위 클래스를 대체할 수 있어야 함

## TDD 사이클

### Red: 문제 인식 - 중복 코드

```python
# Dollar
def __eq__(self, other):
    if not isinstance(other, Dollar):
        return False
    return self._amount == other._amount

# Franc (거의 동일!)
def __eq__(self, other):
    if not isinstance(other, Franc):
        return False
    return self._amount == other._amount
```

### Green: Money 상위 클래스 도입

```python
class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
```

### Refactor: 개선

- Dollar의 `__eq__`를 Money로 이동
- Franc의 `__eq__`를 삭제 (Money 상속)
- `isinstance(other, Dollar)` → `isinstance(other, Money)`

## 전체 코드

```python
class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
```

## 구현된 기능

- ✅ Money 상위 클래스
- ✅ Dollar, Franc이 Money 상속
- ✅ `__eq__` 중복 제거

## Kent Beck의 리팩토링 단계

1. Dollar의 `_amount`를 protected로 변경 (Money에서 접근 가능)
2. `__eq__`의 일부를 Dollar에서 Money로 이동
3. 테스트 통과 확인
4. Franc에서도 동일하게 적용
5. 중복된 Franc의 `__eq__` 삭제

## 다음 챕터 예고

- ⚠️ **Dollar(5) == Franc(5)가 True!**
- ⚠️ 서로 다른 통화인데 같다고 판단됨
- ⚠️ 다음 챕터 "Apples and Oranges"에서 해결

## 테스트 실행

```bash
python -m pytest part01/ch06/ -v
```
