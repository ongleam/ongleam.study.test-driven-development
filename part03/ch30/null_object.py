"""Null Object 패턴 - 객체의 부재를 특수 객체로 표현"""

from abc import ABC, abstractmethod


class Logger(ABC):
    """로거 인터페이스"""

    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    """콘솔 로거"""

    def __init__(self):
        self.messages: list[str] = []

    def log(self, message: str) -> None:
        self.messages.append(message)
        print(message)


class NullLogger(Logger):
    """널 로거 - 아무것도 하지 않음"""

    def log(self, message: str) -> None:
        pass  # 의도적으로 아무것도 안 함


class Calculator:
    """로거를 사용하는 계산기"""

    def __init__(self, logger: Logger | None = None):
        self.logger = logger or NullLogger()  # None이면 NullLogger

    def add(self, a: int, b: int) -> int:
        result = a + b
        self.logger.log(f"add({a}, {b}) = {result}")
        return result

    def subtract(self, a: int, b: int) -> int:
        result = a - b
        self.logger.log(f"subtract({a}, {b}) = {result}")
        return result
