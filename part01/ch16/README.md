# Chapter 16: Abstraction, Finally

## 목표

- Expression을 완전한 추상 클래스로 정의
- 클래스 계층 구조 정리
- 최종 리팩토링

## 이전 챕터와의 차이

- `Expression`을 `ABC` (Abstract Base Class)로 변경
- `@abstractmethod` 데코레이터 추가
- `Money.__repr__()` 추가 (디버깅 용이)
- 모든 인터페이스 명시적 정의

## Red-Green-Refactor 사이클

### 1. Red: 기존 테스트 유지

- 모든 테스트가 여전히 통과해야 함

### 2. Green: 구현

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to_currency):
        pass

    @abstractmethod
    def plus(self, addend):
        pass

    @abstractmethod
    def times(self, multiplier):
        pass
```

### 3. Refactor

- ABC 사용으로 인터페이스 강제
- 명시적 추상 메서드
- 코드 가독성 향상

## 구현된 기능

- ✅ 완전한 Expression 추상 클래스
- ✅ 추상 메서드 명시
- ✅ Money와 Sum의 완전한 구현
- ✅ 깔끔한 클래스 계층

## 학습 포인트

1. **ABC (Abstract Base Class)**: Python의 추상 클래스
2. **@abstractmethod**: 추상 메서드 강제
3. **인터페이스 설계**: 명시적 계약
4. **다형성**: Expression 인터페이스로 통일
5. **완성도**: 모든 코드가 깔끔하게 정리됨

## 최종 구조

```
Expression (ABC)
├── Money
│   ├── times()
│   ├── plus()
│   └── reduce()
└── Sum
    ├── times()
    ├── plus()
    └── reduce()

Bank
├── add_rate()
├── rate()
└── reduce()
```

## 달성한 목표

- ✅ 다중 통화 지원
- ✅ 통화 간 변환
- ✅ 덧셈과 곱셈
- ✅ Expression 기반 계산
- ✅ 깔끔한 코드
