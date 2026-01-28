# Chapter 24: xUnit Retrospective

> "xUnit을 직접 만들어보면 프로그래밍 언어와 테스트 개념에 대한 이해가 깊어진다." - Kent Beck

## 개요

Part 2 xUnit Example의 회고 챕터. xUnit 프레임워크 구현을 통해 배운 것들을 정리한다.

## 핵심 학습 포인트

### 1. Assertion Failure vs Error

- **Assertion Failure**: 예상과 실제 결과가 다른 경우
- **Error**: 예외 발생 등 테스트 실행 중 문제
- 대부분의 xUnit 구현체는 이 둘을 구분하여 표시
- Assertion failure가 일반 에러보다 디버깅에 시간이 더 걸림

### 2. xUnit GUI

- 중요도 순으로 에러 표시
- Red/Green 바로 즉각적인 피드백 제공

### 3. Bootstrap Problem

- 테스트 프레임워크를 테스트 프레임워크로 테스트
- 자기 자신을 검증하는 흥미로운 문제

## Part 2에서 구현한 것들

| Chapter | 주제                 | 구현 내용                          |
| ------- | -------------------- | ---------------------------------- |
| 18      | First Steps to xUnit | TestCase, WasRun, run()            |
| 19      | Set the Table        | setUp()                            |
| 20      | Cleaning Up After    | tearDown(), Template Method        |
| 21      | Counting             | TestResult, runCount, failureCount |
| 22      | Dealing with Failure | testFailed(), 예외 처리            |
| 23      | How Suite It Is      | TestSuite, Composite 패턴          |

## 완료된 TODO 리스트

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [x] 테스트 메서드가 실패해도 tearDown 호출하기
- [x] 여러 테스트 실행하기
- [x] 수집된 결과를 출력하기
- [x] 실패한 테스트 수 추적하기

## 배운 패턴들

1. **Template Method**: setUp -> test -> tearDown 순서
2. **Composite**: TestCase와 TestSuite를 동일하게 다룸
3. **Collecting Parameter**: TestResult를 전달하여 결과 수집
4. **Pluggable Selector**: 메서드 이름으로 테스트 선택

## 다음 Part 예고

- Part 3: Patterns for Test-Driven Development
- TDD 패턴, Red Bar 패턴, Green Bar 패턴 등
