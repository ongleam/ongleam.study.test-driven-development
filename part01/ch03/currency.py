from __future__ import annotations


# Dollar 클래스 - 동등성 비교 추가
class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dollar):
            return False
        return self.amount == other.amount

    def __hash__(self) -> int:
        return hash(self.amount)
