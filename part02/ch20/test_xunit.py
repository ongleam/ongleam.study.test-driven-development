"""Chapter 20: Cleaning Up After - Tests

tearDown이 테스트 메서드 후에 호출되는지 확인.
"""

from part02.ch20.xunit import TestCase, WasRun


class TestCaseTest(TestCase):
    """TestCase를 테스트하는 테스트 케이스"""

    def testTemplateMethod(self) -> None:
        """setUp -> testMethod -> tearDown 순서로 호출되는지 확인 (log)"""
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "


# pytest용 래퍼 함수
def test_template_method():
    """pytest에서 실행할 수 있도록 래핑"""
    test = TestCaseTest("testTemplateMethod")
    test.run()
