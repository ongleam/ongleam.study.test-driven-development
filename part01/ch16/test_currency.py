from part01.ch16.currency import Bank, Money, Sum


class TestMoney:
    """Part 1: The Money Example - 완성된 테스트 스위트"""

    # 기본 연산 테스트
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

    # 덧셈 테스트
    def test_simple_addition(self):
        five = Money.dollar(5)
        sum_result = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_result, "USD")
        assert Money.dollar(10) == reduced

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        assert five == result.augend
        assert five == result.addend

    def test_reduce_sum(self):
        sum_expr = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_expr, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result

    # 환율 변환 테스트
    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result

    def test_identity_rate(self):
        bank = Bank()
        assert 1 == bank.rate("USD", "USD")

    # 혼합 통화 테스트
    def test_mixed_addition(self):
        """$5 + 10 CHF = $10 (환율 2:1)

        Part 1의 최종 목표!
        """
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        assert Money.dollar(10) == result

    # Chapter 16: Abstraction, Finally - Sum.plus, Expression.times

    def test_sum_plus_money(self):
        """Sum.plus: ($5 + 10 CHF) + $5 = $15"""
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum_expr = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(sum_expr, "USD")
        assert Money.dollar(15) == result

    def test_sum_times(self):
        """Expression.times: ($5 + 10 CHF) * 2 = $20"""
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum_expr = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum_expr, "USD")
        assert Money.dollar(20) == result
