"""Chapter 19: Set the Table

setUp() 메서드를 도입하여 테스트 픽스처 설정.
테스트 메서드 실행 전에 setUp()이 먼저 호출됨.
"""


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

    def run(self) -> None:
        """setUp을 먼저 호출한 후 테스트 메서드 실행"""
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    """테스트 실행 여부와 setUp 호출을 확인하는 테스트용 클래스"""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.wasRun: int | None = None
        self.wasSetUp: int | None = None

    def setUp(self) -> None:
        """setUp 호출 기록"""
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self) -> None:
        """테스트 메서드 호출 기록"""
        self.wasRun = 1
