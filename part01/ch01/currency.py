# Dollar 클래스 - Chapter 1: 최소 구현 (side effect 있음)
class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        # side effect: 객체 자체를 수정
        self.amount *= multiplier
