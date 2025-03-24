# Implement pow(x, n).


def myPow(x: float, n: int) -> float:
    """
    Implement pow(x, n), where x is a floating number and n is an integer.

    Args:
    x (float): The base number.
    n (int): The exponent.

    Returns:
    float: The result of x raised to the power of n.
    """
    # Time complexity: O(logน) using the divide and conquer approach.
    # Space complexity: O(logน) due to recursive call stack.

    def helper(x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / helper(x, -n)
        elif n % 2 == 0:
            return helper(x * x, n // 2)
        else:
            return x * helper(x * x, (n - 1) // 2)

    return helper(x, n)
