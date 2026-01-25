from part01.ch10.currency import Money


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
        # 같은 통화, 같은 금액
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.franc(5) == Money.franc(5)
        assert Money.franc(5) != Money.franc(6)
        # 다른 통화는 같은 금액이라도 다름
        assert Money.dollar(5) != Money.franc(5)

    def test_currency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()
