from __future__ import annotations

from abc import ABC, abstractmethod

# Chapter 16: Abstraction, Finally
# Part 1 완성 - 모든 TODO 항목 완료
#
# Kent Beck: "We have finished with the first example. Let's look
# back and review what we've done."


# Expression 인터페이스 - 완전한 추상화
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """Expression을 단일 통화로 환산"""
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        """두 Expression의 합"""
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        """Expression에 배수 적용"""
        pass


# Money 클래스 - Expression 구현
class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount // rate, to_currency)

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


# Sum 클래스 - Expression 구현
class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        amount = (
            self.augend.reduce(bank, to_currency)._amount
            + self.addend.reduce(bank, to_currency)._amount
        )
        return Money(amount, to_currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


# Pair 클래스 - 환율 키
class Pair:
    def __init__(self, from_currency: str, to_currency: str) -> None:
        self._from = from_currency
        self._to = to_currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pair):
            return False
        return self._from == other._from and self._to == other._to

    def __hash__(self) -> int:
        return hash((self._from, self._to))


# Bank 클래스 - 환율 관리
class Bank:
    def __init__(self) -> None:
        self._rates: dict[Pair, int] = {}

    def reduce(self, source: Expression, to_currency: str) -> Money:
        return source.reduce(self, to_currency)

    def add_rate(self, from_currency: str, to_currency: str, rate: int) -> None:
        self._rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency:
            return 1
        return self._rates[Pair(from_currency, to_currency)]
