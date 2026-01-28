# Chapter 28: Green Bar Patterns

> "명백한 구현은 2단 기어다. 뇌가 발행한 수표를 손가락이 현금화하지 못하면 기어를 낮출 준비를 하라." - Kent Beck

## 개요

빨간 막대를 초록 막대로 바꾸는 전략들. 테스트를 통과시키는 세 가지 주요 방법을 다룬다.

## 세 가지 전략

```
확신 있음                           확신 없음
    ←─────────────────────────────────→

Obvious Implementation → Fake It → Triangulate
     (명백한 구현)        (가짜로)    (삼각측량)
```

## 패턴 목록

### 1. Fake It ('Til You Make It) - 가짜로 구현하기

**문제**: 실패하는 테스트가 있을 때 첫 번째 구현은 어떻게 하는가?

**해결**: 상수를 반환한다. 그 다음 점진적으로 상수를 변수로 바꾸어 실제 코드를 만든다.

```python
# Step 1: 테스트 작성 (Red)
def test_sum(self):
    assert sum([1, 2, 3]) == 6

# Step 2: Fake It (Green)
def sum(numbers):
    return 6  # 하드코딩!

# Step 3: 점진적 일반화
def sum(numbers):
    result = 0
    for n in numbers:
        result += n
    return result
```

**Part 1 Money 예제**:

```python
# Fake It
def test_multiplication(self):
    five = Dollar(5)
    assert five.times(2).amount == 10

class Dollar:
    def times(self, multiplier):
        return Dollar(10)  # Fake It!

# 점진적 일반화
class Dollar:
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
```

**언제 사용하는가**:

- 올바른 구현이 명확하지 않을 때
- 작은 걸음으로 확신을 얻고 싶을 때
- 예상치 못한 빨간 막대를 만났을 때

### 2. Triangulate (삼각측량)

**문제**: 추상화가 확실하지 않을 때 어떻게 가장 보수적으로 코드를 작성하는가?

**해결**: 두 개 이상의 예제가 있을 때만 추상화한다.

```python
# 예제 1개 - 아직 추상화하지 않음
def test_sum_single(self):
    assert sum([5]) == 5

def sum(numbers):
    return 5  # Fake It 유지

# 예제 2개 - 이제 추상화
def test_sum_single(self):
    assert sum([5]) == 5

def test_sum_multiple(self):
    assert sum([1, 2]) == 3  # 두 번째 예제!

def sum(numbers):
    # 두 테스트를 모두 통과하려면 일반화 필요
    result = 0
    for n in numbers:
        result += n
    return result
```

**Part 1에서의 사용**:

```python
# Chapter 3: Triangulation으로 equals 일반화
def test_equality(self):
    assert Dollar(5) == Dollar(5)
    assert not Dollar(5) == Dollar(6)  # 두 번째 예제

def __eq__(self, other):
    # 두 테스트가 있으니 이제 일반화
    return self.amount == other.amount
```

**언제 사용하는가**:

- 올바른 추상화가 정말로 불확실할 때
- 설계 결정을 미루고 싶을 때
- Kent Beck: "정말, 정말 확신이 없을 때만 사용"

### 3. Obvious Implementation (명백한 구현)

**문제**: 간단한 연산을 어떻게 구현하는가?

**해결**: 그냥 구현한다.

```python
# 명백한 구현 - 바로 작성
def test_sum(self):
    assert sum([1, 2, 3]) == 6

def sum(numbers):
    result = 0
    for n in numbers:
        result += n
    return result
```

**언제 사용하는가**:

- 무엇을 타이핑해야 할지 알 때
- 구현이 머릿속에서 명확할 때
- 자신감이 있을 때

**주의사항**:

- 예상치 못한 빨간 막대가 나오면 즉시 Fake It으로 전환
- "2단 기어" - 필요하면 기어를 낮출 준비

### 4. One to Many (하나에서 여러 개로)

**문제**: 컬렉션을 다루는 연산은 어떻게 구현하는가?

**해결**: 먼저 컬렉션 없이 구현한 다음, 컬렉션을 사용하도록 변경한다.

```python
# Step 1: 단일 요소로 시작
def test_sum_single(self):
    assert sum(5) == 5

def sum(value):
    return value

# Step 2: 컬렉션으로 확장
def test_sum_collection(self):
    assert sum([1, 2, 3]) == 6

def sum(values):
    if isinstance(values, int):
        values = [values]
    result = 0
    for v in values:
        result += v
    return result

# Step 3: 리팩토링 (단일 값 지원 제거)
def sum(values):
    result = 0
    for v in values:
        result += v
    return result
```

**Part 1에서의 사용**:

```python
# Money 예제: 단일 통화 → 다중 통화
# Step 1: 단일 통화 덧셈
five = Dollar(5)
result = five.plus(Dollar(5))

# Step 2: 다중 통화 (Bank, Expression 도입)
five_bucks = Money.dollar(5)
ten_francs = Money.franc(10)
result = bank.reduce(five_bucks.plus(ten_francs), "USD")
```

## 전략 선택 가이드

```
무엇을 타이핑해야 할지 안다
    → Obvious Implementation

무엇을 타이핑해야 할지 모른다
    → Fake It

올바른 설계가 여전히 불명확하다
    → Triangulate

그래도 모르겠다
    → 샤워하러 가라 (Break 패턴)
```

## 실전 워크플로우

```
1. 테스트 작성 (Red)
           ↓
2. 명백한 구현 시도
           ↓
   성공? ─→ 다음 테스트로
           ↓ (실패)
3. Fake It으로 전환
           ↓
4. 리팩토링하며 일반화
           ↓
5. 자신감 회복 → 명백한 구현으로 복귀
```

## 핵심 원칙

1. **작은 걸음**: Fake It과 Triangulate는 "아주아주 작은 걸음"
2. **자신감 기반**: 자신감이 있으면 명백한 구현, 없으면 Fake It
3. **유연한 전환**: 상황에 따라 전략을 바꿀 준비
4. **테스트가 운전석**: 항상 테스트가 구현을 이끔

## 다음 챕터 예고

- Chapter 29: xUnit Patterns
- Assertion, Fixture, Test Method 등 xUnit 사용 패턴
