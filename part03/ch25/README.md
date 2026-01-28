# Chapter 25: Test-Driven Development Patterns

> "테스트 주도 개발의 리듬: 빨강-초록-리팩토링" - Kent Beck

📌 **Part 3: Patterns for Test-Driven Development**

## 개요

Part 3의 시작 챕터. TDD의 핵심 패턴들을 소개한다.

## TDD 기본 리듬

1. **Red**: 실패하는 작은 테스트를 작성
2. **Green**: 테스트를 통과하는 최소한의 코드 작성
3. **Refactor**: 중복 제거 및 코드 개선

## 핵심 질문들

### 테스트는 언제 작성하는가?

- **테스트 먼저 (Test First)**: 코드 작성 전에 테스트 작성
- 테스트는 설계 도구이자 문서

### 테스트는 어디서 작성하는가?

- 프로덕션 코드와 분리
- 테스트 코드도 프로덕션 코드만큼 중요

### 언제 테스트를 작성하지 않는가?

- 외부 라이브러리/프레임워크 테스트는 필요 시에만
- 단, 이해가 필요한 경우 Learning Test 작성

## Part 3 패턴 카테고리

### Red Bar Patterns (Chapter 26)

테스트를 언제, 어디서, 어떻게 작성할지 결정

- One Step Test
- Starter Test
- Explanation Test
- Learning Test
- Another Test
- Regression Test
- Break
- Do Over
- Cheap Desk, Nice Chair

### Testing Patterns (Chapter 27)

더 상세한 테스트 작성 기법

- Child Test
- Mock Object
- Self Shunt
- Log String
- Crash Test Dummy
- Broken Test
- Clean Check-in

### Green Bar Patterns (Chapter 28)

테스트를 통과시키는 전략

- Fake It ('Til You Make It)
- Triangulate
- Obvious Implementation
- One to Many

### xUnit Patterns (Chapter 29)

xUnit 프레임워크 사용 패턴

- Assertion
- Fixture
- External Fixture
- Test Method
- Exception Test
- All Tests

### Design Patterns (Chapter 30)

TDD와 함께 사용되는 디자인 패턴

- Command
- Value Object
- Null Object
- Template Method
- Pluggable Object
- Pluggable Selector
- Factory Method
- Imposter
- Composite
- Collecting Parameter
- Singleton

### Refactoring (Chapter 31-32)

리팩토링 기법

- Reconcile Differences
- Isolate Change
- Migrate Data
- Extract Method
- Inline Method
- Extract Interface
- Move Method
- Method Object
- Add Parameter
- Method Parameter to Constructor Parameter

## 이 챕터의 핵심

> "Clean code that works" - Ron Jeffries

TDD의 목표는 **작동하는 깨끗한 코드**를 만드는 것이다.

## 다음 챕터 예고

- Chapter 26: Red Bar Patterns
- 테스트를 언제, 어떻게 작성할지에 대한 패턴들
