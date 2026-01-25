from part01.ch01_multiplication.currency import Dollar


class TestDollar:
    # Chapter 1: 곱셈 테스트
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount
