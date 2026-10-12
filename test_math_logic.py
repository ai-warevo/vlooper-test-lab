import pytest
from math_logic import add

def test_add_positive_numbers():
    assert add(2, 2) == 4

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-1, 5) == 4

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
