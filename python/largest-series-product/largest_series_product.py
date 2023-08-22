import functools
import operator
from typing import List


def largest_product(series: str, size: int) -> int:
    """Return largest product of contiguous n-size substrings of series.

    :param digit_string: str - string of digits to be parsed.
    :param size: int - length of the substrings to be compared.
    :return: list - digit substring combinations of the length of size.

    :raises ValueError: span must be smaller than string length
    :raises ValueError: span must not be negative
    :raises ValueError: digits input must only contain digits
    """
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    if size == 0:
        return 1
    return max(multiply(slice) for slice in create_slices(series, size))


def multiply(slice: List[int]) -> int:
    """Return the product of a list of integers."""
    return functools.reduce(operator.mul, slice)


def create_slices(digit_string: str, N: int) -> List[int]:
    """Return contiguous substrings in digit_string of length N."""
    return [
        [int(char) for char in digit_string[(i) : (N + i)]]
        for i in range(len(digit_string) + 1)
        if len(digit_string) - i >= N
    ]
