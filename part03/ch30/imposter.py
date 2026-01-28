"""Imposter 패턴 - 기존 객체처럼 행동하는 다른 객체"""

from abc import ABC, abstractmethod


class Expression(ABC):
    """표현식 인터페이스"""

    @abstractmethod
    def reduce(self, bank: "Bank", to_currency: str) -> "Money":
        pass

    @abstractmethod
    def plus(self, addend: "Expression") -> "Expression":
        pass


class Money(Expression):
    """단일 금액 - 표현식처럼 행동"""

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self) -> int:
        return self._amount

    def currency(self) -> str:
        return self._currency

    def reduce(self, bank: "Bank", to_currency: str) -> "Money":
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount // rate, to_currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency


class Sum(Expression):
    """합계 - Money처럼 행동하는 사칭꾼"""

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: "Bank", to_currency: str) -> Money:
        amount = self.augend.reduce(bank, to_currency).amount + self.addend.reduce(
            bank, to_currency
        ).amount
        return Money(amount, to_currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)


class Bank:
    """환율 관리"""

    def __init__(self):
        self.rates: dict[tuple[str, str], int] = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: int):
        self.rates[(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency:
            return 1
        return self.rates.get((from_currency, to_currency), 1)
