import pytest

from part01.currency import dollar, won


class TestMoney:
    # 곱셈 테스트
    def test_multiplication(self):
        five = dollar(5)
        assert dollar(10) == five.times(2)
        assert dollar(15) == five.times(3)

    # 동등성 테스트
    def test_equality(self):
        assert dollar(5) == dollar(5)
        assert dollar(5) != dollar(6)
        assert dollar(5) != won(5)

    # 통화 테스트
    def test_currency(self):
        assert "USD" == dollar(1).currency()
        assert "KRW" == won(1).currency()

    # 덧셈 테스트 - 같은 통화
    def test_simple_addition(self):
        five = dollar(5)
        ten = five.plus(dollar(5))
        assert dollar(10) == ten

    # 덧셈 테스트 - 다른 통화 (실패해야 함)
    def test_addition_different_currency(self):
        with pytest.raises(ValueError, match="통화가 다른 경우 더할 수 없습니다"):
            dollar(5).plus(won(5000))

    # amount 메서드 테스트
    def test_amount(self):
        five = dollar(5)
        assert 5 == five.amount()

    # 원화 곱셈 테스트
    def test_won_multiplication(self):
        ten_thousand = won(10000)
        assert won(20000) == ten_thousand.times(2)
        assert won(30000) == ten_thousand.times(3)

    # repr 테스트
    def test_repr(self):
        five_dollars = dollar(5)
        assert "5 USD" == repr(five_dollars)

        ten_thousand_won = won(10000)
        assert "10000 KRW" == repr(ten_thousand_won)
