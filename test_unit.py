import pytest
from Test_Python_1 import  fonction

Failures = {"ENGINE": 3, "BRAKE": 7, "TRANSMISSION": 2, "ABS": 5}

def test_fonction():
    assert fonction(Failures) == True