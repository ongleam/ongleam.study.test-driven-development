# Dollar 클래스 - amount를 완전히 private으로
class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return False
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)
