"""Chapter 23: How Suite It Is

TestSuite 클래스를 도입하여 여러 테스트를 함께 실행.
Composite 패턴 적용.
"""


class TestResult:
    """테스트 결과를 수집하는 클래스"""

    def __init__(self) -> None:
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self) -> None:
        """테스트 시작 시 호출"""
        self.runCount = self.runCount + 1

    def testFailed(self) -> None:
        """테스트 실패 시 호출"""
        self.failureCount = self.failureCount + 1

    def summary(self) -> str:
        """테스트 결과 요약 반환"""
        return f"{self.runCount} run, {self.failureCount} failed"


class TestCase:
    """xUnit 테스트 케이스 기본 클래스"""

    def __init__(self, name: str) -> None:
        """테스트 메서드 이름을 저장

        Args:
            name: 실행할 테스트 메서드의 이름
        """
        self.name = name

    def setUp(self) -> None:
        """테스트 픽스처 설정 (서브클래스에서 오버라이드)"""
        pass

    def tearDown(self) -> None:
        """테스트 후 정리 작업 (서브클래스에서 오버라이드)"""
        pass

    def run(self, result: TestResult | None = None) -> TestResult:
        """setUp -> 테스트 메서드 -> tearDown 순서로 실행

        Args:
            result: 테스트 결과를 수집할 객체 (없으면 새로 생성)
        """
        if result is None:
            result = TestResult()
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result


class TestSuite:
    """여러 테스트를 함께 실행하는 테스트 스위트"""

    def __init__(self) -> None:
        self.tests: list[TestCase] = []

    def add(self, test: TestCase) -> None:
        """테스트를 스위트에 추가"""
        self.tests.append(test)

    def run(self, result: TestResult | None = None) -> TestResult:
        """모든 테스트 실행

        Args:
            result: 테스트 결과를 수집할 객체 (없으면 새로 생성)
        """
        if result is None:
            result = TestResult()
        for test in self.tests:
            test.run(result)
        return result


class WasRun(TestCase):
    """테스트 실행 여부와 setUp/tearDown 호출을 확인하는 테스트용 클래스"""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: int | None = None
        self.wasSetUp: int | None = None
        self.wasTornDown: int | None = None
        self.log = ""

    def setUp(self) -> None:
        """setUp 호출 기록"""
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "

    def testMethod(self) -> None:
        """테스트 메서드 호출 기록"""
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def tearDown(self) -> None:
        """tearDown 호출 기록"""
        self.wasTornDown = 1
        self.log = self.log + "tearDown "

    def testBrokenMethod(self) -> None:
        """실패하는 테스트 메서드"""
        raise Exception


class WasRunWithBrokenSetUp(TestCase):
    """setUp에서 실패하는 테스트용 클래스"""

    def setUp(self) -> None:
        """setUp에서 예외 발생"""
        raise Exception

    def testMethod(self) -> None:
        """테스트 메서드 (호출되지 않음)"""
        pass
