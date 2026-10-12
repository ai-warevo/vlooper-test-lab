import pytest
from math_logic import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 10) == 0
    assert multiply(0.5, 2) == 1.0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_float():
    assert divide(1, 3) == pytest.approx(0.3333333333333333)
