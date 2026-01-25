"""Chapter 18: First Steps to xUnit - Tests

xUnit 프레임워크를 테스트하는 테스트.
프레임워크 자체로 자기 자신을 테스트하는 "부트스트랩" 방식.
"""

from part02.ch18.xunit import TestCase, WasRun


class TestCaseTest(TestCase):
    """TestCase를 테스트하는 테스트 케이스

    xUnit의 자기 참조적 특성:
    - TestCase를 테스트하기 위해 TestCase를 상속
    - 만들고 있는 프레임워크로 자기 자신을 테스트
    """

    def testRunning(self) -> None:
        """run()이 테스트 메서드를 실행하는지 확인"""
        test = WasRun("testMethod")
        assert test.wasRun is None  # 아직 실행 안 됨
        test.run()
        assert test.wasRun is True  # 실행됨


# pytest용 래퍼 함수
def test_running():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testRunning")
    test.run()
