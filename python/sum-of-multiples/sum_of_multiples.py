def sum_of_multiples(limit, factors=None):
    if limit < 2 or factors == [0]:
        return 0
    factors = factors or [3, 5]
    multiples = set()
    for factor in factors:
        if factor:
            for i in range(limit):
                if i % factor == 0:
                    multiples.add(i)
    return sum(multiples)
