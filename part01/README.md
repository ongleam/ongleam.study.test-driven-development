# Part 1: The Money Example

Kent Beck의 『Test-Driven Development: By Example』 Part 1 실습

> "Clean code that works." - Kent Beck

## 학습 로드맵

| Ch  | 제목                    | 핵심 패턴                   | 학습 목표                        |
| --- | ----------------------- | --------------------------- | -------------------------------- |
| 01  | Multi-Currency Money    | -                           | TDD 기본 사이클 시작             |
| 02  | Degenerate Objects      | Value Object                | Side effect 제거                 |
| 03  | Equality for All        | Triangulation               | 동등성 비교 구현                 |
| 04  | Privacy                 | Encapsulation               | 캡슐화, 블랙박스 테스트          |
| 05  | Franc-ly Speaking       | -                           | 새로운 통화 추가 (코드 복사)     |
| 06  | Equality for All, Redux | Pull Up Method              | 상속을 통한 중복 제거            |
| 07  | Apples and Oranges      | -                           | 서로 다른 통화 구분              |
| 08  | Makin' Objects          | Factory Method              | 추상 클래스 + 팩토리 메서드      |
| 09  | Times We're Livin' In   | -                           | 통화(currency) 개념 도입         |
| 10  | Interesting Times       | -                           | times() 통합, currency 기반 비교 |
| 11  | The Root of All Evil    | -                           | 서브클래스 완전 제거             |
| 12  | Addition, Finally       | Fake It                     | 덧셈 시작, Expression/Sum 도입   |
| 13  | Make It                 | Triangulation, Polymorphism | Fake → 실제 구현                 |
| 14  | Change                  | -                           | 환율 변환 기능                   |
| 15  | Mixed Currencies        | Composite                   | 다중 통화 덧셈 완성              |
| 16  | Abstraction, Finally    | -                           | Part 1 완성, 구조 정리           |
| 17  | Money Retrospective     | -                           | 회고, 메트릭스, 프로세스 분석    |

## 전체 진행 흐름

```
Ch01-04: 단일 Dollar 클래스
         └─ TDD 기본 사이클, Value Object, 동등성

Ch05-11: 다중 통화 + 상속 구조
         └─ Dollar + Franc → Money 상속 → 서브클래스 제거

Ch12-15: Expression 계층 구조
         └─ 덧셈, 환율 변환, 다중 통화 계산

Ch16-17: 회고
         └─ 메트릭스, 프로세스 분석, 교훈 정리
```

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
```

## 코드 메트릭스

| 항목          | 값     |
| ------------- | ------ |
| 프로덕션 라인 | ~80    |
| 테스트 라인   | ~90    |
| 비율          | 약 1:1 |
| 테스트 실행   | ~125회 |

## 테스트 실행

```bash
# Part 1 전체 테스트
python -m pytest part01/ -v

# 특정 챕터 테스트
python -m pytest part01/ch01/ -v
python -m pytest part01/ch15/ -v
```

## 챕터별 바로가기

- [Chapter 01: Multi-Currency Money](./ch01/README.md)
- [Chapter 02: Degenerate Objects](./ch02/README.md)
- [Chapter 03: Equality for All](./ch03/README.md)
- [Chapter 04: Privacy](./ch04/README.md)
- [Chapter 05: Franc-ly Speaking](./ch05/README.md)
- [Chapter 06: Equality for All, Redux](./ch06/README.md)
- [Chapter 07: Apples and Oranges](./ch07/README.md)
- [Chapter 08: Makin' Objects](./ch08/README.md)
- [Chapter 09: Times We're Livin' In](./ch09/README.md)
- [Chapter 10: Interesting Times](./ch10/README.md)
- [Chapter 11: The Root of All Evil](./ch11/README.md)
- [Chapter 12: Addition, Finally](./ch12/README.md)
- [Chapter 13: Make It](./ch13/README.md)
- [Chapter 14: Change](./ch14/README.md)
- [Chapter 15: Mixed Currencies](./ch15/README.md)
- [Chapter 16: Abstraction, Finally](./ch16/README.md)
- [Chapter 17: Money Retrospective](./ch17/README.md)
