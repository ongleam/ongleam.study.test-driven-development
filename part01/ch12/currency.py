# Chapter 12: Addition, Finally
# "Fake It" 패턴 - stub으로 시작하여 테스트 통과
#
# TDD 진행 과정:
# 1. test_simple_addition 작성
# 2. Fake It: Bank.reduce()가 하드코딩된 값 반환
# 3. 점진적으로 실제 구현으로 발전
#
# 이 챕터의 목표: $5 + $5 = $10 동작하게 만들기


# Expression 인터페이스 (마커 클래스)
class Expression:
    """Expression은 금액 계산을 나타내는 인터페이스.
    아직 reduce() 메서드 없음 - Chapter 13에서 추가 예정.
    """

    pass


# Money 클래스 - Expression 구현
class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        """덧셈 - Sum 반환 (지연 평가)
        아직 계산하지 않고 Sum 객체만 생성.
        """
        return Sum(self, addend)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    def __hash__(self):
        return hash((self._amount, self._currency))

    def __repr__(self):
        return f"Money({self._amount}, '{self._currency}')"

    # 팩토리 메서드
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


# Sum 클래스 - 두 Expression의 합
# 아직 reduce() 메서드 없음 - Chapter 13에서 추가 예정
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend  # 피가산수
        self.addend = addend  # 가산수


# Bank 클래스 - "Fake It" stub 구현
# 다형성 없이 isinstance()로 타입 체크 (Chapter 13에서 개선 예정)
class Bank:
    def reduce(self, source, to_currency):
        """Stub 구현: isinstance()로 타입 체크

        이 구현의 문제점:
        - Bank가 모든 Expression 타입을 알아야 함
        - 새 Expression 타입 추가 시 Bank 수정 필요
        - Chapter 13에서 다형성으로 개선
        """
        if isinstance(source, Money):
            return source
        if isinstance(source, Sum):
            # Fake: 같은 통화라고 가정하고 단순 합산
            amount = source.augend._amount + source.addend._amount
            return Money(amount, to_currency)
        return source
