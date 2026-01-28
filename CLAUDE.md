# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kent Beck의 『Test-Driven Development: By Example』을 기반으로 TDD를 연습하는 저장소입니다. Red-Green-Refactor 사이클을 따르며, 각 챕터는 별도 디렉토리(`part01/ch01`, `part01/ch02`, etc.)로 구성됩니다.

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
python -m pytest

# Run all tests in part01 (Money Example)
python -m pytest part01/

# Run all tests in part02 (xUnit Example)
python -m pytest part02/

# Run tests in a specific chapter
python -m pytest part01/ch01/
python -m pytest part02/ch18/

# Run a specific test file
python -m pytest part01/ch01/test_currency.py
python -m pytest part02/ch18/test_xunit.py

# Run a specific test function
python -m pytest part01/ch01/test_currency.py::test_function_name

# Run tests with verbose output
python -m pytest -v
```

## Architecture

### Directory Structure

```
ongleam.study.test-driven-development/
├── part01/                   # Part 1: The Money Example (ch01-ch17)
│   ├── ch01/                 # Chapter 01
│   │   ├── README.md         # Chapter notes
│   │   ├── currency.py       # Implementation code
│   │   └── test_currency.py  # Test code
│   ├── ch02/ ~ ch17/         # Chapters 02-17
│   ├── currency.py           # Shared currency module
│   └── tests/                # Integration tests
├── part02/                   # Part 2: The xUnit Example (ch18-ch24)
│   ├── ch18/                 # Chapter 18: First Steps to xUnit
│   │   ├── README.md         # Chapter notes
│   │   ├── xunit.py          # xUnit implementation
│   │   └── test_xunit.py     # Test code
│   ├── ch19/                 # Chapter 19: Set the Table (setUp)
│   └── ...                   # Upcoming chapters
```

### Test Organization

- 각 챕터 디렉토리 내에 테스트 파일 위치
- pytest 네이밍 컨벤션: `test_*.py` 또는 `*_test.py`
- 테스트 함수는 `test_`로 시작

## Development Practices

- Python을 주 언어로 사용
- pytest를 테스트 프레임워크로 사용
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
