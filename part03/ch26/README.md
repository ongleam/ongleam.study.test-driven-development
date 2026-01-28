# Chapter 26: Red Bar Patterns

> "테스트를 언제, 어디서, 언제 멈출지에 대한 패턴들" - Kent Beck

## 개요

Red Bar Patterns는 테스트 작성의 타이밍과 방법을 다룬다. 빨간 막대(실패하는 테스트)를 만드는 전략들이다.

## 패턴 목록

### 1. One Step Test (한 걸음 테스트)

**문제**: 테스트 목록에서 다음에 작성할 테스트를 어떻게 선택하는가?

**해결**: 학습과 구현에 대한 자신감을 높여주는 테스트를 선택한다.

- 테스트 목록은 반복적으로 검토
- 적절한 테스트가 없으면 새로운 테스트 생성
- 너무 큰 걸음은 피하고, 작은 걸음으로

```python
# 좋은 예: 작은 걸음
def test_multiplication(self):
    five = Dollar(5)
    assert five.times(2) == Dollar(10)

# 나쁜 예: 너무 큰 걸음
def test_complete_currency_conversion(self):
    # 여러 개념을 한 번에 테스트
    ...
```

### 2. Starter Test (시작 테스트)

**문제**: 어떤 테스트부터 시작해야 하는가?

**해결**: 가장 간단한 형태의 연산을 나타내는 테스트로 시작한다.

- 복잡한 테스트는 피함
- 빠른 피드백 확보
- 동시에 해결할 문제 수를 최소화

```python
# Starter Test 예시
def test_empty(self):
    assert sum([]) == 0

def test_single(self):
    assert sum([5]) == 5

# 그 다음
def test_multiple(self):
    assert sum([1, 2, 3]) == 6
```

### 3. Explanation Test (설명 테스트)

**문제**: 자동화된 테스트를 더 폭넓게 퍼뜨리려면?

**해결**: 테스트를 사용해 설명을 요청하고 제공한다.

- "이게 어떻게 동작하나요?" → 테스트로 보여줌
- 코드 리뷰 시 테스트로 의도 설명
- 문서화 역할

### 4. Learning Test (학습 테스트)

**문제**: 외부 소프트웨어의 동작을 어떻게 이해하는가?

**해결**: 사용하려는 API의 테스트를 작성한다.

```python
# 외부 라이브러리 학습
def test_json_loads(self):
    """json.loads의 동작 확인"""
    result = json.loads('{"key": "value"}')
    assert result == {"key": "value"}

def test_json_loads_with_array(self):
    """배열 처리 확인"""
    result = json.loads('[1, 2, 3]')
    assert result == [1, 2, 3]
```

### 5. Another Test (또 다른 테스트)

**문제**: 토론이 주제를 벗어날 때 어떻게 집중을 유지하는가?

**해결**: 새로운 아이디어가 떠오르면 테스트 목록에 추가하고, 현재 작업에 집중한다.

- 아이디어를 잃지 않으면서
- 현재 흐름을 유지
- TODO 리스트에 기록

### 6. Regression Test (회귀 테스트)

**문제**: 결함이 발견되면 어떻게 해야 하는가?

**해결**: 결함을 재현하는 가장 작은 테스트를 작성한다.

```python
# 버그 리포트: "음수 입력 시 오류 발생"
def test_negative_input(self):
    """Issue #123: 음수 입력 처리"""
    result = calculate(-5)
    assert result == -10  # 먼저 실패 확인, 그 다음 수정
```

- 테스트 없이 버그 수정하지 않음
- 테스트가 먼저 실패해야 함
- 같은 버그가 재발하지 않도록 보장

### 7. Break (휴식)

**문제**: 피곤하거나 막혔을 때 어떻게 해야 하는가?

**해결**: 휴식을 취한다.

- 산책, 낮잠, 커피
- 무의식이 문제를 해결하도록
- 피로한 상태에서 코딩은 비효율적

### 8. Do Over (다시 하기)

**문제**: 길을 잃었을 때 어떻게 해야 하는가?

**해결**: 코드를 버리고 처음부터 다시 시작한다.

- 잘못된 방향으로 깊이 들어가기 전에
- git reset --hard 또는 코드 삭제
- 두 번째 시도는 훨씬 빠름

### 9. Cheap Desk, Nice Chair (싼 책상, 좋은 의자)

**문제**: TDD에 어떤 물리적 환경이 적합한가?

**해결**: 편안한 환경에 투자한다.

- 좋은 의자, 모니터, 키보드
- 집중할 수 있는 환경
- 짝 프로그래밍 공간

## 핵심 원칙

1. **작은 걸음**: 한 번에 하나씩
2. **빠른 피드백**: 즉시 결과 확인
3. **집중 유지**: 현재 작업에 몰입
4. **휴식**: 지치면 쉬기

## 다음 챕터 예고

- Chapter 27: Testing Patterns
- Mock Object, Self Shunt, Log String 등 상세 테스트 기법
