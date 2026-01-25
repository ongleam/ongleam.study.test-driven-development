# Chapter 3: Equality for All

> "Value Objects are a useful idiom when you're dealing with immutable values that have meaningful equality." - Kent Beck

📌 **패턴**: Value Object, Triangulation

## 목표

- Dollar 객체 간 동등성 비교 구현
- `==` 연산자를 사용한 값 비교 가능하게 만들기

## 이전 챕터와의 차이

| 항목        | Chapter 2              | Chapter 3               |
| ----------- | ---------------------- | ----------------------- |
| 동등성 비교 | `product.amount == 10` | `product == Dollar(10)` |
| `__eq__`    | 미구현                 | 구현                    |
| `__hash__`  | 미구현                 | 구현                    |

## 핵심 학습 포인트

1. **값 객체(Value Object)**: 동등성이 속성값으로 결정됨
2. **`__eq__` 구현**: Python의 동등성 비교 커스터마이징
3. **`__hash__` 구현**: `__eq__`를 오버라이드하면 `__hash__`도 구현해야 함
4. **삼각측량(Triangulation)**: 두 개의 예제(`Dollar(5) == Dollar(5)`, `Dollar(5) != Dollar(6)`)로 일반화

## TDD 사이클

### Red: 실패하는 테스트

```python
def test_equality(self):
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
```

### Green: 최소 구현

```python
def __eq__(self, other):
    if not isinstance(other, Dollar):
        return False
    return self.amount == other.amount

def __hash__(self):
    return hash(self.amount)
```

### Refactor: 개선

- `isinstance()`로 타입 체크 추가

## 전체 코드

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return False
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)
```

## 구현된 기능

- ✅ `==` 연산자로 Dollar 객체 비교
- ✅ `!=` 연산자로 불일치 확인
- ✅ 해시 가능한 객체 (집합, 딕셔너리 키로 사용 가능)

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

## 다음 챕터 예고

- ⚠️ 테스트가 여전히 `product.amount`에 직접 접근
- ⚠️ 동등성 비교를 활용하여 테스트 개선 필요

## 테스트 실행

```bash
python -m pytest part01/ch03/ -v
```
