# Chapter 16: Abstraction, Finally

> "We have finished with the first example. Let's look back and review what we've done." - Kent Beck

📌 **주제**: 회고, 구조 정리, Part 1 완성

## 핵심 개념

Part 1 완성 - 모든 TODO 항목 완료

Chapter 1에서 시작한 "$5 + 10 CHF = $10" 목표가 완전히 달성되었습니다.

## 회고 주제

### 1. TODO 리스트 (모두 완료!)

- [x] $5 + 10 CHF = $10 (환율이 2:1일 경우)
- [x] $5 + $5 = $10
- [x] $5 + $5가 Sum을 반환
- [x] Bank.reduce(Sum)
- [x] Money.reduce (같은 통화)
- [x] Reduce Money with conversion
- [x] Reduce(Bank, String)
- [x] Sum.plus
- [x] Expression.times

### 2. 사용된 TDD 패턴

| 패턴                   | 설명                     | 사용된 챕터 |
| ---------------------- | ------------------------ | ----------- |
| Fake It                | 하드코딩으로 빠르게 통과 | Ch12        |
| Triangulation          | 두 번째 테스트로 일반화  | Ch13        |
| Obvious Implementation | 명확하면 바로 구현       | 전체        |

### 3. 리팩토링 기법

- **팩토리 메서드** - Dollar, Franc 서브클래스 제거
- **다형성** - Expression 인터페이스로 통일
- **Composite 패턴** - Sum이 Expression 포함

## 최종 클래스 구조

```
Expression (ABC)
├── reduce(bank, to_currency) -> Money
├── plus(addend) -> Expression
└── times(multiplier) -> Expression

Money(Expression)
├── _amount: int
├── _currency: str
├── times() -> Expression
├── plus() -> Expression
├── reduce() -> Money
└── dollar(), franc() (팩토리)

Sum(Expression)
├── augend: Expression
├── addend: Expression
├── reduce() -> Money
├── plus() -> Expression
└── times() -> Expression

Bank
├── _rates: dict[Pair, int]
├── reduce(source, to_currency) -> Money
├── add_rate(from, to, rate)
└── rate(from, to) -> int

Pair
├── _from: str
├── _to: str
└── __eq__, __hash__
```

## 코드 메트릭스

| 항목          | 값     |
| ------------- | ------ |
| 프로덕션 라인 | ~80    |
| 테스트 라인   | ~90    |
| 비율          | 약 1:1 |

## 핵심 교훈

1. **테스트 작성 과정에서 배운 것**
   - 작은 단계 - 한 번에 하나의 테스트
   - 빠른 피드백 - 테스트가 빨리 실행되어야 함
   - 설계의 진화 - 테스트가 설계를 이끈다

2. **TDD의 핵심**
   - Red → Green → Refactor 사이클
   - 신뢰할 수 있는 테스트가 대담한 리팩토링을 가능하게 함

## 다음 단계

Part 2: xUnit Example - 테스트 프레임워크 직접 구현

## 테스트 실행

```bash
python -m pytest part01/ch16/ -v
```
