"""Value Object 패턴 - 불변 값 객체"""


class Money:
    """불변 값 객체"""

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self) -> int:
        return hash((self._amount, self._currency))

    def __repr__(self) -> str:
        return f"Money({self._amount}, '{self._currency}')"

    def times(self, multiplier: int) -> "Money":
        """새로운 Money 객체 반환 (불변성 유지)"""
        return Money(self._amount * multiplier, self._currency)

    def plus(self, other: "Money") -> "Money":
        """같은 통화끼리 덧셈"""
        if self._currency != other._currency:
            raise ValueError("Currency mismatch")
        return Money(self._amount + other._amount, self._currency)
