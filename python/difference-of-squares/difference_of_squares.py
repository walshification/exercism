def difference_of_squares(N: int) -> int:
    """Return the the difference of squares for numbers up to N.

    :param N: int - the Nth natural number.
    :return: int - the difference of the square of the sum and the sum of the squares.
    """
    return square_of_sum(N) - sum_of_squares(N)


def square_of_sum(N: int) -> int:
    """Returns the square of the sum of the first N natural numbers."""
    return sum(range(N + 1)) ** 2


def sum_of_squares(N: int) -> int:
    """Returns the sum of the squares of the first N natural numbers."""
    return sum(i * i for i in range(N + 1))
