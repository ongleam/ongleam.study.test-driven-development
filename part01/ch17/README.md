# Chapter 17: Money Retrospective

## 목표

- Part 1 회고 및 정리
- 학습한 내용 종합
- TDD 여정 되돌아보기

## 여정 요약

### Chapter 1-4: 기초 (Basic Building Blocks)

- **Ch1**: 곱셈 기능 (최소 구현)
- **Ch2**: 불변 객체 (Immutability)
- **Ch3**: 동등성 비교 (`__eq__`)
- **Ch4**: 캡슐화 (Private fields)

### Chapter 5-8: 중복 제거 (Eliminating Duplication)

- **Ch5**: Franc 클래스 추가 (중복 발생)
- **Ch6**: 교차 비교 테스트
- **Ch7**: 타입 비교 개선 (`type()`)
- **Ch8**: Money 부모 클래스, 팩토리 패턴

### Chapter 9-11: 통화 개념 (Currency Abstraction)

- **Ch9**: 통화 필드 추가 (USD, CHF)
- **Ch10**: times()를 Money로 이동
- **Ch11**: Dollar/Franc 제거, 통화만으로 구분

### Chapter 12-15: Expression 패턴 (Expression & Addition)

- **Ch12**: 덧셈, Expression, Sum, Bank
- **Ch13**: 다형성 기반 reduce
- **Ch14**: 환율 변환
- **Ch15**: 다중 통화 연산

### Chapter 16-17: 완성 (Finalization)

- **Ch16**: 추상 클래스 (ABC)
- **Ch17**: 회고 및 정리

## 학습한 TDD 원칙

### 1. Red-Green-Refactor 사이클

```
Red → Green → Refactor → Red → ...
```

### 2. 작은 단계

- 한 번에 하나의 테스트만
- 최소한의 변경으로 통과
- 점진적 개선

### 3. 테스트가 설계를 주도

- 테스트가 API 설계
- 사용자 관점에서 시작
- 구현 세부사항 숨기기

### 4. 리팩토링의 안전성

- 테스트가 있어 대담한 리팩토링 가능
- Dollar/Franc 제거도 안전하게
- 지속적 개선

## 적용된 디자인 패턴

### 1. Value Object

- Money는 값 객체
- 불변성
- 동등성 비교

### 2. Factory Pattern

```python
def dollar(amount):
    return Money(amount, "USD")
```

### 3. Composite Pattern

- Expression 계층
- Sum이 Expression 포함

### 4. Visitor Pattern

- reduce()의 double dispatch
- 다형성 활용

### 5. Strategy Pattern

- Bank가 환율 전략 관리

## 최종 구조

```
Expression (ABC)
├── reduce(bank, to_currency)
├── plus(addend)
└── times(multiplier)

Money (Expression)
├── _amount: float
├── _currency: str
└── implements all Expression methods

Sum (Expression)
├── augend: Expression
├── addend: Expression
└── implements all Expression methods

Bank
├── _rates: dict
├── add_rate(from, to, rate)
├── rate(from, to)
└── reduce(source, to_currency)
```

## 달성한 기능

✅ **다중 통화 지원**

```python
dollar(5), franc(10)
```

✅ **곱셈**

```python
dollar(5).times(2) == dollar(10)
```

✅ **덧셈**

```python
dollar(5).plus(dollar(5)) == dollar(10)
```

✅ **환율 변환**

```python
bank.add_rate("CHF", "USD", 2)
bank.reduce(franc(2), "USD") == dollar(1)
```

✅ **다중 통화 연산**

```python
dollar(5).plus(franc(10)).times(2)
```

## 핵심 교훈

### 1. 중복은 설계의 적

- 중복을 발견하고 제거
- 추상화로 통합

### 2. 테스트는 문서

- 코드가 무엇을 하는지 명확히
- 예제로서의 테스트

### 3. 점진적 개선

- 완벽하지 않아도 시작
- 계속 개선

### 4. 리팩토링의 용기

- 테스트가 있으면 두렵지 않음
- 과감한 변경 가능

### 5. 간단함의 힘

- 최소한으로 시작
- 필요할 때 복잡성 추가

## TDD의 리듬

1. **작은 테스트 작성** (Red)
2. **빠르게 통과시키기** (Green)
3. **좋은 코드로 만들기** (Refactor)
4. **반복**

## 다음 단계

Part 2에서는 xUnit 테스트 프레임워크를 TDD로 구축합니다!
