from typing import List


def primes(limit: int) -> List[int]:
    """Return a list of prime numbers up to the given limit.

    :param limit: int - the limit up to which we generate primes.
    :return: list - the generated primes.

    A prime number has no factors other than 1 and itself. A composite
    number is a number that is not prime.
    """
    if limit < 2:
        return []

    # store the only even prime so I can skip all other even numbers
    primes = [2]
    composites = set()

    # Run through odd numbers up to and including the limit.
    for j in range(3, limit + 1, 2):
        # If we haven't filtered j out, it must be prime.
        if j not in composites:
            primes.append(j)

        # 1 * j is the prime number.
        # 2 * j is always even and therefore never prime.
        # For the remaining numbers from 3 up to the square of the current prime ...
        for n in range(3, j**2, 2):
            # create a new composite by multiplying it by n.
            new_composite = n * j
            if new_composite > limit:
                # Past the limit, we don't care anymore.
                break

            if new_composite not in composites:
                composites.add(new_composite)

        # Keep the set small by removing composites that no longer matter.
        if j in composites:
            composites.remove(j)

    return primes
