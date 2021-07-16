"""Reusable Math calculation functions"""


def adding_function(number):
    """this function adds 5 to any number, and will give error messages unless the input is a positive, real number"""
    if type(number) not in [int, float]:
        raise TypeError("The number must be a positive, real number")
    if number < 0:
        raise ValueError("number must be postive")
    return number + 5
