from part01.ch07.currency import Dollar, Franc


class TestDollar:
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
        assert Dollar(5) != Franc(5)


class TestFranc:
    def test_franc_multiplication(self):
        five = Franc(5)
        assert Franc(10) == five.times(2)
        assert Franc(15) == five.times(3)

    def test_equality(self):
        assert Franc(5) == Franc(5)
        assert Franc(5) != Franc(6)
