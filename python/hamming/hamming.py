def distance(strand1, strand2):
    assert len(strand1) == len(strand2)
    return len(list(s for i, s in enumerate(strand1) if strand2[i] != s))
