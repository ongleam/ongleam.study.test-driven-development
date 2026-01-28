# Part 3: Patterns for Test-Driven Development

> "패턴은 문제 해결의 반복되는 형태를 포착한다." - Kent Beck

## 개요

TDD를 효과적으로 수행하기 위한 패턴들을 다룬다. Part 1과 Part 2에서 사용한 기법들을 체계적으로 정리한다.

## 챕터 구성

| Chapter | 제목                             | 내용                            |
| ------- | -------------------------------- | ------------------------------- |
| 25      | Test-Driven Development Patterns | TDD 기본 리듬과 핵심 개념       |
| 26      | Red Bar Patterns                 | 테스트 작성 시점과 방법         |
| 27      | Testing Patterns                 | 상세 테스트 기법                |
| 28      | Green Bar Patterns               | 테스트 통과 전략                |
| 29      | xUnit Patterns                   | xUnit 프레임워크 사용법         |
| 30      | Design Patterns                  | TDD와 함께 사용하는 디자인 패턴 |
| 31      | Refactoring                      | 리팩토링 기법 (1)               |
| 32      | Mastering TDD                    | TDD 마스터하기                  |

## 핵심 패턴 카테고리

### Red Bar Patterns

테스트를 언제, 어디서, 어떻게 작성할지

### Green Bar Patterns

- **Fake It**: 하드코딩 후 점진적 일반화
- **Triangulate**: 여러 예제로 일반화
- **Obvious Implementation**: 명백하면 바로 구현

### Testing Patterns

- **Mock Object**: 의존성 대체
- **Self Shunt**: 테스트 자체를 mock으로 사용
- **Log String**: 호출 순서 추적

### Design Patterns

TDD에서 자주 등장하는 디자인 패턴들

## 학습 방법

Part 1, 2를 실습한 후 Part 3의 패턴들을 참조하며 이해를 깊게 한다.
