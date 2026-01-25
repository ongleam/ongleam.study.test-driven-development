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
# Run all tests in part01
python -m pytest part01/

# Run tests in a specific chapter
python -m pytest part01/ch01/

# Run a specific test file
python -m pytest part01/ch01/test_currency.py

# Run a specific test function
python -m pytest part01/ch01/test_currency.py::test_function_name

# Run tests with verbose output
python -m pytest -v part01/
```

## Architecture

### Directory Structure

```
ongleam.study.tdd/
├── part01/                   # Part 1: The Money Example
│   ├── ch01/                 # Chapter 01
│   │   ├── README.md         # Chapter notes
│   │   ├── currency.py       # Implementation code
│   │   └── test_currency.py  # Test code
│   ├── ch02/                 # Chapter 02
│   ├── ...
│   ├── ch17/                 # Chapter 17
│   ├── currency.py           # Shared currency module
│   └── tests/                # Integration tests
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
