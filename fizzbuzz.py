def FizzBuzz(numbre):
    # if numbre is smaller than or equal to 0, it will raise ValueError
    if numbre <= 0:
        raise ValueError

    # if numbre is multiple of 3 and 5, it will return fizzbuzz
    if numbre % 3 == 0 and numbre % 5 == 0:
        return "fizzbuzz"

    # if numbre is multiple of 3, it will return fizz
    if numbre % 3 == 0:
        return "fizz"

    # if numbre is multiple of 5, it will return buzz
    if numbre % 5 == 0:
        return "buzz"
    
    # else means non of the conditions was triggered so, it return the numbre
    return str(numbre)
    
    
