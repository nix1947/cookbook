"""
when to use function ?
    To break large program into smaller ones.
    To improve reusability.

    Tips on function
    ~~~~~~~~~~~~~~~~~
"""

def sum(a, b):
    return a + b # By default return None


# TIP: Never return None from function, rather throw exceptions. 

def divide(x, y):
    try:
        result = x / y
    exception ZeroDivisionError:
        raise("Invalid inputs")

    return result






