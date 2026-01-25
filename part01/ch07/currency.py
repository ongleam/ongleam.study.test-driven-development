# Dollar 클래스
class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, other):
        # type()을 사용하여 정확한 타입 비교
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))


# Franc 클래스
class Franc:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, other):
        # type()을 사용하여 정확한 타입 비교
        return self._amount == other._amount and type(self) == type(other)

    def __hash__(self):
        return hash((self._amount, type(self)))
