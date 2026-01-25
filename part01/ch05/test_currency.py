from part01.ch05_franc_ly_speaking.currency import Dollar, Franc


class TestDollar:
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)


class TestFranc:
    # Chapter 5: Franc 곱셈 테스트
    def test_franc_multiplication(self):
        five = Franc(5)
        assert Franc(10) == five.times(2)
        assert Franc(15) == five.times(3)

    def test_equality(self):
        assert Franc(5) == Franc(5)
        assert Franc(5) != Franc(6)
