from doc_test import fizzbuzz

def test1():
    assert fizzbuzz(15)=="fizzbuzz"

def test2():
    assert fizzbuzz(29)==29

def test3():
    assert fizzbuzz(20)=="buzz"
        