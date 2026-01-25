# Chapter 13: Make It

## 핵심 개념

**"Fake It"에서 실제 구현으로 전환**

Chapter 12에서 `Bank.reduce()`가 하드코딩된 `Money.dollar(10)`을 반환했다.
이는 테스트 데이터($5 + $5 = **$10**)와 코드 데이터(**10**)의 중복이다.

> "We have duplication between the data in the test and the data in the code.
> We have to eliminate it." - Kent Beck

## TODO 리스트

- [x] $5 + 10 CHF = $10 (환율이 2:1일 경우)
- [x] **$5 + $5 = $10**
- [x] **$5 + $5가 Sum을 반환**
- [x] **Bank.reduce(Sum)**
- [x] **Money.reduce (같은 통화)**
- [ ] Reduce Money with conversion
- [ ] Reduce(Bank, String)

## 핵심 변경사항

### 1. Expression에 reduce() 추가

```python
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to_currency: str) -> Money:
        pass
```

### 2. Sum.reduce() 실제 구현

```python
# Chapter 12 (Fake It)
class Bank:
    def reduce(self, source, to_currency):
        return Money.dollar(10)  # 하드코딩!

# Chapter 13 (Make It)
class Sum(Expression):
    def reduce(self, bank, to_currency):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to_currency)
```

### 3. Money.reduce() 다형성

```python
class Money(Expression):
    def reduce(self, bank, to_currency):
        return self  # 자기 자신 반환
```

### 4. Bank.reduce() 다형성 활용

```python
class Bank:
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)  # 다형성!
```

## 테스트

```bash
python -m pytest part01/ch13/ -v
```

## TDD 사이클

1. **Red**: `test_reduce_sum` - $3 + $4 = $7 (하드코딩 $10으로는 실패!)
2. **Green**: `Sum.reduce()` 실제 구현
3. **Refactor**: 다형성으로 Bank.reduce() 단순화

## 배운 점

- **"Fake It"은 임시** - 빨리 테스트를 통과시키기 위한 전략
- **데이터 중복 제거** - 테스트와 코드의 중복된 상수 제거
- **다형성** - Bank가 Sum인지 Money인지 알 필요 없음
