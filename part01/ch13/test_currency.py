from part01.ch13.currency import Bank, Money, Sum


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

    # Chapter 13: "Make It" - 새 테스트들

    def test_plus_returns_sum(self):
        """plus()가 Sum 객체를 반환하는지 확인"""
        five = Money.dollar(5)
        result = five.plus(five)
        assert five == result.augend
        assert five == result.addend

    def test_reduce_sum(self):
        """Sum을 reduce하면 실제 합계가 나오는지 확인

        이 테스트로 Fake It($10 하드코딩)을 실제 구현으로 전환!
        """
        sum_expr = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_expr, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        """Money를 reduce하면 그대로 반환되는지 확인

        다형성: Bank.reduce()가 Money에도 작동해야 함
        """
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result
