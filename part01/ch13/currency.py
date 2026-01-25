from __future__ import annotations

# Chapter 13: Make It
# Expression.reduce() 다형성 구현 - isinstance() 제거


# Expression 인터페이스
class Expression:
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """Expression을 단일 통화 Money로 변환"""
        raise NotImplementedError


# Money 클래스
class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Sum:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        # Money 자체를 reduce하면 그대로 반환 (같은 통화 가정)
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


# Sum 클래스
class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        # 각 항을 reduce한 후 합산 (재귀적)
        amount = (
            self.augend.reduce(bank, to_currency)._amount
            + self.addend.reduce(bank, to_currency)._amount
        )
        return Money(amount, to_currency)


# Bank 클래스
class Bank:
    def reduce(self, source: Expression, to_currency: str) -> Money:
        # 다형성: Expression의 reduce 메서드 호출
        # isinstance() 체크 없이 동작
        return source.reduce(self, to_currency)
