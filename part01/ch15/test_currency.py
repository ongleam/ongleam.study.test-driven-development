from part01.ch15.currency import Bank, Money, Sum


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
        assert Money.dollar(5) != Money.franc(5)

    def test_currency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum_result = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_result, "USD")
        assert Money.dollar(10) == reduced

    def test_plus_returns_sum(self):
        """plus()가 Sum 객체를 반환하는지 확인"""
        five = Money.dollar(5)
        result = five.plus(five)
        assert five == result.augend
        assert five == result.addend

    def test_reduce_sum(self):
        """Sum을 reduce하면 실제 합계가 나오는지 확인"""
        sum_expr = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_expr, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        """Money를 reduce하면 그대로 반환되는지 확인"""
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result

    def test_reduce_money_different_currency(self):
        """다른 통화 변환: 2 CHF = 1 USD"""
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result

    def test_identity_rate(self):
        """같은 통화 환율은 1"""
        bank = Bank()
        assert 1 == bank.rate("USD", "USD")

    # Chapter 15: Mixed Currencies - 핵심 테스트!

    def test_mixed_addition(self):
        """혼합 통화 덧셈: $5 + 10 CHF = $10 (환율 2:1)

        이것이 Part 1의 최종 목표였던 테스트!
        """
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        assert Money.dollar(10) == result
