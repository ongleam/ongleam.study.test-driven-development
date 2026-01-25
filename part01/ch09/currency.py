from __future__ import annotations

from abc import ABC, abstractmethod


# Money 추상 클래스 - 통화 개념 추가
class Money(ABC):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self) -> int:
        return hash((self._amount, type(self)))

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        """추상 메서드 - 하위 클래스에서 구현"""
        pass

    # 팩토리 메서드
    @staticmethod
    def dollar(amount: int) -> Dollar:
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Franc:
        return Franc(amount)


# Dollar 클래스
class Dollar(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount, "USD")

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)


# Franc 클래스
class Franc(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount, "CHF")

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)
