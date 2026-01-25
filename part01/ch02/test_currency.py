from part01.ch02.currency import Dollar


class TestDollar:
    # Chapter 2: 곱셈 테스트 (새 객체 반환 버전)
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount
