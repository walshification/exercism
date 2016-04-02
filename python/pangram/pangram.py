import string


def is_pangram(text):
    """Determines if a sentence is a pangram or not.

    A pangram is any sentence that contains all the letters of the
    English alphabet.

    Args:
        text (str): the sentence in question.

    Returns:
        bool: True if pangram; otherwise, False
    """
    return all(map(lambda c: c in text.lower(), string.ascii_lowercase))
