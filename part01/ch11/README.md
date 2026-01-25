# Chapter 11: The Root of All Evil

> "The root of all evil" - Donald Knuth의 "premature optimization is the root of all evil"에서 영감

📌 **패턴**: -

## 목표

- Dollar와 Franc 서브클래스 완전 제거
- Money 클래스만으로 모든 기능 구현
- "The root of all evil" = 불필요한 중복/복잡성

## 이전 챕터와의 차이

| 항목        | Chapter 10             | Chapter 11 |
| ----------- | ---------------------- | ---------- |
| 클래스 구조 | Money + Dollar + Franc | Money만    |
| 서브클래스  | 빈 껍데기로 존재       | 완전 제거  |
| 코드 복잡도 | 3개 클래스             | 1개 클래스 |

## 핵심 학습 포인트

1. **"The Root of All Evil"**: 불필요한 중복과 복잡성이 악의 근원
2. **데이터 주도 설계**: 타입 계층 대신 데이터(currency)로 구분
3. **단순화의 힘**: 3개 클래스 → 1개 클래스
4. **안전한 리팩토링**: 테스트 덕분에 대담한 삭제 가능

## TDD 사이클

### Red: 기존 테스트 유지

서브클래스 제거 후에도 모든 테스트가 통과해야 함:

```python
def test_multiplication(self):
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
```

### Green: 서브클래스 제거

Dollar와 Franc 클래스를 완전히 삭제:

```python
# 제거됨:
# class Dollar(Money): ...
# class Franc(Money): ...

# Money만 남음
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
```

### Refactor: 개선

- 불필요한 상속 계층 제거
- 코드 단순화 완료

## 전체 코드

```python
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def __eq__(self, other):
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
```

## 구현된 기능

- ✅ Dollar, Franc 서브클래스 완전 제거
- ✅ Money 클래스만으로 모든 기능 구현
- ✅ 팩토리 메서드로 통화별 생성
- ✅ currency 기반 동등성 비교

## 코드 진화 요약 (ch01 → ch11)

```
ch01-04: Dollar 클래스만
ch05:    Dollar + Franc (별도 클래스)
ch06:    Money 상위 클래스 도입
ch07:    type() 비교 추가
ch08:    Money 추상 클래스 + 팩토리 메서드
ch09:    currency 개념 추가
ch10:    times() Money로 통합, currency 비교
ch11:    Dollar/Franc 서브클래스 제거 → Money만!
```

## 다음 챕터 예고

- ⚠️ 아직 덧셈 기능 없음 (`$5 + $5 = $10`)
- ⚠️ 다중 통화 계산 필요 (`$5 + 10 CHF`)
- ⚠️ Expression 인터페이스 도입 예정

## 테스트 실행

```bash
python -m pytest part01/ch11/ -v
```
