import Fixme
import pytest


def test__evens_1():
    assert Fixme.evens(10) == [0, 2, 4, 6, 8, 10]

def test__evens_2():
    assert Fixme.evens(11) == [0, 2, 4, 6, 8, 10]

def test__evens_3():
    assert Fixme.evens(0) == [0]

def test__evens_4():
    assert Fixme.evens(1) == [0]

def test__evens_5():
    assert Fixme.evens(-1) == []

