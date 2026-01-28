"""Fibonacci 수열 - TDD로 구현"""


def fib(n: int) -> int:
    """n번째 피보나치 수를 반환한다.

    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)  (n >= 2)

    Args:
        n: 0 이상의 정수

    Returns:
        n번째 피보나치 수
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 반복적 구현 - O(n) 시간, O(1) 공간
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
