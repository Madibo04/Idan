import simple_cal
import pytest


def test_add():
    assert simple_cal.add(5, 6) == 11
    assert simple_cal.add(-5, -10) == -15
    assert simple_cal.add(-20, 5) == -15
    with pytest.raises(TypeError):
        simple_cal.add("Hi" "Hello")


def test_subtract():
    assert simple_cal.subtract(20, 5) == 15
    assert simple_cal.subtract(-20, 30) == -50
    assert simple_cal.subtract(-15, -8) == -7


def test_multiply():
    assert simple_cal.multiply(5, 6) == 30
    assert simple_cal.multiply(-5, -2) == 10
    assert simple_cal.multiply(-10, 4) == -40


def test_divide():
    assert simple_cal.divide(20, 5) == 4
    assert simple_cal.divide(-20, 4) == -5
    with pytest.raises(TypeError):
        simple_cal.divide("Hello World")
    with pytest.raises(ZeroDivisionError):
        simple_cal.divide(20, 0)