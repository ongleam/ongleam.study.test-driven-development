"""Collecting Parameter 패턴 - 결과를 수집할 객체를 매개변수로 전달"""


class TestResult:
    """수집 매개변수"""

    def __init__(self):
        self.run_count = 0
        self.failure_count = 0
        self.errors: list[str] = []

    def test_started(self):
        self.run_count += 1

    def test_failed(self, error: str | None = None):
        self.failure_count += 1
        if error:
            self.errors.append(error)

    def summary(self) -> str:
        return f"{self.run_count} run, {self.failure_count} failed"


class TestCase:
    """테스트 케이스"""

    def __init__(self, name: str):
        self.name = name

    def run(self, result: TestResult) -> TestResult:
        """result를 수집 매개변수로 받음"""
        result.test_started()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.test_failed(str(e))
        return result


class TestSuite:
    """테스트 스위트"""

    def __init__(self):
        self.tests: list[TestCase] = []

    def add(self, test: TestCase):
        self.tests.append(test)

    def run(self, result: TestResult) -> TestResult:
        """동일한 result를 모든 테스트에 전달"""
        for test in self.tests:
            test.run(result)  # 결과가 누적됨
        return result
