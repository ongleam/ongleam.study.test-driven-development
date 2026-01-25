from __future__ import annotations


# Dollar 클래스 - Chapter 2: Degenerate Objects (side effect 제거)
class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        # side effect 제거: 새 Dollar 객체 반환
        return Dollar(self.amount * multiplier)
