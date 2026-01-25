# Dollar 클래스 - Chapter 1: 최소 구현 (side effect 있음)
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # side effect: 객체 자체를 수정
        self.amount *= multiplier
