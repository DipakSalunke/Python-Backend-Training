def fizzbuzz(i):
    '''
    >>> fizzbuzz(15)=="fizzbuzz"
    True
    >>> fizzbuzz(18)=="fizz"
    True
    >>> fizzbuzz(20)=="buzz"
    True
    >>> fizzbuzz(29)==29
    True
    '''
    
    if i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    if i % 3 == 0:
        return "fizz"
    if i % 5 == 0:
        return "buzz"
    return i

if __name__ == "__main__":
    import doctest
    doctest.testmod()