"""Pluggable Object 패턴 - 조건문 대신 다형성 사용"""

from abc import ABC, abstractmethod


class SelectionMode(ABC):
    """선택 모드 인터페이스"""

    @abstractmethod
    def select(self, items: list, start: int, end: int) -> list:
        pass


class SingleSelection(SelectionMode):
    """단일 선택"""

    def select(self, items: list, start: int, end: int) -> list:
        return [items[start]] if start < len(items) else []


class RangeSelection(SelectionMode):
    """범위 선택"""

    def select(self, items: list, start: int, end: int) -> list:
        return items[start : end + 1]


class Editor:
    """에디터 - 선택 모드를 플러그인"""

    def __init__(self, mode: SelectionMode | None = None):
        self.mode = mode or SingleSelection()
        self.items: list = []

    def set_mode(self, mode: SelectionMode):
        self.mode = mode

    def select(self, start: int, end: int) -> list:
        # if-else 없이 다형성으로 처리
        return self.mode.select(self.items, start, end)
