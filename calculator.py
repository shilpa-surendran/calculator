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

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add(num1, num2)
        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except TypeError as e:
        print(f"Error: {e}")
