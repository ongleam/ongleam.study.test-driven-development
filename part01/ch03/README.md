# Chapter 3: Equality for All

## 목표

- Dollar 객체 간 동등성 비교 구현
- `==` 연산자를 사용한 값 비교 가능하게 만들기

## 이전 챕터와의 차이

- `__eq__()` 메서드 추가로 동등성 비교 지원
- `__hash__()` 메서드 추가 (해시 가능 객체로 만들기)
- amount 대신 객체 자체를 비교 가능

## Red-Green-Refactor 사이클

### 1. Red: 실패하는 테스트 작성

```python
def test_equality(self):
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
```

### 2. Green: 구현

```python
def __eq__(self, other):
    if not isinstance(other, Dollar):
        return False
    return self._amount == other._amount

def __hash__(self):
    return hash(self._amount)
```

### 3. Refactor

- isinstance()로 타입 체크
- amount 대신 \_amount 직접 비교

## 구현된 기능

- ✅ `==` 연산자로 Dollar 객체 비교
- ✅ `!=` 연산자로 불일치 확인
- ✅ 해시 가능한 객체 (집합, 딕셔너리 키로 사용 가능)

## 학습 포인트

1. **값 객체(Value Object)**: 동등성이 속성값으로 결정됨
2. ****eq** 구현**: Python의 동등성 비교 커스터마이징
3. ****hash** 구현**: **eq**를 오버라이드하면 **hash**도 구현해야 함
4. **isinstance() 사용**: 타입 체크의 올바른 방법

## 문제점 (다음 챕터에서 해결)

- 테스트가 여전히 amount에 직접 접근
- 동등성 비교를 활용하여 테스트 개선 필요
