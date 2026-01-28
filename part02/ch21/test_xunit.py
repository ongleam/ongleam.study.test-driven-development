"""Chapter 21: Counting - Tests

TestResult로 테스트 결과를 수집하는지 확인.
"""

from part02.ch21.xunit import TestCase, WasRun


class TestCaseTest(TestCase):
    """TestCase를 테스트하는 테스트 케이스"""

    def testTemplateMethod(self) -> None:
        """setUp -> testMethod -> tearDown 순서로 호출되는지 확인 (log)"""
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        """run()이 TestResult를 반환하는지 확인"""
        test = WasRun("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        """실패한 테스트 결과 확인"""
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"


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
