"""Chapter 19: Set the Table - Tests

setUp이 테스트 메서드보다 먼저 호출되는지 확인.
"""

from part02.ch19.xunit import TestCase, WasRun


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


# pytest용 래퍼 함수
def test_running():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testRunning")
    test.run()


def test_set_up():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testSetUp")
    test.run()
