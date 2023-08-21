def to_rna(dna_strand: str) -> str:
    """Convert a DNS strand to its RNA complement."""
    complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    return "".join(complements[nucleotide] for nucleotide in dna_strand)
