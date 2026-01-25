# Chapter 4: Privacy

## 목표

- amount를 완전히 private으로 만들기
- 테스트에서 구현 세부사항 대신 동작을 테스트

## 이전 챕터와의 차이

- `@property` 데코레이터 제거 (amount에 대한 public 접근 제거)
- 테스트가 amount 대신 동등성 비교 사용
- test_multiplication 간소화

## Red-Green-Refactor 사이클

### 1. Red: 테스트 리팩토링

```python
def test_multiplication(self):
    five = Dollar(5)
    # amount 대신 객체 비교
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)
```

### 2. Green: 구현

```python
# @property 제거 - amount는 완전히 private
class Dollar:
    def __init__(self, amount):
        self._amount = amount

    # amount property 제거됨
```

### 3. Refactor

- 테스트가 더 간결해짐
- 구현 세부사항이 아닌 동작을 테스트

## 구현된 기능

- ✅ 완전히 캡슐화된 Dollar 클래스
- ✅ 테스트가 공개 인터페이스만 사용
- ✅ 동작 기반 테스트

## 학습 포인트

1. **캡슐화**: 내부 구현을 숨기고 공개 인터페이스만 노출
2. **블랙박스 테스트**: 구현이 아닌 동작을 테스트
3. **테스트 개선**: 동등성을 활용하여 테스트 코드 간소화

## 문제점 (다음 챕터에서 해결)

- 다른 통화(Franc) 지원 필요
- Dollar만으로는 실제 Money 시스템 부족
