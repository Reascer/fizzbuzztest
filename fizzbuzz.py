def FizzBuzz(numbre):
    if numbre <= 0:
        raise ValueError
    if numbre % 3 == 0:
        return "fizz"
    if numbre % 5 == 0:
        return "buzz"
    
