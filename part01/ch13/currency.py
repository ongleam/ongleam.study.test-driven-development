from __future__ import annotations

from abc import ABC, abstractmethod

# Chapter 13: Make It
# "Fake It"에서 실제 구현으로 전환
#
# Kent Beck: "We have duplication between the data in the test
# and the data in the code. We have to eliminate it."
# ($5 + $5 = $10 에서 10이 테스트와 코드에 중복!)


# Expression 인터페이스 - reduce() 추가
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """Expression을 단일 통화로 환산"""
        pass


# Money 클래스 - Expression 구현
class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Sum:
        """덧셈 - Sum 반환"""
        return Sum(self, addend)

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """Money는 그대로 반환 (같은 통화일 때)"""
        return self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self) -> int:
        return hash((self._amount, self._currency))

    def __repr__(self) -> str:
        return f"Money({self._amount}, '{self._currency}')"

    # 팩토리 메서드
    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")


# Sum 클래스 - reduce() 실제 구현
class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """augend + addend 의 실제 합계 반환

        Chapter 12의 하드코딩($10)을 실제 계산으로 교체!
        """
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to_currency)


# Bank 클래스 - 타입 체크 후 다형성으로 리팩토링 예정
class Bank:
    def reduce(self, source: Expression, to_currency: str) -> Money:
        """타입별 reduce() 호출

        Chapter 12: return Money.dollar(10)  # Fake It!
        Chapter 13: 타입 체크로 분기 처리
        """
        if isinstance(source, Money):
            return source.reduce(self, to_currency)
        sum_expr: Sum = source  # type: ignore
        return sum_expr.reduce(self, to_currency)
