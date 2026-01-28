# Appendix: 부록

> Kent Beck의 "Test-Driven Development: By Example" 부록 내용

## 구성

| Appendix | 제목               | 내용                           |
| -------- | ------------------ | ------------------------------ |
| I        | Influence Diagrams | 피드백 다이어그램과 TDD의 심리 |
| II       | Fibonacci          | TDD로 피보나치 구현하기        |

## Appendix I: Influence Diagrams (영향 다이어그램)

자세한 내용은 [influence_diagrams/README.md](./influence_diagrams/README.md) 참조

## Appendix II: Fibonacci (피보나치)

자세한 내용은 [fibonacci/README.md](./fibonacci/README.md) 참조

## 테스트 실행

```bash
# 피보나치 테스트
cd appendix/fibonacci && python -m pytest test_fibonacci.py -v
```
