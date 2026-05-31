import pytest
from Test_Python_1 import Failures

def test_failures():
    assert Failures["ENGINE"] == 3
    assert Failures["BRAKE"] == 7
    assert Failures["TRANSMISSION"] == 2
    assert Failures["ABS"] == 5

