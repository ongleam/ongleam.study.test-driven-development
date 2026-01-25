from __future__ import annotations

from abc import ABC, abstractmethod

# Chapter 14: Change
# 환율 변환 기능 추가
#
# Kent Beck: "2 CHF = 1 USD"
# Bank에 환율을 등록하고, reduce()에서 변환


# Expression 인터페이스
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """Expression을 단일 통화로 환산"""
        pass


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
        """덧셈 - Sum 반환"""
        return Sum(self, addend)

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """통화 변환하여 반환

        Chapter 13: return self (변환 없음)
        Chapter 14: Bank에서 환율 조회하여 변환
        """
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


# Sum 클래스
class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to_currency: str) -> Money:
        """augend + addend 의 실제 합계 반환"""
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to_currency)


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


# Bank 클래스 - 환율 관리 추가
class Bank:
    def __init__(self) -> None:
        self._rates: dict[Pair, int] = {}

    def reduce(self, source: Expression, to_currency: str) -> Money:
        """Expression을 지정 통화로 환산"""
        return source.reduce(self, to_currency)

    def add_rate(self, from_currency: str, to_currency: str, rate: int) -> None:
        """환율 등록

        예: add_rate("CHF", "USD", 2) → 2 CHF = 1 USD
        """
        self._rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        """환율 조회

        같은 통화면 1 반환 (변환 불필요)
        """
        if from_currency == to_currency:
            return 1
        return self._rates[Pair(from_currency, to_currency)]
