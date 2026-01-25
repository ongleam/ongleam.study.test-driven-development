from part01.ch02.currency import Dollar


class TestDollar:
    # Chapter 2: 곱셈 테스트 (같은 객체로 두 번 곱셈 → immutability 암묵적 검증)
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)  # side effect 없으면 15, 있으면 30
        assert 15 == product.amount
