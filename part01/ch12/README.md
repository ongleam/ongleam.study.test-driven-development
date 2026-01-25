# Chapter 12: Addition, Finally

## 목표

- 덧셈 기능 구현
- Expression 인터페이스 도입
- Bank와 reduce 개념 도입

## 이전 챕터와의 차이

- `Expression` 추상 클래스 추가
- `Sum` 클래스 추가 (두 Expression의 합)
- `Bank` 클래스 추가 (reduce 기능)
- `Money.plus()` 메서드 추가

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_simple_addition(self):
    five = dollar(5)
    sum_result = five.plus(dollar(5))
    bank = Bank()
    reduced = bank.reduce(sum_result, "USD")
    assert dollar(10) == reduced
```

### 2. Green: 구현

```python
class Expression:
    pass

class Money(Expression):
    def plus(self, addend):
        return Sum(self, addend)

class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

class Bank:
    def reduce(self, source, to_currency):
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)
        return source
```

### 3. Refactor

- Expression 계층 구조 정립
- Bank를 통한 변환

## 구현된 기능

- ✅ Money 덧셈 (plus)
- ✅ Expression 인터페이스
- ✅ Sum 클래스 (지연 평가)
- ✅ Bank.reduce() (Expression을 Money로 변환)

## 학습 포인트

1. **Expression 패턴**: 계산을 객체로 표현
2. **지연 평가**: plus()는 즉시 계산하지 않고 Sum 반환
3. **Bank의 역할**: 환율 변환 책임
4. **Reduce**: Expression을 단일 통화 Money로 변환

## 문제점 (다음 챕터에서 해결)

- reduce가 같은 통화만 처리
- 환율 변환 미지원
- Sum이 다른 통화 처리 못함
