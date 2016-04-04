def sieve(limit):
    # store the only even prime so I can skip all other even numbers
    primes = [2]
    composites = set()
    for j in range(3, limit + 1, 2):
        if j not in composites:
            primes.append(j)
        # Odd times an even is even, so only store multiples of odd pairs.
        for n in range(3, j + 1, 2):
            new_composite = n * j  # accounts for n up to j ** 2
            # Since we have a target, we can ignore everything higher.
            # This li'l break cut down on the calculations dramatically.
            if new_composite > limit:
                break
            composites.add(new_composite)
        composites.discard(j)  # keep the set small
    return primes
