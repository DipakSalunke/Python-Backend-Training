import pytest
from totest.app import fizzbuzz

def test1():
    assert fizzbuzz(15)=="fizzbuzz"

@pytest.mark.skip(reason="Skip this test")
def test_skip():
    assert fizzbuzz(29)==29

@pytest.mark.skipif(5==5, reason="condition true")
def test_skip_if_true():
    assert fizzbuzz(8) == "fizz"

@pytest.mark.xfail
def test_xfail():
    assert fizzbuzz(6) == "buzz" 

@pytest.mark.parametrize("test_input,expected", [(15, "fizzbuzz"), (18, "fizz")])
def test_fb(test_input, expected):
    assert fizzbuzz(test_input) == expected

