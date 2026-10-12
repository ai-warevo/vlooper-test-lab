import pytest
from math_logic import add

def test_add_positive():
    assert add(2, 2) == 4

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_mixed():
    assert add(-1, 1) == 0

def test_add_float():
    assert add(1.5, 2.5) == 4.0

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
