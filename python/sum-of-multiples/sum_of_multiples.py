def sum_of_multiples(limit, numbers=(3, 5)):
    """Return the sum of the multiples of a particular set of numbers
    up to the limit.

    :param limit: the number up to which multiples are summed.
    :type limit: int
    :param numbers: (option) a list of numbers used to find the
                    multiples. Defaults to (3, 5).
    :type numbers: list, tuple

    :returns: the sum of the multiples.
    :rtype: int
    """
    return sum(set(i for f in filter(lambda f: f != 0, numbers)
                   for i in range(limit) if i % f == 0))
