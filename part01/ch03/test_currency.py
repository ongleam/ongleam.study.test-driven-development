from part01.ch03.currency import Dollar


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
        assert 5 == five.amount

    # Chapter 3: 동등성 테스트
    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
        assert not (Dollar(5) == Dollar(6))
