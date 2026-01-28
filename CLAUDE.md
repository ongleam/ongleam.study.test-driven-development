# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kent Beck의 『Test-Driven Development: By Example』을 기반으로 TDD를 연습하는 저장소입니다. Red-Green-Refactor 사이클을 따르며, 각 챕터는 별도 디렉토리(`part01/ch01`, `part02/ch18`, `part03/ch25` 등)로 구성됩니다.

## TDD Workflow

이 저장소의 핵심 개발 방법론:

1. **Red**: 실패하는 테스트를 먼저 작성
2. **Green**: 테스트를 통과하는 최소한의 코드 작성
3. **Refactor**: 코드 개선 및 중복 제거

모든 코드 작성 시 이 사이클을 엄격하게 준수해야 합니다.

## Commands

### Running Tests

```bash
# Run all tests
uv run pytest

# Run all tests in each part
uv run pytest part01/    # Money Example
uv run pytest part02/    # xUnit Example
uv run pytest part03/    # Patterns (ch30 only)

# Run tests in a specific chapter
uv run pytest part01/ch01/
uv run pytest part02/ch18/
uv run pytest part03/ch30/

# Run a specific test file
uv run pytest part01/ch01/test_currency.py
uv run pytest part02/ch23/test_xunit.py

# Run tests with verbose output
uv run pytest -v

# Run ch30 design pattern tests
cd part03/ch30 && uv run pytest test_patterns.py -v
```

## Architecture

### Directory Structure

```
ongleam.study.test-driven-development/
├── part01/                   # Part 1: The Money Example (ch01-ch17)
│   ├── ch01/ ~ ch17/         # 각 챕터별 디렉토리
│   │   ├── README.md         # 챕터 노트
│   │   ├── currency.py       # 구현 코드
│   │   └── test_currency.py  # 테스트 코드
│   ├── currency.py           # 공유 모듈
│   └── tests/                # 통합 테스트
│
├── part02/                   # Part 2: The xUnit Example (ch18-ch24)
│   ├── ch18/                 # First Steps to xUnit
│   ├── ch19/                 # Set the Table (setUp)
│   ├── ch20/                 # Cleaning Up After (tearDown)
│   ├── ch21/                 # Counting (TestResult)
│   ├── ch22/                 # Dealing with Failure
│   ├── ch23/                 # How Suite It Is (TestSuite)
│   └── ch24/                 # xUnit Retrospective (README only)
│
├── part03/                   # Part 3: Patterns for TDD (ch25-ch32)
│   ├── ch25/                 # TDD Patterns (README only)
│   ├── ch26/                 # Red Bar Patterns (README only)
│   ├── ch27/                 # Testing Patterns (README only)
│   ├── ch28/                 # Green Bar Patterns (README only)
│   ├── ch29/                 # xUnit Patterns (README only)
│   ├── ch30/                 # Design Patterns (코드 + 테스트)
│   │   ├── README.md         # 11개 디자인 패턴 설명
│   │   ├── command.py        # Command 패턴
│   │   ├── value_object.py   # Value Object 패턴
│   │   ├── null_object.py    # Null Object 패턴
│   │   ├── template_method.py # Template Method 패턴
│   │   ├── pluggable_object.py # Pluggable Object 패턴
│   │   ├── pluggable_selector.py # Pluggable Selector 패턴
│   │   ├── factory_method.py # Factory Method 패턴
│   │   ├── imposter.py       # Imposter 패턴
│   │   ├── composite.py      # Composite 패턴
│   │   ├── collecting_parameter.py # Collecting Parameter 패턴
│   │   ├── singleton.py      # Singleton 패턴
│   │   └── test_patterns.py  # 모든 패턴 테스트
│   ├── ch31/                 # Refactoring (README only)
│   └── ch32/                 # Mastering TDD (README only)
```

### Book Structure Mapping

| Part   | Chapters  | 내용              | 구현                      |
| ------ | --------- | ----------------- | ------------------------- |
| Part 1 | ch01-ch17 | The Money Example | 코드 + 테스트             |
| Part 2 | ch18-ch24 | The xUnit Example | 코드 + 테스트 (ch24 제외) |
| Part 3 | ch25-ch32 | Patterns for TDD  | README (ch30만 코드)      |

### Test Organization

- 각 챕터 디렉토리 내에 테스트 파일 위치
- pytest 네이밍 컨벤션: `test_*.py` 또는 `*_test.py`
- 테스트 함수는 `test_`로 시작
- Part 2의 xUnit 테스트는 pytest 래퍼 함수 사용

## Key Patterns by Part

### Part 1: Money Example

- Value Object (Money, Dollar, Franc)
- Factory Method (Money.dollar(), Money.franc())
- Imposter (Sum implements Expression)
- Composite (Expression)

### Part 2: xUnit Example

- Template Method (setUp → test → tearDown)
- Pluggable Selector (getattr)
- Composite (TestSuite)
- Collecting Parameter (TestResult)
- Log String (WasRun.log)

### Part 3: Patterns Reference

- Red Bar Patterns: One Step Test, Starter Test, Learning Test
- Green Bar Patterns: Fake It, Triangulate, Obvious Implementation
- Testing Patterns: Mock Object, Self Shunt, Log String
- Design Patterns: 11개 패턴 (ch30에 코드 예시)
- Refactoring: Extract Method, Move Method, etc.

## Development Practices

- Python을 주 언어로 사용
- pytest를 테스트 프레임워크로 사용
- uv를 패키지 관리자로 사용
- 각 챕터는 독립적인 연습 단위
- 한글 주석 사용 (Korean comments for internal documentation)

## References

### 원서

- Kent Beck, _Test-Driven Development: By Example_, Addison-Wesley, 2003

### 참고 구현 저장소

- [jdodds/py-tdd-by-example](https://github.com/jdodds/py-tdd-by-example) - Python으로 책의 예제를 따라가는 저장소 (챕터별 태그 제공)
- [brunogabriel/xUnit-tdd](https://github.com/brunogabriel/xUnit-tdd) - xUnit 구현 코드 (완성된 버전)
- [bioerrorlog/kent-beck-tdd-python](https://github.com/bioerrorlog/kent-beck-tdd-python) - Kent Beck TDD 책 Python 구현
- [vnqthai/tdd-kentbeck](https://github.com/vnqthai/tdd-kentbeck) - TDD by Example 소스 코드

### 학습 자료

- [Notes on TDD by Example](https://stanislaw.github.io/2016-01-25-notes-on-test-driven-development-by-example-by-kent-beck.html) - 책 요약 노트
- [TDD notes from Kent Beck book (Gist)](https://gist.github.com/kkisiele/ab1e1bc1b6312cdf20ad7839ae31f5b3) - TDD 핵심 개념 정리
- [Test Driven Development: By Example - O'Reilly](https://www.oreilly.com/library/view/test-driven-development/0321146530/) - 원서 (O'Reilly)
- [TDD Buddy - Green Bar Patterns](https://www.tddbuddy.com/references/green-bar-patterns.html) - Green Bar 패턴 레퍼런스
