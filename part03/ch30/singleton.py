"""Singleton 패턴 - 클래스의 인스턴스가 하나만 존재"""


class Configuration:
    """싱글톤 설정 관리자"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.settings: dict = {}

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str, default=None):
        return self.settings.get(key, default)

    def clear(self):
        """테스트를 위한 초기화"""
        self.settings.clear()


# 대안: 모듈 수준 싱글톤 (더 파이썬다운 방식)
class _ConfigModule:
    """모듈 수준 싱글톤"""

    def __init__(self):
        self.settings: dict = {}

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str, default=None):
        return self.settings.get(key, default)

    def clear(self):
        self.settings.clear()


# 모듈 임포트 시 한 번만 생성
config = _ConfigModule()
