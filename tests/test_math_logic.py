import pytest
from math_logic import add

def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_negative_integers():
    assert add(-1, -1) == -2

def test_add_mixed_integers():
    assert add(-1, 5) == 4

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -3) == -3

def test_add_floats():
    assert add(1.1, 2.2) == pytest.approx(3.3)

def test_add_large_integers():
    assert add(10**18, 10**18) == 2 * 10**18
