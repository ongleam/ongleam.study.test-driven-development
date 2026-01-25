# Chapter 15: Mixed Currencies

## 핵심 개념

**서로 다른 통화의 덧셈 + Expression 일반화**

드디어 Part 1의 최종 목표 달성!

> "$5 + 10 CHF = $10 if rate is 2:1" - Kent Beck

## TODO 리스트

- [x] **$5 + 10 CHF = $10 (환율이 2:1일 경우)** ← 완료!
- [x] $5 + $5 = $10
- [x] $5 + $5가 Sum을 반환
- [x] Bank.reduce(Sum)
- [x] Money.reduce (같은 통화)
- [x] Reduce Money with conversion
- [x] Reduce(Bank, String)
- [] **Sum.plus**
- [] **Expression.times**

## 핵심 변경사항

### 1. Expression 인터페이스 확장

```python
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        pass
```

### 2. Money - Expression 반환

```python
def times(self, multiplier: int) -> Expression:
    return Money(self._amount * multiplier, self._currency)

def plus(self, addend: Expression) -> Expression:
    return Sum(self, addend)
```

### 3. Sum - plus()와 times() 구현

```python
def plus(self, addend: Expression) -> Expression:
    """Sum + Expression = 새로운 Sum"""
    return Sum(self, addend)

def times(self, multiplier: int) -> Expression:
    """Sum의 각 피연산자에 배수 적용"""
    return Sum(self.augend.times(multiplier), self.addend.times(multiplier))
```

### 4. Sum의 augend/addend - Expression 타입

```python
def __init__(self, augend: Expression, addend: Expression) -> None:
    self.augend = augend
    self.addend = addend
```

## 테스트

```bash
python -m pytest part01/ch15/ -v
```

## 새 테스트 케이스

```python
def test_sum_plus_money(self):
    """($5 + 10 CHF) + $5 = $15"""

def test_sum_times(self):
    """($5 + 10 CHF) * 2 = $20"""
```

## 배운 점

- **Expression 일반화** - Money와 Sum 모두 동일한 인터페이스
- **Composite 패턴** - Sum이 Expression을 포함, 재귀적 구조
- **다형성의 힘** - reduce(), plus(), times() 모두 다형적 호출

## Part 1 완료!

Chapter 1에서 시작한 "$5 + 10 CHF = $10" 테스트가 완전히 통과!
Sum.plus, Expression.times까지 모두 구현 완료.
