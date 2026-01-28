"""Factory Method 패턴 - 객체 생성을 별도 메서드로 분리"""

from abc import ABC, abstractmethod


class Money(ABC):
    """통화 추상 클래스"""

    def __init__(self, amount: int):
        self._amount = amount

    @property
    def amount(self) -> int:
        return self._amount

    @abstractmethod
    def currency(self) -> str:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> "Money":
        pass

    # 팩토리 메서드
    @staticmethod
    def dollar(amount: int) -> "Money":
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> "Money":
        return Franc(amount)


class Dollar(Money):
    """달러"""

    def currency(self) -> str:
        return "USD"

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    """프랑"""

    def currency(self) -> str:
        return "CHF"

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
