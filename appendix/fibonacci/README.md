# Appendix II: Fibonacci (피보나치)

> TDD의 클래식한 예제 - 피보나치 수열 구현

## 개요

피보나치 수열을 TDD로 구현하는 과정을 보여준다. 간단한 예제지만 TDD의 핵심 리듬을 명확하게 보여준다.

## 피보나치 수열

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)  (n >= 2)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

## TDD 단계별 구현

### Step 1: 가장 단순한 케이스 (fib(0))

```python
# test_fibonacci.py
def test_fib_0():
    assert fib(0) == 0
```

```python
# fibonacci.py - Fake It
def fib(n):
    return 0
```

### Step 2: 다음 단순 케이스 (fib(1))

```python
def test_fib_1():
    assert fib(1) == 1
```

```python
# Triangulation을 위한 수정
def fib(n):
    if n == 0:
        return 0
    return 1
```

### Step 3: 패턴 발견 (fib(2))

```python
def test_fib_2():
    assert fib(2) == 1
```

테스트 통과! `fib(2) = fib(1) + fib(0) = 1 + 0 = 1`

### Step 4: 일반화 필요 (fib(3))

```python
def test_fib_3():
    assert fib(3) == 2
```

```python
# 재귀적 구현 (Obvious Implementation)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

### Step 5: 더 큰 값으로 검증

```python
def test_fib_larger():
    assert fib(5) == 5
    assert fib(10) == 55
```

## 최종 코드

### fibonacci.py

```python
"""Fibonacci 수열 - TDD로 구현"""


def fib(n: int) -> int:
    """n번째 피보나치 수를 반환한다.

    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)  (n >= 2)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

### test_fibonacci.py

```python
"""Fibonacci TDD 테스트"""

from fibonacci import fib


def test_fib_0():
    """fib(0) = 0"""
    assert fib(0) == 0


def test_fib_1():
    """fib(1) = 1"""
    assert fib(1) == 1


def test_fib_2():
    """fib(2) = fib(1) + fib(0) = 1"""
    assert fib(2) == 1


def test_fib_3():
    """fib(3) = fib(2) + fib(1) = 2"""
    assert fib(3) == 2


def test_fib_larger():
    """더 큰 피보나치 수"""
    assert fib(5) == 5
    assert fib(10) == 55
    assert fib(20) == 6765
```

## 리팩토링: 성능 개선

재귀 버전은 큰 n에서 매우 느리다 (O(2^n)). TDD로 최적화해보자.

### 반복적 구현 (Iterative)

테스트는 그대로 두고, 구현만 변경:

```python
def fib(n: int) -> int:
    """반복적 구현 - O(n) 시간, O(1) 공간"""
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

테스트 실행 → 모두 통과 → 리팩토링 성공!

### 메모이제이션 (Memoization)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """메모이제이션 - O(n) 시간, O(n) 공간"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

## TDD 교훈

### 1. 가장 단순한 것부터

```
fib(0) → fib(1) → fib(2) → fib(3) → ...
```

### 2. 작은 단계로 진행

각 테스트는 **하나의 새로운 요구사항**만 추가

### 3. 테스트가 리팩토링을 보호

구현을 재귀에서 반복으로 변경해도 테스트가 정확성 보장

### 4. Triangulation

`fib(0)`과 `fib(1)` 두 예제로 기본 케이스 패턴 발견

### 5. Obvious Implementation

패턴이 명확해지면 바로 일반적 구현 작성

## 실행

```bash
cd appendix/fibonacci
python -m pytest test_fibonacci.py -v
```

## 연습 문제

1. **음수 처리**: `fib(-1)`은 어떻게 처리해야 할까?
2. **큰 수**: `fib(100)`을 계산하려면?
3. **일반화**: 피보나치 같은 수열(fib(n) = fib(n-1) + fib(n-2) + fib(n-3))은?

```python
# 힌트: 먼저 테스트 작성
def test_fib_negative():
    # 어떤 결과를 기대해야 할까?
    # - 0 반환?
    # - 예외 발생?
    # - 음수 피보나치 (확장 정의)?
    pass
```
