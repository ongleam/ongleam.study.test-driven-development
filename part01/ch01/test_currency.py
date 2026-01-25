from part01.ch01.currency import Dollar


class TestDollar:
    # Chapter 1: 곱셈 테스트 (side effect 버전)
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount
