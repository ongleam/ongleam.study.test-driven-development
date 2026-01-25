# Expression 인터페이스
class Expression:
    def reduce(self, bank, to_currency):
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
        # Money 자체를 reduce하면 그대로 반환 (같은 통화 가정)
        return self

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))


# Sum 클래스
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to_currency):
        # 각 항을 reduce한 후 합산
        amount = (
            self.augend.reduce(bank, to_currency)._amount
            + self.addend.reduce(bank, to_currency)._amount
        )
        return Money(amount, to_currency)


# Bank 클래스
class Bank:
    def reduce(self, source, to_currency):
        # Expression의 reduce 메서드 호출
        return source.reduce(self, to_currency)


# 팩토리 함수
def dollar(amount):
    return Money(amount, "USD")


def franc(amount):
    return Money(amount, "CHF")
