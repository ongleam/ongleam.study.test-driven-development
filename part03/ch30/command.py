"""Command 패턴 - 계산 작업을 객체로 표현"""

from abc import ABC, abstractmethod


class Command(ABC):
    """명령 인터페이스"""

    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    """전등 켜기 명령"""

    def __init__(self, light: "Light"):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class LightOffCommand(Command):
    """전등 끄기 명령"""

    def __init__(self, light: "Light"):
        self.light = light

    def execute(self) -> None:
        self.light.off()


class Light:
    """전등"""

    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False


class RemoteControl:
    """리모컨 - 명령 실행기"""

    def __init__(self):
        self.command: Command | None = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
