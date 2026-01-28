"""Composite 패턴 - 개별 객체와 컬렉션을 동일하게 취급"""

from abc import ABC, abstractmethod


class TestResult:
    """테스트 결과"""

    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, {self.failure_count} failed"


class Component(ABC):
    """컴포넌트 인터페이스"""

    @abstractmethod
    def run(self, result: TestResult | None = None) -> TestResult:
        pass


class TestCase(Component):
    """개별 테스트 케이스"""

    def __init__(self, name: str):
        self.name = name

    def run(self, result: TestResult | None = None) -> TestResult:
        result = result or TestResult()
        result.test_started()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        return result


class TestSuite(Component):
    """테스트 스위트 - 컴포지트"""

    def __init__(self):
        self.tests: list[Component] = []

    def add(self, test: Component):
        self.tests.append(test)

    def run(self, result: TestResult | None = None) -> TestResult:
        result = result or TestResult()
        for test in self.tests:
            test.run(result)  # TestCase든 TestSuite든 동일하게 호출
        return result
