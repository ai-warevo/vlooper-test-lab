import pytest

from math_logic import add, pow, sqrt


def test_add():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add("a", "b") == "ab"
    with pytest.raises(TypeError):
        add(1, "a")


def test_sqrt():
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0
    assert sqrt(1e308) > 0
    with pytest.raises(ValueError):
        sqrt(-1)
    with pytest.raises(TypeError):
        sqrt("a")


def test_pow():
    assert pow(2, 3) == 8.0
    assert pow(5, 2) == 25.0
    assert pow(10, 0) == 1.0
    assert pow(2, -1) == 0.5
    with pytest.raises(ValueError):
        pow(-1, 0.5)
    with pytest.raises(ValueError):
        pow(0, -1)
    with pytest.raises(TypeError):
        pow("a", 2)
