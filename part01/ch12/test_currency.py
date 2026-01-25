from part01.ch12.currency import Bank, Money, Sum


class TestMoney:
    def test_multiplication(self):
        five = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_franc_multiplication(self):
        five = Money.franc(5)
        assert Money.franc(10) == five.times(2)
        assert Money.franc(15) == five.times(3)

    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.franc(5) == Money.franc(5)
        assert Money.franc(5) != Money.franc(6)
        assert Money.dollar(5) != Money.franc(5)

    def test_currency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()

    # Chapter 12: 덧셈 테스트
    def test_simple_addition(self):
        five = Money.dollar(5)
        sum_result = five.plus(Money.dollar(5))
        bank = Bank()
        reduced = bank.reduce(sum_result, "USD")
        assert Money.dollar(10) == reduced

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        result = five.plus(Money.dollar(5))
        assert isinstance(result, Sum)
        assert five == result.augend
        assert Money.dollar(5) == result.addend

    def test_reduce_sum(self):
        sum_result = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_result, "USD")
        assert Money.dollar(7) == result
