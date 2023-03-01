# HTTLAP doinky doinky
'''
Beep boop
HTTLAP
'''


def magic_function(num1: int, num2: int, op: str) -> int:
    """
    Calls the function that implements the operation op and returns the result
    Assumes that functions add, sub, int_div, modulo exist, receive 2 integer params and return an integer

    Args:
        num1 (int): First operand
        num2 (int): Second operand
        op (str): Operator

    Returns:
        int: The result of the operation
    """
    options = {"+": add, "-": sub, "//": int_div, "%": modulo}
    return options[op](num1, num2)


def add(num1: int, num2: int) -> int:
    """Takes two integers and returns the sum.
    args:
        num1 (int): 1st addend
        num2 (int): 2nd addend
    returns
        (int) sum of num1 & num2"""
    return num1 + num2


def sub(num1: int, num2: int) -> int:
    """Takes takes two integers and subtracts the 2nd from 1st, and
    returns the difference
    args:
        num1 (int): 1st term
        num2 (int): 2nd term
    returns
        (int) difference between num1 & num2"""
    return num1 - num2


def int_div(num1: int, num2: int) -> int:
    """Takes two integers and returns the integer quotient
    args:
        num1 (int): dividend
        num2 (int): divisor
    returns
        (int) quotient of num1 and num2"""
    return num1 // num2


def modulo(num1: int, num2: int) -> int:
    """Takes two integers and returns remainder. woo
    args:
        num1 (int): Integer
        num2 (int): modulus of range
    returns
        (int) modular remainder"""
    return num1 % num2


if __name__ == '__main__':
    print(
        magic_function(2, 2, '+') == 4,
        magic_function(magic_function(2, 2, '+'), 2, '-') == 2
    )
