def distance(strand1: str, strand2: str) -> int:
    """Return the Hamming Distance between two DNA strands.

    :param strand1: str - the first DNA strand to compare.
    :param strand2: str - the second DNA strand to compare.
    :return: int - the number of deviations between the strands.
    """
    if len(strand1) != len(strand2):
        raise ValueError("Strands must be of equal length.")
    return len([s2 for s1, s2 in zip(strand1, strand2) if s1 != s2])
