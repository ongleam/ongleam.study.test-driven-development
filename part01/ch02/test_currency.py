from part01.ch02_degenerate_objects.currency import Dollar


class TestDollar:
    # Chapter 1: 곱셈 테스트
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount

    # Chapter 2: 불변성 테스트
    def test_immutability(self):
        five = Dollar(5)
        five.times(2)
        # five는 변경되지 않아야 함
        assert 5 == five.amount
