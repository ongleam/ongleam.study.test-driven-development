# Chapter 8: Makin' Objects

## 목표

- Money 상위 클래스 도입
- 팩토리 함수로 객체 생성 추상화
- 중복 코드 제거 시작

## 이전 챕터와의 차이

- `Money` 부모 클래스 추가
- Dollar와 Franc이 Money 상속
- `dollar()`, `franc()` 팩토리 함수 추가
- `__eq__`와 `__hash__`를 Money로 이동

## Red-Green-Refactor 사이클

### 1. Red: 테스트 리팩토링

```python
def test_multiplication(self):
    five = dollar(5)  # 팩토리 함수 사용
    assert dollar(10) == five.times(2)
```

### 2. Green: 구현

```python
class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

def dollar(amount):
    return Dollar(amount)
```

### 3. Refactor

- 중복 코드를 부모 클래스로 이동
- 팩토리 함수로 생성 캡슐화

## 구현된 기능

- ✅ Money 추상 클래스
- ✅ Dollar와 Franc이 Money 상속
- ✅ 팩토리 함수 (dollar, franc)
- ✅ 공통 로직 통합 (**eq**, **hash**)

## 학습 포인트

1. **상속**: 공통 코드를 부모 클래스로
2. **팩토리 패턴**: 객체 생성 로직 캡슐화
3. **점진적 리팩토링**: 한 번에 하나씩 개선
4. **테스트 주도 리팩토링**: 테스트가 있어 안전하게 리팩토링

## 문제점 (다음 챕터에서 해결)

- times() 메서드가 여전히 중복
- 통화(currency) 개념 부재
