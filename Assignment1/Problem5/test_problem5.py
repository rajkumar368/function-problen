import pytest
from Solution5 import int_roman
def test_int_roman():
    num = int(12)
    assert int_roman(num) == "XII"
    
def test_int_roman1():
    num = int(8)
    assert int_roman(num) ==  "VIII"
  