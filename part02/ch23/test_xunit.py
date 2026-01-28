"""Chapter 23: How Suite It Is - Tests

TestSuite로 여러 테스트 실행 확인.
"""

from part02.ch23.xunit import (
    TestCase,
    TestResult,
    TestSuite,
    WasRun,
    WasRunWithBrokenSetUp,
)


class TestCaseTest(TestCase):
    """TestCase를 테스트하는 테스트 케이스"""

    def setUp(self) -> None:
        """각 테스트 전에 TestResult 인스턴스 생성"""
        self.result = TestResult()

    def testTemplateMethod(self) -> None:
        """setUp -> testMethod -> tearDown 순서로 호출되는지 확인 (log)"""
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        """run()이 TestResult를 반환하는지 확인"""
        test = WasRun("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        """실패한 테스트 결과 확인"""
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self) -> None:
        """TestResult 포맷팅 확인"""
        self.result.testStarted()
        self.result.testFailed()
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedSetUpResult(self) -> None:
        """setUp 실패 시 결과 확인"""
        test = WasRunWithBrokenSetUp("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testSuite(self) -> None:
        """TestSuite로 여러 테스트 실행 확인"""
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed"


# pytest용 래퍼 함수
def test_template_method():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testTemplateMethod")
    test.run()


def test_result():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testResult")
    test.run()


def test_failed_result():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testFailedResult")
    test.run()


def test_failed_result_formatting():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testFailedResultFormatting")
    test.run()


def test_failed_set_up_result():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testFailedSetUpResult")
    test.run()


def test_suite():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testSuite")
    test.run()
