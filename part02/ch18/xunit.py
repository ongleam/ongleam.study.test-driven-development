"""Chapter 18: First Steps to xUnit

xUnit 테스트 프레임워크의 첫 번째 단계.
테스트 메서드를 이름으로 호출하는 기본 구조 구현.
"""


class TestCase:
    """xUnit 테스트 케이스 기본 클래스"""

    def __init__(self, name: str) -> None:
        """테스트 메서드 이름을 저장

        Args:
            name: 실행할 테스트 메서드의 이름
        """
        self.name = name

    def run(self) -> None:
        """테스트 메서드를 이름으로 찾아서 실행 (reflection)"""
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    """테스트 실행 여부를 확인하는 테스트용 클래스

    xUnit 프레임워크 자체를 테스트하기 위한 클래스.
    "부트스트랩 문제"를 해결하는 핵심 요소.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: int | None = None

    def testMethod(self) -> None:
        """실행되면 wasRun을 1로 설정"""
        self.wasRun = 1
