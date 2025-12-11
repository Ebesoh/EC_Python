import pytest
from CalculatorProgram import calculator   # replace 'your_module' with the name of the file containing the function

def test_addition():
    assert calculator(5, 3, "+") == 8

def test_subtraction():
    assert calculator(10, 4, "-") == 6

def test_multiplication():
    assert calculator(7, 6, "*") == 42

def test_division():
    assert calculator(8, 2, "/") == 4

def test_mod():
    assert calculator(8, 7, "%") == 1

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator(10, 0, "/")

def test_invalid_operator():
    with pytest.raises(ValueError, match="Unknow operator"):
        calculator(5, 6, "&")
