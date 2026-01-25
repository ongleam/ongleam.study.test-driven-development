from __future__ import annotations


# Dollar 클래스
class Dollar:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dollar):
            return False
        return self._amount == other._amount

    def __hash__(self) -> int:
        return hash(self._amount)


# Franc 클래스 (Dollar와 동일한 구조)
class Franc:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Franc):
            return False
        return self._amount == other._amount

    def __hash__(self) -> int:
        return hash(self._amount)
