# Chapter 4: Privacy

> "Making tests that don't need to know much about the implementation is one of the keys to keeping your tests robust." - Kent Beck

📌 **패턴**: Encapsulation

## 목표

- amount를 완전히 private으로 만들기
- 테스트에서 구현 세부사항 대신 동작을 테스트

## 이전 챕터와의 차이

| 항목          | Chapter 3              | Chapter 4               |
| ------------- | ---------------------- | ----------------------- |
| amount 접근   | Public (직접 접근)     | Private (\_amount)      |
| 테스트 비교   | `product.amount == 10` | `product == Dollar(10)` |
| 테스트 스타일 | 구현 세부사항          | 동작 기반               |

## 핵심 학습 포인트

1. **캡슐화**: 내부 구현을 숨기고 공개 인터페이스만 노출
2. **블랙박스 테스트**: 구현이 아닌 동작을 테스트
3. **테스트 개선**: 동등성을 활용하여 테스트 코드 간소화

## TDD 사이클

### Red: 테스트 리팩토링

```python
def test_multiplication(self):
    five = Dollar(5)
    # amount 대신 객체 비교
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)
```

### Green: 최소 구현

```python
# @property 제거 - amount는 완전히 private
class Dollar:
    def __init__(self, amount):
        self._amount = amount

    # amount property 제거됨
```

### Refactor: 개선

- 테스트가 더 간결해짐
- 구현 세부사항이 아닌 동작을 테스트

## 전체 코드

```python
class Dollar:
    def __init__(self, amount):
        self._amount = amount

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

- ✅ 완전히 캡슐화된 Dollar 클래스
- ✅ 테스트가 공개 인터페이스만 사용
- ✅ 동작 기반 테스트

## 다음 챕터 예고

- ⚠️ 다른 통화(Franc) 지원 필요
- ⚠️ Dollar만으로는 실제 Money 시스템 부족

## 테스트 실행

```bash
python -m pytest part01/ch04/ -v
```
