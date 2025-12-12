import pytest

import CalculatorProgram
from CalculatorProgram import calculator   # replace 'your_module' with the name of the file containing the function
from unittest.mock import patch

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
    with pytest.raises(ValueError, match = "Cannot divide by zero"):
        calculator(10, 0, "/")

def test_invalid_operator():
    with pytest.raises(ValueError, match = "Unknow operator"):
        calculator(5, 6, "&")

def test_invalid_no_operator():
    with pytest.raises(ValueError, match = "Unknow operator"):
        calculator(5, 6, "")

def test_add_Mock():
    with patch("CalculatorProgram.calculator", return_value = 4) as mock_calc:
        result =  CalculatorProgram.calculator(2,2,"+")
        assert result == 4
        mock_calc.assert_called_once_with(2,2,"+")

def test_sub_Mock():
    with patch("CalculatorProgram.calculator", return_value = 2) as mock_calc:
        result =  CalculatorProgram.calculator(4,2,"-")
        assert result == 2
        mock_calc.assert_called_once_with(4,2,"-")

def test_multi_Mock():
    with patch("CalculatorProgram.calculator", return_value = 4) as mock_calc:
        result =  CalculatorProgram.calculator(2,2,"*")
        assert result == 4
        mock_calc.assert_called_once_with(2,2,"*")

def test_divide_Mock():
    with patch("CalculatorProgram.calculator", return_value = 2) as mock_calc:
        result =  CalculatorProgram.calculator(4,2,"/")
        assert result == 2
        mock_calc.assert_called_once_with(4,2,"/")

def test_mod_Mock():
    with patch("CalculatorProgram.calculator", return_value = 1) as mock_calc:
        result =  CalculatorProgram.calculator(3,2,"%")
        assert result == 1
        mock_calc.assert_called_once_with(3,2,"%")