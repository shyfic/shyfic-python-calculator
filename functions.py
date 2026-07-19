import math

def subtraction(x, y):
    result = x - y
    return result

def addition(x, y):
    result = x + y
    return result

def multiplication(x, y):
    result = x * y
    return result

def division(x, y):
    if x == 0 or y == 0:
        result = "Undefined"
    else:
        result = x / y
    return result

def exponent(x, y):
    if x == 0 and y == -1:
        result = "Undefined"
    elif x == -1 and y == 0.5:
        result = "Undefined"
    elif x == 0 and y == 0:
        result = "Undefined"
    else:
        result = math.pow(x, y)
    return result

def root(x, y):
    if x < 0:
        result = "Undefined"
    else:
        result = math.pow(x, 1/y)
    return result
