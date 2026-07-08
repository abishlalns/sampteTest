def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
