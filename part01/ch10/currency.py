from __future__ import annotations


# Money 클래스 - times() 통합
# Chapter 10: Money가 concrete 클래스가 되어 직접 인스턴스화 가능
class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        # Money를 직접 반환 - Dollar/Franc 구분 불필요
        return Money(self._amount * multiplier, self._currency)

    def __eq__(self, other: object) -> bool:
        # Chapter 10: currency 기반 비교로 변경 (type 비교 제거)
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self) -> int:
        return hash((self._amount, self._currency))

    def __repr__(self) -> str:
        return f"Money({self._amount}, '{self._currency}')"

    # 팩토리 메서드
    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")


# Dollar와 Franc은 이제 불필요하지만 호환성을 위해 유지
# 다음 챕터에서 제거 예정
class Dollar(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount, "USD")


class Franc(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount, "CHF")
