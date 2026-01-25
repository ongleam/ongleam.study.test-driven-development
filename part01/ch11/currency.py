# Money 클래스 - 통화만으로 구분
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        # 동일한 통화로 새 Money 객체 생성
        return Money(self._amount * multiplier, self._currency)

    def __eq__(self, other):
        # 타입이 아닌 통화로 비교
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))


# 팩토리 함수
def dollar(amount):
    return Money(amount, "USD")


def franc(amount):
    return Money(amount, "CHF")
