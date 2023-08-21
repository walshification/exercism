from typing import Sequence


def sum_of_multiples(N: int, numbers: Sequence[int]) -> int:
    """Return the sum of the multiples of a set of numbers up to N.

    :param limit: int - the number up to which multiples are summed.
    :param numbers: sequence - a sequence of numbers.
    :returns: int - sum of the multiples of the given numbers up to N.
    """
    return sum(
        {factor for factor in range(N) for i in numbers if i and factor % i == 0}
    )
