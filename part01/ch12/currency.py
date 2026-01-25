# Expression 인터페이스 (추상 클래스)
class Expression:
    pass


# Money 클래스 - Expression 구현
class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        # 덧셈은 Sum 반환
        return Sum(self, addend)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))


# Sum 클래스 - 두 Expression의 합
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend


# Bank 클래스 - Expression을 Money로 변환
class Bank:
    def reduce(self, source, to_currency):
        # 간단한 경우: Money를 그대로 반환
        if isinstance(source, Money):
            return source
        # Sum의 경우: 두 Money를 더함
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)


# 팩토리 함수
def dollar(amount):
    return Money(amount, "USD")


def franc(amount):
    return Money(amount, "CHF")
