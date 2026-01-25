# Chapter 15: Mixed Currencies

## 목표

- 다중 통화 덧셈 지원
- Sum에 plus(), times() 메서드 추가
- 복잡한 Expression 계산

## 이전 챕터와의 차이

- `Expression`에 `plus()`, `times()` 메서드 추가
- `Sum.plus()` 구현 (Sum + Expression)
- `Sum.times()` 구현 (Sum \* multiplier)
- 다중 통화 연산 지원

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_mixed_addition(self):
    five_bucks = dollar(5)
    ten_francs = franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert dollar(10) == result
```

### 2. Green: 구현

```python
class Expression:
    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        pass

class Sum(Expression):
    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier),
                   self.addend.times(multiplier))
```

### 3. Refactor

- Expression 인터페이스 확장
- Sum의 재귀적 연산

## 구현된 기능

- ✅ 다중 통화 덧셈
- ✅ Sum.plus() (연쇄 덧셈)
- ✅ Sum.times() (분배 법칙)
- ✅ 복잡한 Expression 트리

## 학습 포인트

1. **Composite 패턴**: Sum이 Expression을 포함
2. **재귀적 구조**: Sum 안에 Sum 가능
3. **분배 법칙**: (a+b)*n = a*n + b\*n
4. **지연 평가**: reduce 시점까지 계산 미루기

## 문제점 (다음 챕터에서 해결)

- Expression 인터페이스가 완전하지 않음
- 일부 메서드가 구현 누락
