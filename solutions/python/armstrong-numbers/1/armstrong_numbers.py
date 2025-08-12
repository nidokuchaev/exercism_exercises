def is_armstrong_number(number):
    i = len(str(number))
    d = [int(d) for d in str(number)]
    test = sum([digit ** i for digit in d])
    return test == number