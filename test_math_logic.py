import pytest
from math_logic import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_signs():
    assert add(-1, 1) == 0
    assert add(1, -1) == 0

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_large_numbers():
    assert add(10**15, 10**15) == 2 * 10**15
