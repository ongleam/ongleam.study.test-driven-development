"""Chapter 22: Dealing with Failure - Tests

실패한 테스트 결과 포맷팅 확인.
"""

from part02.ch22.xunit import TestCase, TestResult, WasRun, WasRunWithBrokenSetUp


class TestCaseTest(TestCase):
    """TestCase를 테스트하는 테스트 케이스"""

    def setUp(self) -> None:
        """각 테스트 전에 WasRun 인스턴스 생성"""
        self.test = WasRun("testMethod")

    def testRunning(self) -> None:
        """run()이 테스트 메서드를 실행하는지 확인"""
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self) -> None:
        """run()이 setUp을 먼저 호출하는지 확인"""
        self.test.run()
        assert self.test.wasSetUp

    def testTearDown(self) -> None:
        """run()이 tearDown을 마지막에 호출하는지 확인"""
        self.test.run()
        assert self.test.wasTornDown

    def testTemplateMethod(self) -> None:
        """setUp -> testMethod -> tearDown 순서로 호출되는지 확인 (log)"""
        self.test.run()
        assert self.test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        """run()이 TestResult를 반환하는지 확인"""
        result = self.test.run()
        assert result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        """실패한 테스트 결과 확인"""
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self) -> None:
        """TestResult 포맷팅 확인"""
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"

    def testFailedSetUpResult(self) -> None:
        """setUp 실패 시 결과 확인"""
        test = WasRunWithBrokenSetUp("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"


# pytest용 래퍼 함수
def test_running():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testRunning")
    test.run()


def test_set_up():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testSetUp")
    test.run()


def test_tear_down():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testTearDown")
    test.run()


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
