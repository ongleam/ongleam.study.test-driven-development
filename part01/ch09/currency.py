from abc import ABC, abstractmethod


# Money 추상 클래스 - 통화 개념 추가
class Money(ABC):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))

    @abstractmethod
    def times(self, multiplier):
        """추상 메서드 - 하위 클래스에서 구현"""
        pass

    # 팩토리 메서드
    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


# Dollar 클래스
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


# Franc 클래스
class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount, "CHF")

    def times(self, multiplier):
        return Franc(self._amount * multiplier)
