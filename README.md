# TDD Practice Repository

켄트 벡(Kent Beck)의 『Test-Driven Development: By Example』을 바탕으로 TDD를 연습하는 저장소입니다.

## 목표

- Red-Green-Refactor 사이클 체득
- 작은 단위의 테스트부터 시작하여 점진적으로 기능 구현
- 테스트 코드를 통한 설계 개선

## 구성

```
ongleam.study.tdd/
├── part01/                   # Part 1: The Money Example (ch01-ch17)
│   ├── ch01/                 # 각 챕터별 디렉토리
│   │   ├── README.md         # 챕터 노트
│   │   ├── currency.py       # 구현 코드
│   │   └── test_currency.py  # 테스트 코드
│   └── ...
```

## TDD 사이클

1. **Red**: 실패하는 테스트 작성
2. **Green**: 테스트를 통과하는 최소한의 코드 작성
3. **Refactor**: 코드 개선 및 중복 제거

## 테스트 실행 방법

```bash
# Part 1 전체 테스트 실행
python -m pytest part01/

# 특정 챕터 테스트 실행
python -m pytest part01/ch01/

# 특정 테스트 파일 실행
python -m pytest part01/ch01/test_currency.py

# 특정 테스트 케이스 실행
python -m pytest part01/ch01/test_currency.py::test_multiplication

# 상세한 출력과 함께 실행
python -m pytest part01/ -v

# 실패한 테스트만 다시 실행
python -m pytest part01/ --lf
```

## 참고 자료

- Kent Beck, "Test-Driven Development: By Example"
