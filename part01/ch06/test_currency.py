from part01.ch06.currency import Dollar, Franc


class TestMoney:
    def test_dollar_multiplication(self):
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
        # Money 상위 클래스 도입 후 발생하는 문제!
        # Dollar(5)와 Franc(5)가 같다고 판단됨 (버그)
        assert Dollar(5) == Franc(5)  # 버그! 다른 통화인데 같다고 판단됨
        assert Franc(5) == Dollar(5)  # 버그! 다른 통화인데 같다고 판단됨
        # 이 문제는 다음 챕터 "Apples and Oranges"에서 해결
