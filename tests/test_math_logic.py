from math_logic import add, sqrt, pow
import pytest

def test_add():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add('a', 'b') == 'ab'

def test_sqrt():
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0
    with pytest.raises(ValueError):
        sqrt(-1)

def test_pow():
    assert pow(2, 3) == 8.0
    assert pow(5, 2) == 25.0
    assert pow(10, 0) == 1.0
    assert pow(2, -1) == 0.5
    with pytest.raises(ValueError):
        pow(-1, 0.5)

