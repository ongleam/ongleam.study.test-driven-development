# Chapter 7: Apples and Oranges

## 목표

- 동등성 비교를 더 명확하게 개선
- type() 사용으로 타입 비교 단순화

## 이전 챕터와의 차이

- `isinstance()` 대신 `type()` 사용
- 더 간결한 동등성 비교 로직
- **hash**에 타입 정보 포함

## Red-Green-Refactor 사이클

### 1. Red: 기존 테스트 유지

- 기존 테스트가 모두 통과해야 함

### 2. Green: 구현 개선

```python
def __eq__(self, other):
    # isinstance() 대신 type() 사용
    return self._amount == other._amount and type(self) == type(other)

def __hash__(self):
    return hash((self._amount, type(self)))
```

### 3. Refactor

- isinstance() 체크 제거
- 더 간결한 표현식

## 구현된 기능

- ✅ type()을 사용한 정확한 타입 비교
- ✅ 간결해진 동등성 로직
- ✅ 타입을 포함한 해시값

## 학습 포인트

1. **type() vs isinstance()**: 정확한 타입 비교 vs 상속 고려
2. **코드 단순화**: 조건문을 표현식으로 변경
3. **해시 함수**: 동등성 비교에 사용되는 모든 필드 포함

## 문제점 (다음 챕터에서 해결)

- 여전히 Dollar와 Franc의 중복 코드
- 공통 부모 클래스 필요
