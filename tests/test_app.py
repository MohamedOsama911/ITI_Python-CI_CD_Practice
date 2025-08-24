import pytest
from src import app

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 3) == 2

def test_multiply():
    assert app.multiply(2, 3) == 6

def test_divide():
    assert app.divide(6, 3) == 2
    assert app.divide(6, 0) is None
