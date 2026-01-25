from part01.ch12.currency import Bank, Sum, dollar, franc


class TestMoney:
    def test_multiplication(self):
        five = dollar(5)
        assert dollar(10) == five.times(2)
        assert dollar(15) == five.times(3)

    def test_franc_multiplication(self):
        five = franc(5)
        assert franc(10) == five.times(2)
        assert franc(15) == five.times(3)

    def test_equality(self):
        assert dollar(5) == dollar(5)
        assert dollar(5) != dollar(6)
        assert franc(5) == franc(5)
        assert franc(5) != franc(6)
        assert dollar(5) != franc(5)

    def test_currency(self):
        assert "USD" == dollar(1).currency()
        assert "CHF" == franc(1).currency()

    # Chapter 12: 덧셈 테스트
    def test_simple_addition(self):
        five = dollar(5)
        sum_result = five.plus(dollar(5))
        bank = Bank()
        reduced = bank.reduce(sum_result, "USD")
        assert dollar(10) == reduced

    def test_plus_returns_sum(self):
        five = dollar(5)
        result = five.plus(dollar(5))
        assert isinstance(result, Sum)
        assert five == result.augend
        assert dollar(5) == result.addend

    def test_reduce_sum(self):
        sum_result = Sum(dollar(3), dollar(4))
        bank = Bank()
        result = bank.reduce(sum_result, "USD")
        assert dollar(7) == result
