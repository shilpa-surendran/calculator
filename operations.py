def add(a, b):
    """
    This function adds two numbers and returns the result.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The sum of the two numbers.
    
    Raises:
        TypeError: If the inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a + b

def subtract(a, b):
    """
    This function subtracts the second number from the first and returns the result.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The difference of the two numbers.
    
    Raises:
        TypeError: If the inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a - b

def divide(a, b):
    """
    This function divides the first number by the second and returns the result.

    Args:
        a (int, float): The numerator.
        b (int, float): The denominator.

    Returns:
        int, float: The quotient of the two numbers.
    
    Raises:
        TypeError: If the inputs are not numbers.
        ValueError: If the denominator is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
