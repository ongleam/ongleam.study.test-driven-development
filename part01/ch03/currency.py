# Dollar 클래스 - 동등성 비교 추가
class Dollar:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, other):
        # 동등성 비교 구현
        if not isinstance(other, Dollar):
            return False
        return self._amount == other._amount

    def __hash__(self):
        # __eq__를 구현하면 __hash__도 구현해야 함
        return hash(self._amount)
