# Chapter 3: Equality for All

## 목표

- Dollar 객체 간 동등성 비교 구현
- `==` 연산자를 사용한 값 비교 가능하게 만들기

## 이전 챕터와의 차이

| 항목        | Chapter 2              | Chapter 3               |
| ----------- | ---------------------- | ----------------------- |
| 동등성 비교 | `product.amount == 10` | `product == Dollar(10)` |
| `__eq__`    | 미구현                 | 구현                    |
| `__hash__`  | 미구현                 | 구현                    |

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_equality(self):
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
```

### 2. Green: 구현

```python
def __eq__(self, other):
    if not isinstance(other, Dollar):
        return False
    return self._amount == other._amount

def __hash__(self):
    return hash(self._amount)
```

### 3. Refactor

- `isinstance()`로 타입 체크 추가
- `_amount`를 private 변수로 변경

## 전체 코드

```python
class Dollar:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return False
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)
```

## 구현된 기능

- ✅ `==` 연산자로 Dollar 객체 비교
- ✅ `!=` 연산자로 불일치 확인
- ✅ 해시 가능한 객체 (집합, 딕셔너리 키로 사용 가능)
- ✅ `_amount` private 변수로 캡슐화

## 학습 포인트

1. **값 객체(Value Object)**: 동등성이 속성값으로 결정됨
2. **`__eq__` 구현**: Python의 동등성 비교 커스터마이징
3. **`__hash__` 구현**: `__eq__`를 오버라이드하면 `__hash__`도 구현해야 함
4. **삼각측량(Triangulation)**: 두 개의 예제(`Dollar(5) == Dollar(5)`, `Dollar(5) != Dollar(6)`)로 일반화

## 테스트 목록

```python
def test_multiplication(self):      # Chapter 2에서 완성
    five = Dollar(5)
    product = five.times(2)
    assert 10 == product.amount
    product = five.times(3)
    assert 15 == product.amount

def test_equality(self):            # Chapter 3에서 추가
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
```

## 문제점 (다음 챕터에서 해결)

- ⚠️ 테스트가 여전히 `product.amount`에 직접 접근
- ⚠️ 동등성 비교를 활용하여 테스트 개선 필요
