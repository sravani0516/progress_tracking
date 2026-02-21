import pytest

# Calculator class
class Calculator:
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

class TestCalculator:

    # 14. setup_method
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2,3) == 5

    def test_subtract(self):
        assert self.calc.subtract(5,3) == 2

# 20. Marker example
@pytest.mark.slow
def test_slow_example():
    assert True