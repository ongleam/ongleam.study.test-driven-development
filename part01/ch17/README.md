# Chapter 17: Money Retrospective

> "TDD is an awareness of the gap between decision and feedback during programming, and techniques to control that gap." - Kent Beck

📌 **주제**: 회고, 메트릭스, 프로세스 분석

## 핵심 개념

Part 1 회고 - 과정과 결과 되돌아보기

## 회고 주제

### 1. Metaphor (메타포)

메타포가 설계 구조에 미친 영향:

- **Expression** - 수학적 표현식 메타포
- **Sum** - 덧셈 표현식
- **reduce** - 표현식을 단일 값으로 "축소"

메타포가 코드를 더 이해하기 쉽게 만들었다.

### 2. JUnit Usage (테스트 실행)

Money 예제 작성 중 테스트 실행 횟수: **약 125회**

- 거의 일정한 간격으로 테스트 실행
- 작은 단계마다 피드백 획득
- Red → Green → Refactor 사이클 반복

### 3. Process (TDD 프로세스)

| 단계     | 활동                 |
| -------- | -------------------- |
| Red      | 실패하는 테스트 작성 |
| Green    | 최소한의 코드로 통과 |
| Refactor | 중복 제거, 구조 개선 |

**사용된 전략들:**

- **Fake It** - 하드코딩으로 빠르게 통과 (Ch12)
- **Triangulation** - 두 테스트로 일반화 유도 (Ch13)
- **Obvious Implementation** - 명확하면 바로 구현

### 4. Test Quality (테스트 품질)

**Statement Coverage**: 높음 (거의 100%)

TDD 테스트의 특징:

- 결함 발견에 효과적
- 그러나 다른 테스트를 대체하지 않음
  - 성능 테스트
  - 사용성 테스트
  - 통합 테스트

## 코드 메트릭스

```
┌─────────────────┬───────────┬───────────┐
│                 │ 프로덕션  │ 테스트    │
├─────────────────┼───────────┼───────────┤
│ 라인 수         │ ~80       │ ~90       │
│ 함수 수         │ ~15       │ ~13       │
│ 복잡도          │ 낮음      │ 매우 낮음 │
└─────────────────┴───────────┴───────────┘
```

**낮은 복잡도의 이유**: 다형성 활용으로 조건문 최소화

## 남은 중복

```python
# Money.plus()
def plus(self, addend: Expression) -> Expression:
    return Sum(self, addend)

# Sum.plus()
def plus(self, addend: Expression) -> Expression:
    return Sum(self, addend)
```

**해결책**: Expression을 클래스로 만들어 공통 코드 추출

```python
class Expression(ABC):
    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)  # 공통 구현
```

## 핵심 교훈

### "Clean Code That Works"

1. **예측 가능한 개발** - 언제 끝나는지 알 수 있음
2. **긴 버그 꼬리 없음** - 작은 단계로 버그 조기 발견
3. **학습 기회** - 코드가 가르쳐주는 모든 것을 배울 수 있음

### TDD의 가치

- 결정과 피드백 사이의 간격을 인식
- 그 간격을 제어하는 기법

## Part 1 완료!

```
시작: $5 + 10 CHF = $10 (if rate is 2:1)
종료: 모든 TODO 완료, 깔끔한 설계
```

## 다음 단계

**Part 2: xUnit Example**

- 테스트 프레임워크 직접 구현
- Python으로 xUnit 만들기

## 테스트 실행

```bash
python -m pytest part01/ch17/ -v
```
