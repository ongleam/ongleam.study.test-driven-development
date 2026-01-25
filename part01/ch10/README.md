# Chapter 10: Interesting Times

## 목표

- times() 메서드를 Money 클래스로 이동
- 중복 제거

## 이전 챕터와의 차이

- Money 클래스에 `times()` 메서드 추가
- Dollar와 Franc의 times() 제거
- 통화 기반으로 올바른 타입 반환

## Red-Green-Refactor 사이클

### 1. Red: 기존 테스트 유지

- 모든 테스트가 여전히 통과해야 함

### 2. Green: 구현

```python
class Money:
    def times(self, multiplier):
        if self._currency == "USD":
            return dollar(self._amount * multiplier)
        elif self._currency == "CHF":
            return franc(self._amount * multiplier)

class Dollar(Money):
    # times() 메서드 제거됨
    pass
```

### 3. Refactor

- 서브클래스의 중복 메서드 제거
- 부모 클래스에서 통합 처리

## 구현된 기능

- ✅ Money 클래스의 times() 메서드
- ✅ 통화 기반 객체 생성
- ✅ Dollar와 Franc의 간소화

## 학습 포인트

1. **중복 제거**: 동일한 로직을 부모로
2. **조건부 로직**: 통화에 따라 분기
3. **팩토리 활용**: 올바른 타입 생성

## 문제점 (다음 챕터에서 해결)

- if-elif 조건문이 좋지 않음
- Dollar와 Franc 서브클래스가 거의 비어있음
- 통화만으로 구분 가능
