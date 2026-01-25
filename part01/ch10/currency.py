# Money 상위 클래스 - times() 메서드 통합
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        # 팩토리 함수를 사용하여 올바른 타입 반환
        if self._currency == "USD":
            return dollar(self._amount * multiplier)
        elif self._currency == "CHF":
            return franc(self._amount * multiplier)

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))


# Dollar 클래스
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")


# Franc 클래스
class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount, "CHF")


# 팩토리 함수
def dollar(amount):
    return Dollar(amount)


def franc(amount):
    return Franc(amount)
