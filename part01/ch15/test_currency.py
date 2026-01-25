from part01.ch15.currency import dollar, franc, Bank


class TestMoney:
    def test_multiplication(self):
        five = dollar(5)
        assert dollar(10) == five.times(2)
        assert dollar(15) == five.times(3)

    def test_equality(self):
        assert dollar(5) == dollar(5)
        assert dollar(5) != dollar(6)
        assert dollar(5) != franc(5)

    def test_currency(self):
        assert "USD" == dollar(1).currency()
        assert "CHF" == franc(1).currency()

    def test_simple_addition(self):
        five = dollar(5)
        sum_result = five.plus(dollar(5))
        bank = Bank()
        reduced = bank.reduce(sum_result, "USD")
        assert dollar(10) == reduced

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(franc(2), "USD")
        assert dollar(1) == result

    # Chapter 15: 다중 통화 덧셈 테스트
    def test_mixed_addition(self):
        five_bucks = dollar(5)
        ten_francs = franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        assert dollar(10) == result

    def test_sum_plus_money(self):
        five_bucks = dollar(5)
        ten_francs = franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum_result = five_bucks.plus(ten_francs).plus(dollar(5))
        result = bank.reduce(sum_result, "USD")
        assert dollar(15) == result

    def test_sum_times(self):
        five_bucks = dollar(5)
        ten_francs = franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum_result = five_bucks.plus(ten_francs).times(2)
        result = bank.reduce(sum_result, "USD")
        assert dollar(20) == result
