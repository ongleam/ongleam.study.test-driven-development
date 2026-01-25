from part01.ch14_change.currency import dollar, franc, Bank, Sum


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

    def test_reduce_sum(self):
        sum_result = Sum(dollar(3), dollar(4))
        bank = Bank()
        result = bank.reduce(sum_result, "USD")
        assert dollar(7) == result

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(dollar(1), "USD")
        assert dollar(1) == result

    # Chapter 14: 환율 변환 테스트
    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(franc(2), "USD")
        assert dollar(1) == result

    def test_identity_rate(self):
        # 같은 통화는 환율 1
        bank = Bank()
        assert 1 == bank.rate("USD", "USD")
