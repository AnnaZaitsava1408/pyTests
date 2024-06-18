import pytest

from app.calc import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 17, 6) == 23

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 37,9) == 28

    def test_multiply_success(self):
        assert self.calc.multiply(self, 7,9) == 63

    def test_division_success(self):
        assert self.calc.division(self, 36,9) == 4

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')