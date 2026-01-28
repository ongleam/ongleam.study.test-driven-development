"""Template Method 패턴 - 순서는 정의하고 세부 구현은 위임"""

from abc import ABC, abstractmethod


class TestCase(ABC):
    """템플릿 메서드 패턴 - xUnit"""

    def __init__(self, name: str):
        self.name = name

    def setUp(self) -> None:
        """하위 클래스에서 오버라이드"""
        pass

    def tearDown(self) -> None:
        """하위 클래스에서 오버라이드"""
        pass

    def run(self) -> str:
        """템플릿 메서드 - 순서 정의"""
        log = ""
        self.setUp()
        log += "setUp "
        method = getattr(self, self.name)
        method()
        log += f"{self.name} "
        self.tearDown()
        log += "tearDown"
        return log


class DataProcessor(ABC):
    """데이터 처리 템플릿"""

    def process(self, data):
        """템플릿 메서드"""
        validated = self.validate(data)
        transformed = self.transform(validated)
        result = self.save(transformed)
        return result

    @abstractmethod
    def validate(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def save(self, data):
        pass


class JSONProcessor(DataProcessor):
    """JSON 데이터 처리"""

    def __init__(self):
        self.saved_data = None

    def validate(self, data):
        if not isinstance(data, dict):
            raise ValueError("Must be dict")
        return data

    def transform(self, data):
        return {k.upper(): v for k, v in data.items()}

    def save(self, data):
        self.saved_data = data
        return data
