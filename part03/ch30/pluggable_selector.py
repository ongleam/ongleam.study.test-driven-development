"""Pluggable Selector 패턴 - 메서드 이름으로 동적 호출"""

import json


class Report:
    """리포트 - 플러거블 셀렉터"""

    def __init__(self, format_name: str = "text"):
        self.format_name = format_name
        self.data: dict = {}

    def set_data(self, data: dict):
        self.data = data

    def output(self) -> str:
        """저장된 메서드 이름으로 동적 호출"""
        method_name = f"format_{self.format_name}"
        method = getattr(self, method_name)
        return method()

    def format_text(self) -> str:
        lines = [f"{k}: {v}" for k, v in self.data.items()]
        return "\n".join(lines)

    def format_html(self) -> str:
        lines = [f"<li>{k}: {v}</li>" for k, v in self.data.items()]
        return "<ul>" + "".join(lines) + "</ul>"

    def format_json(self) -> str:
        return json.dumps(self.data)
