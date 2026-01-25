# Money 상위 클래스 - 통화 개념 추가
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))


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


# 팩토리 함수
def dollar(amount):
    return Dollar(amount)


def franc(amount):
    return Franc(amount)
