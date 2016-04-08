def sum_of_multiples(limit, numbers=(3, 5)):
    """Return the sum of the multiples of a particular set of numbers
    up to the limit.

    :param limit: the number up to which multiples are summed.
    :type limit: int
    :param numbers: (option) a list of numbers used to find the
                    multiples. Defaults to (3, 5).
    :type numbers: list, tuple

    :returns: sum of the multiples of the given numbers to the limit.
    :rtype: int
    """
    return sum(_unique(_multiples_of(_positive(numbers), limit)))


def _positive(numbers_list):
    return list(filter(lambda f: f > 0, numbers_list))


def _multiples_of(integers, bound):
    return [i for i in range(bound) for j in integers if i % j == 0]


def _unique(_list):
    return list(set(_list))
