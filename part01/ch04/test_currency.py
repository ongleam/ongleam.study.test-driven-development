from part01.ch04.currency import Dollar


class TestDollar:
    # Chapter 1-4: 곱셈 테스트 (동등성 사용으로 개선)
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    # Chapter 3: 동등성 테스트
    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
