# Chapter 6: Equality for All, Redux

## 목표

- Dollar와 Franc 간의 비교 테스트
- 서로 다른 클래스는 같지 않음을 확인

## 이전 챕터와의 차이

- `Dollar(5) != Franc(5)` 테스트 추가
- 기존 `isinstance()` 체크가 이미 이 동작을 보장함

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_equality(self):
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    assert Dollar(5) != Franc(5)  # 새로운 테스트
```

### 2. Green: 구현

- 이미 구현되어 있음 (isinstance() 체크가 타입을 구분)
- 테스트는 바로 통과

### 3. Refactor

- 리팩토링 없음 (다음 챕터를 위한 준비)

## 구현된 기능

- ✅ Dollar와 Franc은 같은 금액이어도 다름
- ✅ isinstance()로 타입 체크

## 학습 포인트

1. **테스트의 가치**: 이미 동작하는 것도 테스트로 명시적으로 확인
2. **타입 안전성**: isinstance()가 다른 타입을 구분
3. **문서로서의 테스트**: 코드의 의도를 명확하게 표현

## 문제점 (다음 챕터에서 해결)

- 여전히 Dollar와 Franc의 코드 중복
- 동등성 비교 로직도 중복
