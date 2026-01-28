"""Chapter 30: Design Patterns - Tests"""


# 1. Command Pattern
def test_command():
    from command import Light, LightOffCommand, LightOnCommand, RemoteControl

    light = Light()
    remote = RemoteControl()

    # 전등 켜기
    remote.set_command(LightOnCommand(light))
    remote.press_button()
    assert light.is_on

    # 전등 끄기
    remote.set_command(LightOffCommand(light))
    remote.press_button()
    assert not light.is_on


# 2. Value Object Pattern
def test_value_object():
    from value_object import Money

    # 동등성
    five_a = Money(5, "USD")
    five_b = Money(5, "USD")
    assert five_a == five_b
    assert five_a is not five_b  # 다른 객체

    # 불변성 - times는 새 객체 반환
    ten = five_a.times(2)
    assert ten == Money(10, "USD")
    assert five_a == Money(5, "USD")  # 원본 불변

    # 해시 가능 (딕셔너리 키로 사용 가능)
    prices = {Money(5, "USD"): "five dollars"}
    assert prices[Money(5, "USD")] == "five dollars"


# 3. Null Object Pattern
def test_null_object():
    from null_object import Calculator, ConsoleLogger

    # NullLogger 사용 - if 체크 불필요
    calc = Calculator()  # logger=None
    result = calc.add(2, 3)
    assert result == 5  # 로깅 없이 정상 동작

    # ConsoleLogger 사용
    logger = ConsoleLogger()
    calc_with_log = Calculator(logger)
    calc_with_log.add(2, 3)
    assert "add(2, 3) = 5" in logger.messages


# 4. Template Method Pattern
def test_template_method():
    from template_method import JSONProcessor

    processor = JSONProcessor()
    result = processor.process({"name": "alice", "age": 30})

    assert result == {"NAME": "alice", "AGE": 30}
    assert processor.saved_data == {"NAME": "alice", "AGE": 30}


# 5. Pluggable Object Pattern
def test_pluggable_object():
    from pluggable_object import Editor, RangeSelection, SingleSelection

    editor = Editor()
    editor.items = ["a", "b", "c", "d", "e"]

    # 단일 선택 모드
    editor.set_mode(SingleSelection())
    assert editor.select(1, 3) == ["b"]

    # 범위 선택 모드로 교체
    editor.set_mode(RangeSelection())
    assert editor.select(1, 3) == ["b", "c", "d"]


# 6. Pluggable Selector Pattern
def test_pluggable_selector():
    from pluggable_selector import Report

    data = {"name": "Alice", "age": 30}

    # 텍스트 포맷
    report = Report("text")
    report.set_data(data)
    assert "name: Alice" in report.output()

    # HTML 포맷
    report = Report("html")
    report.set_data(data)
    assert "<li>name: Alice</li>" in report.output()

    # JSON 포맷
    report = Report("json")
    report.set_data(data)
    assert '"name": "Alice"' in report.output()


# 7. Factory Method Pattern
def test_factory_method():
    from factory_method import Money

    # 팩토리 메서드로 생성 - 구체 클래스 은닉
    five_dollars = Money.dollar(5)
    ten_francs = Money.franc(10)

    assert five_dollars.currency() == "USD"
    assert ten_francs.currency() == "CHF"

    # 클라이언트는 Dollar, Franc을 직접 알 필요 없음
    assert five_dollars.times(2).amount == 10


# 8. Imposter Pattern
def test_imposter():
    from imposter import Bank, Money

    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    # Money와 Sum 모두 Expression처럼 행동
    five_dollars = Money(5, "USD")
    ten_francs = Money(10, "CHF")

    # Sum은 Money를 사칭
    sum_expr = five_dollars.plus(ten_francs)
    result = sum_expr.reduce(bank, "USD")

    assert result.amount == 10  # 5 + 10/2


# 9. Composite Pattern
def test_composite():
    from composite import TestCase, TestSuite

    class SampleTest(TestCase):
        def test_pass(self):
            assert True

        def test_fail(self):
            raise Exception("fail")

    # 개별 테스트
    single = SampleTest("test_pass")
    result = single.run()
    assert result.summary() == "1 run, 0 failed"

    # 스위트 (복합체)
    suite = TestSuite()
    suite.add(SampleTest("test_pass"))
    suite.add(SampleTest("test_fail"))

    result = suite.run()
    assert result.summary() == "2 run, 1 failed"

    # 스위트 안에 스위트 (재귀 구조)
    outer_suite = TestSuite()
    outer_suite.add(suite)
    outer_suite.add(SampleTest("test_pass"))

    result = outer_suite.run()
    assert result.summary() == "3 run, 1 failed"


# 10. Collecting Parameter Pattern
def test_collecting_parameter():
    from collecting_parameter import TestCase, TestResult, TestSuite

    class MyTest(TestCase):
        def test_one(self):
            pass

        def test_two(self):
            raise Exception("error in two")

    result = TestResult()  # 수집 매개변수

    # 여러 테스트가 동일한 result에 결과 누적
    suite = TestSuite()
    suite.add(MyTest("test_one"))
    suite.add(MyTest("test_two"))
    suite.run(result)

    assert result.run_count == 2
    assert result.failure_count == 1
    assert "error in two" in result.errors


# 11. Singleton Pattern
def test_singleton():
    from singleton import Configuration, config

    # 클래스 기반 싱글톤
    config1 = Configuration()
    config2 = Configuration()

    assert config1 is config2  # 동일 인스턴스

    config1.set("debug", True)
    assert config2.get("debug")  # 상태 공유

    config1.clear()  # 테스트 정리

    # 모듈 기반 싱글톤
    config.set("env", "test")
    assert config.get("env") == "test"

    config.clear()  # 테스트 정리
