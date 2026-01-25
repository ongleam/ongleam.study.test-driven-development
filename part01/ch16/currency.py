from abc import ABC, abstractmethod


# Expression 인터페이스 (추상 클래스)
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to_currency):
        pass

    @abstractmethod
    def plus(self, addend):
        pass

    @abstractmethod
    def times(self, multiplier):
        pass


# Money 클래스
class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to_currency):
        rate = bank.rate(self._currency, to_currency)
        return Money(self._amount / rate, to_currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))

    def __repr__(self):
        return f"Money({self._amount}, {self._currency})"


# Sum 클래스
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to_currency):
        amount = (
            self.augend.reduce(bank, to_currency)._amount
            + self.addend.reduce(bank, to_currency)._amount
        )
        return Money(amount, to_currency)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


# Bank 클래스
class Bank:
    def __init__(self):
        self._rates = {}

    def add_rate(self, from_currency, to_currency, rate):
        key = (from_currency, to_currency)
        self._rates[key] = rate

    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        key = (from_currency, to_currency)
        return self._rates.get(key, 1)

    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)


# 팩토리 함수
def dollar(amount):
    return Money(amount, "USD")


def franc(amount):
    return Money(amount, "CHF")
