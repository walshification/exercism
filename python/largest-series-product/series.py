import functools
import operator


def largest_product(num_str, length):
    """Takes a string of digits and gives you the largest product of
    the digits of the contiguous substrings of length `n`.

    Args:
        * digit_string (str): string of digits to be parsed.
        * n (int): length of the substrings `digit_string` will be
                   divided into.

    Returns:
        * list: list of digit combinations `digit_string` was divided
                into.

    Raises:
        * ValueError: if n is longer than the `digit_string` or 0.
    """
    if length == 0:
        return 1
    return max(
        functools.reduce(operator.mul, sl) for sl in _slices(num_str, length)
    )


def _slices(digit_string, n):
    """Takes a string of digits and gives you all the contiguous
    substrings of length `n` in that string.
    """
    if n > len(digit_string):
        raise ValueError('Digit string is too small for the desired slice.')
    if n < 0:
        raise ValueError('Length must be 0 or longer.')
    return _slice(digit_string, n)


def _slice(string, n):
    """Divides a string of length `n` into a list of integers."""
    return list(
        _intergize(string[(i):(n + i)]) for i in range(len(string) + 1) if
        len(string) - i >= n
    )


def _intergize(chars):
    """Converts lists of number strings into lists of integers."""
    return list(int(char) for char in chars)
