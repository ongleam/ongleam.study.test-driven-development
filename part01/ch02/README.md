# Chapter 2: Degenerate Objects

## 목표

- Dollar 객체를 불변(immutable) 객체로 만들기
- 부작용(side-effect) 없는 times() 메서드 구현

## 이전 챕터와의 차이

- `amount`를 `_amount`로 변경하여 private 변수화
- `@property` 데코레이터를 사용하여 읽기 전용 접근 제공
- `times()` 메서드가 기존 객체를 수정하지 않고 새 객체를 반환

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_immutability(self):
    five = Dollar(5)
    five.times(2)
    # five는 변경되지 않아야 함
    assert 5 == five.amount
```

### 2. Green: 구현

```python
class Dollar:
    def __init__(self, amount):
        self._amount = amount  # private 변수

    @property
    def amount(self):
        return self._amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)  # 새 객체 반환
```

### 3. Refactor

- `_amount`를 private으로 변경
- property를 통한 읽기 전용 접근

## 구현된 기능

- ✅ Dollar 객체의 불변성
- ✅ times() 메서드가 새로운 Dollar 객체 반환
- ✅ amount는 읽기 전용 프로퍼티

## 학습 포인트

1. **불변 객체**: 객체가 생성된 후 상태가 변경되지 않음
2. **부작용 제거**: 메서드 호출이 객체의 상태를 변경하지 않음
3. **캡슐화**: private 변수와 property 사용

## 문제점 (다음 챕터에서 해결)

- 아직 동등성 비교(`==`)가 불가능
- amount로 직접 비교해야 함
