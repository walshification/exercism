def to_rna(nucleotides):
    complements = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    return ''.join(complements[n] for n in nucleotides)
