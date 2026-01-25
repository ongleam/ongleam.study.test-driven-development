# Chapter 5: Franc-ly Speaking

## 목표

- 스위스 프랑(Franc) 지원 추가
- Dollar와 동일한 기능을 가진 새로운 통화 클래스

## 이전 챕터와의 차이

- `Franc` 클래스 추가 (Dollar와 거의 동일한 코드)
- Franc에 대한 테스트 추가
- 명백한 코드 중복 발생

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_franc_multiplication(self):
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
```

### 2. Green: 최소 구현 (복사-붙여넣기)

```python
class Franc:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Franc):
            return False
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)
```

### 3. Refactor

- 이 단계에서는 리팩토링하지 않음
- 중복을 인식하지만 다음 챕터에서 해결

## 구현된 기능

- ✅ Franc 클래스 (Dollar와 동일한 구조)
- ✅ Franc 곱셈
- ✅ Franc 동등성 비교

## 학습 포인트

1. **중복 허용**: TDD에서는 일단 동작하게 만든 후 리팩토링
2. **작은 단계**: 한 번에 하나의 테스트만 통과시킴
3. **명백한 구현**: 복잡하지 않으면 바로 구현
4. **기술 부채 인식**: 중복을 알지만 나중에 해결

## 문제점 (다음 챕터에서 해결)

- Dollar와 Franc의 코드 중복
- 두 클래스가 거의 동일
- 공통 상위 클래스 필요
