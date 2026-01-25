from part01.ch03.currency import Dollar


class TestDollar:
    # Chapter 2: 곱셈 테스트 (immutability 암묵적 검증)
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount

    # Chapter 3: 동등성 테스트
    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
