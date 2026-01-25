# Chapter 12: Addition, Finally
# Expression 인터페이스와 Sum 클래스 도입


# Expression 인터페이스 (마커 클래스)
class Expression:
    """Expression은 금액 계산을 나타내는 인터페이스.
    단순한 Money일 수도 있고, Sum 같은 복합 표현식일 수도 있음.
    """

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
        """덧셈 - Sum 반환 (지연 평가)"""
        return Sum(self, addend)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))

    def __repr__(self):
        return f"Money({self._amount}, '{self._currency}')"

    # 팩토리 메서드
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


# Sum 클래스 - 두 Expression의 합 (Composite 패턴)
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend  # 피가산수
        self.addend = addend  # 가산수


# Bank 클래스 - Expression을 Money로 변환 (reduce)
class Bank:
    def reduce(self, source, to_currency):
        """Expression을 단일 통화 Money로 변환"""
        if isinstance(source, Money):
            return source
        if isinstance(source, Sum):
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)
        return source
