from __future__ import annotations

# Chapter 12: Addition, Finally
# "Fake It" 패턴 - 하드코딩으로 테스트 통과
#
# Kent Beck: "Return a constant and gradually replace constants
# with variables until you have the real code."


# Expression 인터페이스 (마커 클래스)
class Expression:
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


# Sum 클래스 - 두 Expression의 합
class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend


# Bank 클래스 - "Fake It" 하드코딩
class Bank:
    def reduce(self, source: Expression, to_currency: str) -> Money:
        """Fake It: 하드코딩된 값 반환

        test_simple_addition을 통과시키기 위한 최소 구현.
        $5 + $5 = $10 이므로 그냥 10을 반환!
        """
        return Money.dollar(10)
