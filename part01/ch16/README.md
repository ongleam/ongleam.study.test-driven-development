# Chapter 16: Abstraction, Finally

## 핵심 개념

**Part 1 완성 - 모든 TODO 항목 완료**

> "We have finished with the first example. Let's look back and review
> what we've done." - Kent Beck

## TODO 리스트 (모두 완료!)

- [x] $5 + 10 CHF = $10 (환율이 2:1일 경우)
- [x] $5 + $5 = $10
- [x] $5 + $5가 Sum을 반환
- [x] Bank.reduce(Sum)
- [x] Money.reduce (같은 통화)
- [x] Reduce Money with conversion
- [x] Reduce(Bank, String)
- [x] **Sum.plus**
- [x] **Expression.times**

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

## 테스트

```bash
python -m pytest part01/ch16/ -v
```

## Part 1 회고 (Kent Beck)

### 테스트 작성 과정에서 배운 것

1. **작은 단계** - 한 번에 하나의 테스트
2. **빠른 피드백** - 테스트가 빨리 실행되어야 함
3. **설계의 진화** - 테스트가 설계를 이끈다

### 사용된 TDD 패턴

| 패턴                   | 설명                     | 사용된 챕터 |
| ---------------------- | ------------------------ | ----------- |
| Fake It                | 하드코딩으로 빠르게 통과 | Ch12        |
| Triangulation          | 두 번째 테스트로 일반화  | Ch13        |
| Obvious Implementation | 명확하면 바로 구현       | 전체        |

### 리팩토링 기법

- **팩토리 메서드** - Dollar, Franc 서브클래스 제거
- **다형성** - Expression 인터페이스로 통일
- **Composite 패턴** - Sum이 Expression 포함

## 코드 라인 수

```
Production code: ~80 lines
Test code: ~90 lines
Ratio: 약 1:1
```

## 다음 단계

Part 2: xUnit Example - 테스트 프레임워크 직접 구현
