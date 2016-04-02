def difference(limit):
    """Finds the difference between the sum of the squares and the
    square of the sums of the first N natural numbers.

    Args:
        * limit (int): the Nth natural number.

    Returns:
        * int: the difference in question.
    """
    return square_of_sum(limit) - sum_of_squares(limit)


def square_of_sum(limit):
    """Returns the square of the sum of the first N natural numbers."""
    sum_total = sum(range(limit + 1))
    return sum_total * sum_total


def sum_of_squares(limit):
    """Returns the sum of the squares of the first N natural numbers."""
    return sum(map(lambda i: i * i, range(limit + 1)))
