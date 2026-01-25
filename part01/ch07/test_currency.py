from part01.ch07.currency import Dollar, Franc


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    def test_franc_multiplication(self):
        five = Franc(5)
        assert Franc(10) == five.times(2)
        assert Franc(15) == five.times(3)

    def test_equality(self):
        # Dollar 동등성
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
        # Franc 동등성
        assert Franc(5) == Franc(5)
        assert Franc(5) != Franc(6)
        # Chapter 7: "Apples and Oranges" - 문제 해결!
        # getClass() 비교 추가로 Dollar != Franc
        assert Dollar(5) != Franc(5)  # 이제 통과!
        assert Franc(5) != Dollar(5)  # 이제 통과!
