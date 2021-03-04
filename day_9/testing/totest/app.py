def fizzbuzz(i):
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