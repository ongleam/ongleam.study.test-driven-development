# Chapter 10: Interesting Times

> "Does it really matter whether we have a Franc or a Money? We could carefully reason about this given knowledge of the system. However, we have clean code and we have tests that give us confidence that the clean code works. Rather than apply minutes of suspect reasoning, we can just ask the computer by making the change and running the tests." - Kent Beck

📌 **패턴**: -

## 목표

- times() 메서드를 Money 클래스로 통합
- Money를 직접 인스턴스화 (concrete 클래스)
- type 비교를 currency 비교로 변경
- Dollar/Franc 서브클래스 제거 준비

## 이전 챕터와의 차이

| 항목          | Chapter 9                   | Chapter 10                          |
| ------------- | --------------------------- | ----------------------------------- |
| Money 클래스  | 추상 클래스 (ABC)           | Concrete 클래스                     |
| times() 위치  | 하위 클래스에 각각          | Money에 통합                        |
| times() 반환  | `Dollar`, `Franc`           | `Money`                             |
| `__eq__` 비교 | `type(self) == type(other)` | `self._currency == other._currency` |
| 팩토리 반환   | `Dollar(amount)`            | `Money(amount, "USD")`              |

## 핵심 학습 포인트

1. **"Does it really matter?"**: 구분이 필요 없다면 제거
2. **점진적 리팩토링**: 테스트가 통과하는 상태 유지
3. **type → currency**: 클래스 타입 대신 도메인 개념으로 구분

## TDD 사이클

### Red: 기존 테스트가 계속 통과해야 함

```python
def test_multiplication(self):
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
```

### Green: times()를 Money로 이동

Kent Beck의 질문: "Does it really matter whether we have a Franc or a Money?"

```python
# 기존 (Dollar 클래스)
def times(self, multiplier):
    return Dollar(self._amount * multiplier)

# 변경 후 (Dollar 클래스)
def times(self, multiplier):
    return Money(self._amount * multiplier, self._currency)
```

Dollar와 Franc의 times()가 동일해지면 Money로 이동:

```python
class Money:
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)
```

### Refactor: `__eq__`를 currency 기반으로 변경

```python
def __eq__(self, other):
    # type 비교 대신 currency 비교
    return self._amount == other._amount and self._currency == other._currency
```

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


# Dollar와 Franc은 이제 불필요 (호환성을 위해 유지)
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount, "CHF")
```

## 구현된 기능

- ✅ times() 메서드 Money로 통합
- ✅ Money 직접 인스턴스화 가능
- ✅ currency 기반 동등성 비교
- ✅ 팩토리 메서드가 Money 직접 반환

## 다음 챕터 예고

- ⚠️ Dollar, Franc 서브클래스가 비어있음 → 제거 가능
- ⚠️ Expression 인터페이스 필요 (덧셈 지원)

## 테스트 실행

```bash
python -m pytest part01/ch10/ -v
```
