import pytest
from solution4 import check_parentheses
def  test_check_parentheses():
    str = "({[]})"
    assert check_parentheses(str) == True
    
def  test_check_parentheses1():
    str = "({[]))"
    assert check_parentheses(str) == False