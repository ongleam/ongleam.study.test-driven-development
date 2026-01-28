# Chapter 31: Refactoring

> "리팩토링은 설계를 급진적으로 바꾸더라도 작은 단계로 수행한다." - Kent Beck

## 개요

시스템의 설계를 변경하는 리팩토링 패턴들을 다룬다. TDD에서 리팩토링은 특별한 의미를 가진다 - 이미 통과하는 테스트를 깨뜨리지 않는 변경이다.

## TDD에서의 리팩토링

일반적인 리팩토링: 어떤 상황에서도 프로그램의 의미를 바꾸지 않음

TDD에서의 리팩토링: **이미 통과하는 테스트**를 깨뜨리지 않음

```python
# TDD에서는 이것도 리팩토링
def times(self, multiplier):
    return Dollar(10)  # 상수

# → 변수로 교체
def times(self, multiplier):
    return Dollar(self.amount * multiplier)  # 변수

# 테스트가 여전히 통과하므로 리팩토링!
```

## 패턴 목록

### 1. Reconcile Differences (차이점 조정)

**문제**: 비슷하지만 다른 두 코드를 어떻게 합치는가?

**해결**: 두 코드를 점진적으로 비슷하게 만들어 완전히 같아지면 합친다.

```python
# Before: 비슷하지만 다른 두 메서드
class Dollar:
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

class Franc:
    def times(self, multiplier):
        return Franc(self.amount * multiplier)

# Step 1: 반환 타입을 Money로 통일
class Dollar(Money):
    def times(self, multiplier):
        return Money(self.amount * multiplier, "USD")

class Franc(Money):
    def times(self, multiplier):
        return Money(self.amount * multiplier, "CHF")

# Step 2: 완전히 같아졌으므로 상위 클래스로 이동
class Money:
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
```

**Part 1에서의 사용**: Dollar.times()와 Franc.times() 통합

---

### 2. Isolate Change (변경 격리)

**문제**: 여러 부분에 영향을 주는 변경을 어떻게 안전하게 하는가?

**해결**: 변경할 부분을 먼저 격리한 다음 변경한다.

```python
# Before: 변경이 여러 곳에 영향
class Order:
    def calculate_total(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.price * item.quantity
        tax = subtotal * 0.1  # 세금 계산이 여기에 있음
        return subtotal + tax

# Step 1: 변경할 부분 격리 (Extract Method)
class Order:
    def calculate_total(self):
        subtotal = self._calculate_subtotal()
        tax = self._calculate_tax(subtotal)
        return subtotal + tax

    def _calculate_subtotal(self):
        return sum(item.price * item.quantity for item in self.items)

    def _calculate_tax(self, subtotal):
        return subtotal * 0.1

# Step 2: 격리된 부분만 안전하게 변경
    def _calculate_tax(self, subtotal):
        # 세금 정책 변경
        if subtotal > 100:
            return subtotal * 0.08
        return subtotal * 0.1
```

---

### 3. Migrate Data (데이터 이전)

**문제**: 데이터 표현을 어떻게 안전하게 바꾸는가?

**해결**: 새 표현을 추가하고, 새 표현을 사용하도록 점진적으로 변경한 후, 이전 표현을 제거한다.

```python
# Before: 이름을 단일 문자열로 저장
class User:
    def __init__(self, name):
        self.name = name  # "John Doe"

# Step 1: 새 표현 추가 (기존 유지)
class User:
    def __init__(self, name):
        self.name = name
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = parts[-1] if len(parts) > 1 else ""

# Step 2: 사용처를 새 표현으로 변경
# user.name → f"{user.first_name} {user.last_name}"

# Step 3: 이전 표현 제거
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

---

### 4. Extract Method (메서드 추출)

**문제**: 길고 복잡한 메서드를 어떻게 읽기 쉽게 만드는가?

**해결**: 의미 있는 부분을 별도 메서드로 추출한다.

```python
# Before: 긴 메서드
class Report:
    def generate(self, data):
        # 헤더 생성
        header = "=" * 40 + "\n"
        header += f"Report: {data['title']}\n"
        header += f"Date: {data['date']}\n"
        header += "=" * 40 + "\n"

        # 본문 생성
        body = ""
        for item in data['items']:
            body += f"- {item['name']}: {item['value']}\n"

        # 푸터 생성
        footer = "=" * 40 + "\n"
        footer += f"Total: {sum(i['value'] for i in data['items'])}\n"

        return header + body + footer

# After: 메서드 추출
class Report:
    def generate(self, data):
        header = self._generate_header(data)
        body = self._generate_body(data)
        footer = self._generate_footer(data)
        return header + body + footer

    def _generate_header(self, data):
        lines = ["=" * 40]
        lines.append(f"Report: {data['title']}")
        lines.append(f"Date: {data['date']}")
        lines.append("=" * 40)
        return "\n".join(lines) + "\n"

    def _generate_body(self, data):
        lines = [f"- {item['name']}: {item['value']}" for item in data['items']]
        return "\n".join(lines) + "\n"

    def _generate_footer(self, data):
        total = sum(i['value'] for i in data['items'])
        return "=" * 40 + "\n" + f"Total: {total}\n"
```

**Part 1에서의 사용**: Bank.reduce()에서 로직 추출

---

### 5. Inline Method (메서드 인라인)

**문제**: 메서드가 너무 간단하거나 이름이 본문만큼 명확하지 않을 때?

**해결**: 메서드 본문을 호출 위치에 직접 넣고 메서드를 삭제한다.

```python
# Before: 불필요한 간접 참조
class Order:
    def get_base_price(self):
        return self.quantity * self.item_price

    def get_discount(self):
        return self._has_discount()

    def _has_discount(self):
        return self.quantity > 10

# After: 인라인
class Order:
    def get_base_price(self):
        return self.quantity * self.item_price

    def get_discount(self):
        return self.quantity > 10  # 직접 인라인
```

**주의**: Extract Method의 반대 작업. 과도한 추출 후 정리할 때 사용

---

### 6. Extract Interface (인터페이스 추출)

**문제**: 여러 구현의 공통 부분을 어떻게 표현하는가?

**해결**: 공통 메서드를 인터페이스로 추출한다.

```python
# Before: 공통점이 암묵적
class Rectangle:
    def area(self):
        return self.width * self.height

class Circle:
    def area(self):
        return 3.14159 * self.radius ** 2

# After: 인터페이스 추출
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2
```

**Part 1에서의 사용**: Expression 인터페이스 추출 (Money, Sum 공통)

---

### 7. Move Method (메서드 이동)

**문제**: 메서드가 다른 클래스의 기능을 더 많이 사용할 때?

**해결**: 메서드를 해당 클래스로 이동한다.

```python
# Before: Order가 Customer의 데이터를 많이 사용
class Order:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

    def get_discount_rate(self):
        # Customer 데이터만 사용
        if self.customer.loyalty_years > 5:
            return 0.1
        elif self.customer.total_purchases > 1000:
            return 0.05
        return 0

class Customer:
    def __init__(self, loyalty_years, total_purchases):
        self.loyalty_years = loyalty_years
        self.total_purchases = total_purchases

# After: Customer로 이동
class Order:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

    def get_discount_rate(self):
        return self.customer.get_discount_rate()

class Customer:
    def __init__(self, loyalty_years, total_purchases):
        self.loyalty_years = loyalty_years
        self.total_purchases = total_purchases

    def get_discount_rate(self):
        if self.loyalty_years > 5:
            return 0.1
        elif self.total_purchases > 1000:
            return 0.05
        return 0
```

---

### 8. Method Object (메서드 객체)

**문제**: 메서드가 너무 복잡해서 분해하기 어려울 때?

**해결**: 메서드를 별도의 객체로 만든다.

```python
# Before: 복잡한 메서드 (많은 지역 변수)
class Order:
    def calculate_price(self):
        base_price = self.quantity * self.item_price
        quantity_discount = max(0, self.quantity - 100) * self.item_price * 0.1
        shipping = min(base_price * 0.1, 100)
        tax = (base_price - quantity_discount) * 0.08
        return base_price - quantity_discount + shipping + tax

# After: Method Object로 추출
class PriceCalculator:
    """가격 계산을 담당하는 객체"""

    def __init__(self, order):
        self.quantity = order.quantity
        self.item_price = order.item_price

    def calculate(self):
        return (
            self.base_price
            - self.quantity_discount
            + self.shipping
            + self.tax
        )

    @property
    def base_price(self):
        return self.quantity * self.item_price

    @property
    def quantity_discount(self):
        return max(0, self.quantity - 100) * self.item_price * 0.1

    @property
    def shipping(self):
        return min(self.base_price * 0.1, 100)

    @property
    def tax(self):
        return (self.base_price - self.quantity_discount) * 0.08


class Order:
    def calculate_price(self):
        return PriceCalculator(self).calculate()
```

---

### 9. Add Parameter (매개변수 추가)

**문제**: 메서드에 더 많은 정보가 필요할 때?

**해결**: 매개변수를 추가한다.

```python
# Before
class Report:
    def generate(self, data):
        return f"Report: {data}"

# After: 포맷 매개변수 추가
class Report:
    def generate(self, data, format="text"):
        if format == "text":
            return f"Report: {data}"
        elif format == "html":
            return f"<h1>Report</h1><p>{data}</p>"
```

**주의**: 너무 많은 매개변수는 코드 스멜. 객체로 묶거나 메서드 분리 고려

---

### 10. Method Parameter to Constructor Parameter (메서드 매개변수 → 생성자 매개변수)

**문제**: 여러 메서드가 같은 매개변수를 받을 때?

**해결**: 매개변수를 생성자로 옮겨 인스턴스 변수로 만든다.

```python
# Before: 같은 매개변수 반복
class Formatter:
    def format_header(self, locale):
        return get_header(locale)

    def format_body(self, locale, content):
        return translate(content, locale)

    def format_footer(self, locale):
        return get_footer(locale)

# After: 생성자 매개변수로 변환
class Formatter:
    def __init__(self, locale):
        self.locale = locale

    def format_header(self):
        return get_header(self.locale)

    def format_body(self, content):
        return translate(content, self.locale)

    def format_footer(self):
        return get_footer(self.locale)

# 사용
formatter = Formatter("ko_KR")
formatter.format_header()
formatter.format_body("Hello")
formatter.format_footer()
```

**Part 2에서의 사용**: TestResult를 run() 매개변수에서 TestCase 상태로 변경 가능

---

## 리팩토링 패턴 요약

| 패턴                       | 문제                 | 해결                        |
| -------------------------- | -------------------- | --------------------------- |
| Reconcile Differences      | 비슷한 코드 중복     | 점진적으로 같게 만들어 합침 |
| Isolate Change             | 영향 범위가 큰 변경  | 먼저 격리 후 변경           |
| Migrate Data               | 데이터 표현 변경     | 새 표현 추가 → 이전 → 삭제  |
| Extract Method             | 긴 메서드            | 의미 단위로 추출            |
| Inline Method              | 과도한 간접 참조     | 본문을 호출 위치에 삽입     |
| Extract Interface          | 숨겨진 공통점        | 인터페이스로 명시           |
| Move Method                | 잘못된 위치의 메서드 | 적절한 클래스로 이동        |
| Method Object              | 복잡한 메서드        | 별도 객체로 분리            |
| Add Parameter              | 추가 정보 필요       | 매개변수 추가               |
| Method → Constructor Param | 반복되는 매개변수    | 생성자로 이동               |

## 핵심 원칙

1. **작은 단계**: 한 번에 하나의 리팩토링만
2. **테스트 유지**: 각 단계 후 테스트 실행
3. **의미 보존**: 동작은 그대로, 구조만 개선
4. **가역성**: 잘못되면 되돌릴 수 있어야 함

## 다음 챕터 예고

- Chapter 32: Mastering TDD
- TDD 마스터하기 - 자주 묻는 질문과 답변
