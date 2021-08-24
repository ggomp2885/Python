"""Tests for math calculations"""
import pytest
from math_calculations import adding_function


def test_math():
    """ensures the math of the adding_function is working"""
    assert adding_function(5) == 11
    assert adding_function(10) == 15


def test_v_error():
    with pytest.raises(ValueError):
        adding_function(-1)


def test_t_error():
    with pytest.raises(TypeError):
        adding_function('hello')
