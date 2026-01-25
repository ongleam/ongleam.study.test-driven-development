from __future__ import annotations

from abc import ABC, abstractmethod

# Chapter 15: Mixed Currencies
# 서로 다른 통화의 덧셈
#
# Kent Beck: "$5 + 10 CHF = $10 if rate is 2:1"
# Sum.reduce()에서 각 피연산자를 먼저 reduce해야 함


# Expression 인터페이스
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


# Money 클래스
class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        """덧셈 - Sum 반환"""
        return Sum(self, addend)

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """통화 변환하여 반환"""
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


# Sum 클래스 - 혼합 통화 지원
class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """각 피연산자를 먼저 reduce 후 합산

        Chapter 14: amount = self.augend._amount + self.addend._amount
                    (통화 변환 없이 단순 합산 - 같은 통화만 가능)

        Chapter 15: 각각 reduce하여 통화 변환 후 합산
                    ($5 + 10 CHF → $5 + $5 → $10)
        """
        amount = (
            self.augend.reduce(bank, to_currency)._amount
            + self.addend.reduce(bank, to_currency)._amount
        )
        return Money(amount, to_currency)

    def plus(self, addend: Expression) -> Expression:
        """Sum + Expression = 새로운 Sum"""
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        """Sum의 각 피연산자에 배수 적용"""
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


# Pair 클래스 - 환율 키로 사용
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


# Bank 클래스
class Bank:
    def __init__(self) -> None:
        self._rates: dict[Pair, int] = {}

    def reduce(self, source: Expression, to_currency: str) -> Money:
        """Expression을 지정 통화로 환산"""
        return source.reduce(self, to_currency)

    def add_rate(self, from_currency: str, to_currency: str, rate: int) -> None:
        """환율 등록"""
        self._rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        """환율 조회"""
        if from_currency == to_currency:
            return 1
        return self._rates[Pair(from_currency, to_currency)]
