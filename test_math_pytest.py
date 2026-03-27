import pytest
from math_utils import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(1.5, 2.5) == 4.0
    with pytest.raises(TypeError):
        calc.add(8, None)
        calc.add('3', 1)
        calc.add(4.5, 'x')
        calc.add([5.5], 1)
        calc.add({'a': 5}, 3)
        calc.add({'a': 7}, {'b': 15})
        calc.add([1], [2])
        calc.add('2', '3')
        calc.add(None, None)

def test_subtract():
    calc = Calculator()
    assert calc.subtract(4, 7) == -3
    assert calc.subtract(5.5, 2.2) == 3.3
    with pytest.raises(TypeError):
        calc.subtract(None, 1)
        calc.subtract('9', 2)
        calc.subtract(6.6, 'a')
        calc.subtract([3], 1.1)
        calc.subtract(6, {'b': 8})
        calc.subtract({'a': 1}, {'b': 2})
        calc.subtract([5], [9])
        calc.subtract('8', '3')
        calc.subtract(None, None)

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(4, 2.5) == 10.0
    with pytest.raises(TypeError):
        calc.multiply(None, 5.5)
        calc.multiply('6.3', 3)
        calc.multiply(6, 'm')
        calc.multiply([4], 2)
        calc.multiply({'a': 7}, 1)
        calc.multiply({'a': 6.5}, {'b': 5.5})
        calc.multiply([7.1], [2])
        calc.multiply('9', '5')
        calc.multiply(None, None)

def test_divide():
    calc = Calculator()
    assert calc.divide(4, 2) == 2
    assert calc.divide(4.8, 2.4) == 2.0
    with pytest.raises(ZeroDivisionError):
        calc.divide(3, 0)
    with pytest.raises(TypeError):
        calc.divide(5, None)
        calc.divide('2', 1)
        calc.divide(3, 'c')
        calc.divide([7], 2)
        calc.divide(6, {'b': 8})
        calc.divide({'a': 10}, {'b': 5})
        calc.divide([1.5], [2.5])
        calc.divide('7', '3')
        calc.divide(None, None)
