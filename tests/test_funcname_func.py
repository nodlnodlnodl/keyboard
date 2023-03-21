from utils import funcname
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (10, 5, 2),
                                                   (20, 5, 4),
                                                   (-10, 2, -5)])
def test_funcname_1(a, b, expected_result):
    assert funcname(a, b) == expected_result


def test_funcname_zero():
    with pytest.raises(ZeroDivisionError): # ожидаем ошибки
        funcname(10, 0)


def test_funcname_type():
    with pytest.raises(TypeError): # ожидаем ошибки
        funcname(10, "2")