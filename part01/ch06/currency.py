from __future__ import annotations


# Money 상위 클래스 - 공통 동등성 비교
class Money:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other: object) -> bool:
        # 동등성 비교를 상위 클래스로 이동
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount

    def __hash__(self) -> int:
        return hash(self._amount)


# Dollar 클래스 - Money 상속
class Dollar(Money):
    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)


# Franc 클래스 - Money 상속
class Franc(Money):
    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)
