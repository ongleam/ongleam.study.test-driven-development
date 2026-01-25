# Dollar 클래스 - 불변 객체로 변경
class Dollar:
    def __init__(self, amount):
        self._amount = amount  # private 변수로 변경

    @property
    def amount(self):
        return self._amount

    def times(self, multiplier):
        # 새로운 Dollar 객체를 반환 (불변성 유지)
        return Dollar(self._amount * multiplier)
