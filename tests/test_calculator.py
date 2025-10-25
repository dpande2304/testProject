import pytest
from app.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(1,1) == 0

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-2,4) == -8

def test_divide():
    assert divide(4,2) == 2
    with pytest.raises(ValueError):
        assert divide(10,0)