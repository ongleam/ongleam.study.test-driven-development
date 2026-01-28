# Part 3: Patterns for Test-Driven Development

> "패턴은 문제 해결의 반복되는 형태를 포착한다." - Kent Beck

## 개요

TDD를 효과적으로 수행하기 위한 패턴들을 다룬다. Part 1과 Part 2에서 사용한 기법들을 체계적으로 정리한다.

## 챕터 구성

| Chapter | 제목                             | 내용                            | 핵심 패턴                                    |
| ------- | -------------------------------- | ------------------------------- | -------------------------------------------- |
| 25      | Test-Driven Development Patterns | TDD 기본 리듬과 핵심 개념       | Red-Green-Refactor                           |
| 26      | Red Bar Patterns                 | 테스트 작성 시점과 방법         | One Step Test, Starter Test, Learning Test   |
| 27      | Testing Patterns                 | 상세 테스트 기법                | Mock Object, Self Shunt, Log String          |
| 28      | Green Bar Patterns               | 테스트 통과 전략                | Fake It, Triangulate, Obvious Implementation |
| 29      | xUnit Patterns                   | xUnit 프레임워크 사용법         | Assertion, Fixture, Test Method              |
| 30      | Design Patterns                  | TDD와 함께 사용하는 디자인 패턴 | Value Object, Composite, Factory Method      |
| 31      | Refactoring                      | 리팩토링 기법                   | Extract Method, Move Method, Migrate Data    |
| 32      | Mastering TDD                    | TDD 마스터하기 (FAQ)            | Best Practices, 17개 Q&A                     |

## 핵심 패턴 카테고리

### Red Bar Patterns (ch26)

테스트를 언제, 어디서, 어떻게 작성할지

- **One Step Test**: 학습과 자신감을 높이는 테스트 선택
- **Starter Test**: 가장 간단한 형태로 시작
- **Explanation Test**: 테스트로 설명하고 이해시키기
- **Learning Test**: 외부 API 학습용 테스트
- **Regression Test**: 버그 재현 테스트 먼저 작성

### Testing Patterns (ch27)

더 상세한 테스트 작성 기법

- **Child Test**: 큰 테스트를 작은 테스트로 분리
- **Mock Object**: 비용이 큰 리소스를 가짜 객체로 대체
- **Self Shunt**: 테스트 케이스 자체를 mock으로 사용
- **Log String**: 문자열로 메시지 호출 순서 추적
- **Crash Test Dummy**: 예외만 던지는 객체로 에러 상황 테스트

### Green Bar Patterns (ch28)

테스트를 통과시키는 전략

- **Fake It**: 하드코딩 후 점진적 일반화
- **Triangulate**: 두 개 이상의 예제로 추상화
- **Obvious Implementation**: 명백하면 바로 구현
- **One to Many**: 단일 요소 → 컬렉션으로 확장

### xUnit Patterns (ch29)

xUnit 프레임워크 사용 패턴

- **Assertion**: Boolean 표현식으로 결과 검증
- **Fixture**: 여러 테스트가 공유하는 객체 (setUp)
- **External Fixture**: 외부 리소스 해제 (tearDown)
- **Test Method**: test로 시작하는 메서드
- **Exception Test**: 예외 발생 검증

### Design Patterns (ch30)

TDD에서 자주 등장하는 디자인 패턴들

- **Command**: 계산을 객체로 표현
- **Value Object**: 불변 값 객체
- **Null Object**: 객체 부재 표현
- **Template Method**: 순서 정의, 세부 구현 위임
- **Pluggable Selector**: 동적 메서드 호출
- **Factory Method**: 객체 생성 캡슐화
- **Imposter**: 기존 객체 사칭
- **Composite**: 개별/컬렉션 동일 취급
- **Collecting Parameter**: 결과 수집 객체 전달

### Refactoring (ch31)

리팩토링 기법

- **Reconcile Differences**: 비슷한 코드를 점진적으로 합침
- **Isolate Change**: 변경할 부분을 먼저 격리
- **Migrate Data**: 새 표현 추가 → 이전 → 삭제
- **Extract Method**: 긴 메서드를 의미 단위로 추출
- **Move Method**: 적절한 클래스로 메서드 이동
- **Method Object**: 복잡한 메서드를 별도 객체로 분리

## Part 1, 2와의 연결

| 패턴                 | Part 1 Money 예제             | Part 2 xUnit 예제        |
| -------------------- | ----------------------------- | ------------------------ |
| Value Object         | Money, Dollar, Franc          | -                        |
| Factory Method       | Money.dollar(), Money.franc() | -                        |
| Composite            | Expression (Money + Sum)      | TestSuite                |
| Template Method      | -                             | setUp → test → tearDown  |
| Pluggable Selector   | -                             | getattr(self, self.name) |
| Collecting Parameter | -                             | TestResult               |
| Log String           | -                             | WasRun.log               |
| Imposter             | Sum (Expression 구현)         | -                        |

## 학습 방법

1. **Part 1, 2 실습**: Money 예제와 xUnit 예제를 직접 구현
2. **패턴 참조**: 구현 중 사용한 기법들을 Part 3에서 확인
3. **FAQ 활용**: ch32의 질문/답변으로 이해 심화
4. **반복 연습**: 다른 프로젝트에 TDD 적용

## 테스트 실행

```bash
# ch30 디자인 패턴 테스트
cd part03/ch30 && python -m pytest test_patterns.py -v
```

## 핵심 교훈

> "Clean code that works." - Ron Jeffries

TDD의 목표는 **작동하는 깨끗한 코드**다.

```
Red → Green → Refactor → (반복)
```
