"""Fibonacci TDD 테스트"""

from fibonacci import fib


# Step 1: 가장 단순한 케이스
def test_fib_0():
    """fib(0) = 0"""
    assert fib(0) == 0


# Step 2: 다음 단순 케이스
def test_fib_1():
    """fib(1) = 1"""
    assert fib(1) == 1


# Step 3: 패턴 확인
def test_fib_2():
    """fib(2) = fib(1) + fib(0) = 1"""
    assert fib(2) == 1


# Step 4: 일반화 필요
def test_fib_3():
    """fib(3) = fib(2) + fib(1) = 2"""
    assert fib(3) == 2


# Step 5: 더 큰 값으로 검증
def test_fib_larger():
    """더 큰 피보나치 수"""
    assert fib(5) == 5
    assert fib(10) == 55
    assert fib(20) == 6765


# 추가 테스트: 경계 값
def test_fib_edge_cases():
    """경계 값 테스트"""
    assert fib(4) == 3   # 0, 1, 1, 2, 3
    assert fib(6) == 8   # 0, 1, 1, 2, 3, 5, 8
    assert fib(7) == 13  # 0, 1, 1, 2, 3, 5, 8, 13
