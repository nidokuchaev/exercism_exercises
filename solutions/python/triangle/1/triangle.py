def equilateral(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a == b == c and (a != 0 or b != 0 or c != 0)


def isosceles(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a == b or b == c or a == c
    else: 
        return False


def scalene(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a != b and b != c and a != c
    else: 
        return False