# Chapter 13: Make It

## 목표

- Expression에 reduce() 메서드 추가
- 다형성을 활용한 reduce 구현

## 이전 챕터와의 차이

- `Expression.reduce()` 추상 메서드 정의
- `Money.reduce()` 구현 (자기 자신 반환)
- `Sum.reduce()` 구현 (각 항을 reduce 후 합산)
- `Bank.reduce()`가 Expression의 reduce 호출

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_reduce_money(self):
    bank = Bank()
    result = bank.reduce(dollar(1), "USD")
    assert dollar(1) == result
```

### 2. Green: 구현

```python
class Expression:
    def reduce(self, bank, to_currency):
        pass

class Money(Expression):
    def reduce(self, bank, to_currency):
        return self

class Sum(Expression):
    def reduce(self, bank, to_currency):
        amount = (self.augend.reduce(bank, to_currency)._amount +
                  self.addend.reduce(bank, to_currency)._amount)
        return Money(amount, to_currency)

class Bank:
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)
```

### 3. Refactor

- isinstance() 체크 제거
- 다형성 활용
- 재귀적 reduce

## 구현된 기능

- ✅ Expression.reduce() 인터페이스
- ✅ Money.reduce() 구현
- ✅ Sum.reduce() 구현
- ✅ 다형성 기반 설계

## 학습 포인트

1. **다형성**: 각 클래스가 자신의 reduce 구현
2. **재귀**: Sum.reduce()가 augend, addend의 reduce 호출
3. **캡슐화**: Bank가 타입 체크 안 함
4. **Visitor 패턴**: reduce가 double dispatch 수행

## 문제점 (다음 챕터에서 해결)

- 환율 변환 미지원
- 다른 통화 간 덧셈 불가
