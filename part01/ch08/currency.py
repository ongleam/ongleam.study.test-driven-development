# Money 상위 클래스
class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))


# Dollar 클래스 - Money 상속
class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


# Franc 클래스 - Money 상속
class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)


# 팩토리 함수
def dollar(amount):
    return Dollar(amount)


def franc(amount):
    return Franc(amount)
