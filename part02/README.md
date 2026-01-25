# Part 2: The xUnit Example

Kent Beck의 『Test-Driven Development: By Example』 Part 2 실습

> "How do you test a testing framework? You use the framework to test itself." - Kent Beck

## 학습 로드맵

| Ch  | 제목                 | 핵심 개념            | 학습 목표                    |
| --- | -------------------- | -------------------- | ---------------------------- |
| 18  | First Steps to xUnit | Bootstrap            | 테스트 프레임워크 부트스트랩 |
| 19  | Set the Table        | setUp()              | 테스트 픽스처 설정           |
| 20  | Cleaning Up After    | tearDown()           | 테스트 정리 작업             |
| 21  | Counting             | TestResult           | 테스트 결과 집계             |
| 22  | Dealing with Failure | Exception Handling   | 실패한 테스트 처리           |
| 23  | How Suite It Is      | TestSuite, Composite | 테스트 스위트 구현           |
| 24  | xUnit Retrospective  | -                    | 회고, 정리                   |

## 전체 진행 흐름

```
Ch18:    TestCase 기본 구조
         └─ 메서드 이름으로 테스트 실행

Ch19-20: 테스트 생명주기
         └─ setUp() → test → tearDown()

Ch21-22: 결과 수집
         └─ TestResult, 실패 처리

Ch23:    테스트 스위트
         └─ Composite 패턴으로 여러 테스트 묶기

Ch24:    회고
         └─ 자기 참조적 테스트의 의미
```

## 최종 클래스 구조

```
TestCase
├── __init__(name)
├── setUp()
├── tearDown()
└── run(result)

TestResult
├── runCount
├── failureCount
├── testStarted()
├── testFailed()
└── summary()

TestSuite
├── tests: list[TestCase]
├── add(test)
└── run(result)
```

## 부트스트랩 문제

xUnit의 핵심 도전:

- 테스트 프레임워크를 테스트하려면 테스트 프레임워크가 필요
- 해결: 프레임워크 자체로 자신을 테스트

## 테스트 실행

```bash
# Part 2 전체 테스트
python -m pytest part02/ -v

# 특정 챕터 테스트
python -m pytest part02/ch18/ -v
```

## 챕터별 바로가기

- [Chapter 18: First Steps to xUnit](./ch18/README.md)
- [Chapter 19: Set the Table](./ch19/README.md)
- [Chapter 20: Cleaning Up After](./ch20/README.md)
- [Chapter 21: Counting](./ch21/README.md)
- [Chapter 22: Dealing with Failure](./ch22/README.md)
- [Chapter 23: How Suite It Is](./ch23/README.md)
- [Chapter 24: xUnit Retrospective](./ch24/README.md)
