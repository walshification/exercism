from typing import List


def slices(digit_string: str, N: int) -> List[str]:
    """Returns substrings of digits of N-length from the digit string.

    :param digit_string: str - string of digits to be parsed.
    :param N: int - length of the desired substrings.
    :return: list - substrings of digit_string of N-length.

    :raises ValueError: slice length cannot be zero
    :raises ValueError: series cannot be empty
    :raises ValueError: slice length cannot be greater than series length
    :raises ValueError: slice length cannot be negative
    """
    if N == 0:
        raise ValueError("slice length cannot be zero")
    if len(digit_string) == 0:
        raise ValueError("series cannot be empty")
    if N > len(digit_string):
        raise ValueError("slice length cannot be greater than series length")
    if N < 0:
        raise ValueError("slice length cannot be negative")

    return list(
        digit_string[i : (N + i)]
        for i in range(len(digit_string) + 1)
        if len(digit_string) - i >= N
    )
