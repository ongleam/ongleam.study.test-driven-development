# Chapter 32: Mastering TDD

> "TDD는 프로그래밍 중 불안감을 관리하는 기법이다." - Kent Beck

## 개요

TDD에 대한 자주 묻는 질문과 답변을 다룬다. TDD를 마스터하기 위한 실용적인 조언들이다.

## 자주 묻는 질문

### Q1. 한 걸음의 크기는 얼마나 커야 하는가?

**A**: 상황에 따라 다르다.

- **확신이 있을 때**: 큰 걸음 (Obvious Implementation)
- **불확실할 때**: 작은 걸음 (Fake It, Triangulate)
- **실패하면**: 더 작은 걸음으로

```python
# 작은 걸음 예시
def test_sum_empty():
    assert sum([]) == 0

def test_sum_one():
    assert sum([5]) == 5

def test_sum_many():
    assert sum([1, 2, 3]) == 6
```

**핵심**: 의심스러우면 작게 가라.

---

### Q2. 테스트하지 않아도 되는 것은?

**A**: 테스트를 작성하면서 얻는 **자신감**에 집중하라.

테스트할 필요 없는 것:

- 단순한 getter/setter (로직이 없음)
- 외부 라이브러리/프레임워크 (이미 테스트됨)
- private 메서드 (public을 통해 간접 테스트)
- 생성자 (단순 할당만)

테스트해야 하는 것:

- 조건문이 있는 코드
- 비즈니스 로직
- 버그가 발생했던 코드 (회귀 테스트)
- 복잡한 알고리즘

```python
# 테스트 불필요
class User:
    def __init__(self, name):
        self.name = name  # 단순 할당

# 테스트 필요
class User:
    def is_adult(self):
        return self.age >= 18  # 조건문
```

---

### Q3. 좋은 테스트인지 어떻게 아는가?

**A**: 좋은 테스트의 특징 (F.I.R.S.T):

| 특성                | 설명                    |
| ------------------- | ----------------------- |
| **F**ast            | 빠르게 실행됨           |
| **I**ndependent     | 다른 테스트와 독립적    |
| **R**epeatable      | 반복 실행해도 같은 결과 |
| **S**elf-validating | 자동으로 성공/실패 판단 |
| **T**imely          | 적시에 작성 (코드 전에) |

**나쁜 테스트의 징후**:

- 실행이 느림 (외부 의존성)
- 순서에 따라 결과가 달라짐
- 가끔 실패함 (flaky test)
- 하나 고치면 여러 개 깨짐

---

### Q4. TDD는 어떻게 프레임워크로 이어지는가?

**A**: TDD를 하다 보면 자연스럽게 재사용 가능한 추상화가 등장한다.

```python
# 테스트를 위해 만든 코드
class MockDatabase:
    def save(self, data): pass
    def load(self, id): return {}

# 반복되면 → 프레임워크로 발전
class Repository(ABC):
    @abstractmethod
    def save(self, entity): pass

    @abstractmethod
    def find_by_id(self, id): pass
```

Part 1의 Money → Expression → Bank 진화가 좋은 예.

---

### Q5. 얼마나 많은 피드백이 필요한가?

**A**: 불안감이 사라질 만큼.

- **초보자**: 더 많은 테스트, 작은 걸음
- **숙련자**: 적은 테스트로도 자신감
- **새로운 도메인**: 다시 작은 걸음으로

```
테스트 수 ∝ 1 / 자신감
```

---

### Q6. 테스트를 삭제해야 할 때는?

**A**: 테스트가 가치보다 비용이 클 때.

삭제 고려 대상:

- 중복 테스트 (같은 코드 경로)
- 느린 테스트 (빠른 것으로 대체 가능)
- 깨지기 쉬운 테스트 (구현에 의존)
- 리팩토링마다 수정 필요한 테스트

**주의**: 회귀 테스트는 보존

---

### Q7. 프로그래밍 언어/환경이 TDD에 영향을 주는가?

**A**: 그렇다.

TDD 친화적 환경:

- 빠른 컴파일/실행
- 좋은 테스트 프레임워크
- 리팩토링 도구
- REPL (빠른 실험)

```
Python, Ruby, JavaScript → TDD 쉬움
C++, Java (무거운 빌드) → TDD 어려움 (개선 중)
```

---

### Q8. 거대한 시스템도 TDD로 개발할 수 있는가?

**A**: 그렇다. 단, 아키텍처가 중요.

전략:

- 모듈별 독립 테스트
- 통합 테스트는 최소화
- 테스트 피라미드 준수

```
       /\
      /  \  E2E (적게)
     /----\
    /      \ Integration (중간)
   /--------\
  /          \ Unit (많이)
```

---

### Q9. 애플리케이션 수준 테스트로 개발을 주도할 수 있는가?

**A**: 가능하지만 어렵다 (ATDD/BDD).

```gherkin
# 애플리케이션 수준 테스트 (BDD)
Given 사용자가 로그인했을 때
When 장바구니에 상품을 추가하면
Then 장바구니 수량이 증가한다
```

**도전 과제**:

- 실행 속도가 느림
- 이해관계자 참여 필요
- 유지보수 비용

---

### Q10. 진행 중인 프로젝트에서 TDD로 전환하려면?

**A**: 점진적으로.

1. **새 코드**부터 TDD 적용
2. **버그 수정** 시 테스트 먼저 작성
3. **변경할 코드** 주변에 테스트 추가
4. 레거시 코드는 필요할 때만

```python
# 버그 수정 시
def test_negative_amount_bug():
    """Issue #42 재현"""
    result = calculate(-10)
    assert result >= 0  # 먼저 실패 확인

# 그 다음 수정
```

---

### Q11. TDD는 누구를 위한 것인가?

**A**: 프로그래머.

- **초보자**: 설계 사고력 향상
- **경력자**: 자신감과 속도 향상
- **팀**: 코드 품질과 문서화

TDD가 맞지 않을 수 있는 경우:

- 탐색적 프로토타이핑
- 한 번 쓰고 버리는 코드
- 테스트 불가능한 UI/하드웨어

---

### Q12. TDD는 초기 조건에 민감한가?

**A**: 어느 정도는.

좋은 시작:

- 명확한 요구사항
- 적절한 크기의 첫 번째 테스트
- 작동하는 개발 환경

나쁜 시작에서 회복:

- 테스트 삭제하고 다시 시작 (Do Over)
- 더 작은 문제로 분해
- 페어 프로그래밍

---

### Q13. TDD와 디자인 패턴의 관계는?

**A**: TDD가 패턴을 자연스럽게 발견하게 한다.

```
테스트 작성 → 중복 발견 → 리팩토링 → 패턴 등장
```

Part 1 예시:

- Value Object → Money
- Factory Method → Money.dollar()
- Composite → Expression

**주의**: 패턴을 미리 적용하지 말고, 필요할 때 발견하라.

---

### Q14. TDD는 왜 동작하는가?

**A**: 여러 이유.

1. **피드백 루프 단축**: 빠른 오류 발견
2. **작은 단계**: 복잡도 관리
3. **설계 압력**: 테스트 가능한 설계 유도
4. **문서화**: 테스트가 사용법 예시
5. **자신감**: 변경에 대한 두려움 감소

```
두려움 → 주저 → 덜 빈번한 변경 → 나쁜 코드 → 더 큰 두려움
     ↑                                              |
     └──────────────────────────────────────────────┘

TDD → 자신감 → 빈번한 변경 → 좋은 코드 → 더 큰 자신감
```

---

### Q15. "Test-Driven Development"라는 이름의 의미는?

**A**: 테스트가 개발을 **주도(drive)**한다.

- 테스트 먼저 → 설계 결정
- 테스트 통과 → 진행 허가
- 테스트 실패 → 방향 수정

**테스트 후 개발(Test-After Development)**과의 차이:

- TAD: 코드 작성 후 테스트 (검증 목적)
- TDD: 테스트 먼저 작성 (설계 목적)

---

### Q16. TDD와 Extreme Programming(XP)의 관계는?

**A**: TDD는 XP의 핵심 프랙티스 중 하나.

XP 프랙티스:

- **TDD** ← 여기
- 짝 프로그래밍
- 지속적 통합
- 리팩토링
- 단순한 설계

TDD는 독립적으로도 사용 가능하지만, 다른 프랙티스와 함께할 때 더 효과적.

---

### Q17. Darach의 도전

**Q**: "테스트를 먼저 작성하면 설계가 정말 더 좋아지는가?"

**A**: 직접 경험해보라.

```
1주일 동안 TDD로 개발
→ 결과물의 설계 품질 평가
→ 같은 문제를 TDD 없이 개발
→ 비교
```

대부분의 개발자가 TDD 후 더 나은 설계를 경험한다고 보고.

---

## 핵심 교훈

### 1. 불안감 관리

> "TDD는 프로그래밍 중 불안감을 관리하는 기법이다."

- 불안하면 테스트 작성
- 자신감이 생기면 더 큰 걸음
- 실패하면 더 작은 걸음

### 2. 지속적 개선

```
Red → Green → Refactor → (반복)
```

### 3. 실용주의

- 규칙은 가이드라인
- 상황에 맞게 적용
- 목표는 **작동하는 깨끗한 코드**

---

## Part 3 완료

### 학습한 패턴 카테고리

| 챕터 | 카테고리           | 핵심 패턴                                    |
| ---- | ------------------ | -------------------------------------------- |
| 25   | TDD Patterns       | Red-Green-Refactor                           |
| 26   | Red Bar Patterns   | One Step Test, Starter Test                  |
| 27   | Testing Patterns   | Mock Object, Self Shunt, Log String          |
| 28   | Green Bar Patterns | Fake It, Triangulate, Obvious Implementation |
| 29   | xUnit Patterns     | Assertion, Fixture, Test Method              |
| 30   | Design Patterns    | Value Object, Composite, Factory Method      |
| 31   | Refactoring        | Extract Method, Move Method                  |
| 32   | Mastering TDD      | FAQ, Best Practices                          |

---

## 마무리

> "Clean code that works." - Ron Jeffries

TDD의 목표는 **작동하는 깨끗한 코드**다.

1. **작동하는** → Green (테스트 통과)
2. **깨끗한** → Refactor (리팩토링)
3. **코드** → 실제 소프트웨어

이제 직접 해보라. 연습만이 마스터리로 이끈다.
