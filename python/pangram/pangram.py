import string


def is_pangram(text: str) -> bool:
    """Returns True is text is a pangram.

    A pangram is any sentence that contains all the letters of the
    English alphabet.

    Args:
        text (str): the sentence in question.

    Returns:
        bool: True if pangram; otherwise, False
    """
    text = text.lower()
    return all(c in text for c in string.ascii_lowercase)
