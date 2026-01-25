from part01.ch10_interesting_times.currency import dollar, franc


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
