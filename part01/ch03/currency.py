# Dollar 클래스 - 동등성 비교 추가
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return False
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)
