import pytest

from calculator import Calculator, CalculatorException

EPSILON = 0.1 ** 10


@pytest.fixture(scope='session', autouse=True)
def calculator():
    return Calculator()


def test_numbers(calculator):
    assert calculator.calculate('5') == 5
    assert calculator.calculate('5000') == 5 * 10 ** 3
    assert calculator.calculate('5000000000000') == 5 * 10 ** 12

    assert calculator.calculate('4.0') == 4.0
    assert calculator.calculate('4.') == 4.
    assert calculator.calculate('.4') == .4
    with pytest.raises(CalculatorException):
        calculator.calculate('.')

    with pytest.raises(CalculatorException):
        calculator.calculate('sus')


def test_basic(calculator):
    assert calculator.calculate('5 + 5') == 10
    assert calculator.calculate('5 - 5') == 0
    assert calculator.calculate('-5 - 5') == -10
    with pytest.raises(CalculatorException):
        calculator.calculate('5 + -5')

    assert abs(calculator.calculate('2.39 + 5') - 7.39) < EPSILON
    assert abs(calculator.calculate('-2.39 + 5') - 2.61) < EPSILON
    assert abs(calculator.calculate('-6.66 + 2.39 - 5 + 17.17') - 7.9) < EPSILON

    assert calculator.calculate('5 * 5') == 25
    assert abs(calculator.calculate('-2.5 * 2.5') + 6.25) < EPSILON
    assert abs(calculator.calculate('5 / 5') - 1) < EPSILON
    assert abs(calculator.calculate('-6 / 2.5') + 2.4) < EPSILON

    assert calculator.calculate('5 * 5 + 5') == 30
    assert calculator.calculate('5 + 5 * 5') == 30
    assert abs(calculator.calculate('-6.66 / 3.33 + 2.39 - 5 * 3 + 17.17') - 2.56) < EPSILON

    with pytest.raises(CalculatorException):
        calculator.calculate('6 + 5 - sus')


def test_brackets(calculator):
    assert calculator.calculate('5 + (-5)') == 0
    assert calculator.calculate('5 * (5 + 5)') == 50
    assert abs(calculator.calculate('(12 + 22*7) / (33 + (12*3 -8)) * 3') - 8.1639344262) < EPSILON
