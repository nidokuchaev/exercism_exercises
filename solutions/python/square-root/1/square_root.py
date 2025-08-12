def square_root(number):
    x = number
    while x * x > number:
        x -= 1
    return x