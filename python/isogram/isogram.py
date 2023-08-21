import re


NON_LETTERS = re.compile("[^a-zA-Z]")


def is_isogram(phrase: str) -> bool:
    """Returns True is phrase is isogrammatic.

    A phrase is isogrammatic if it doesn't use a letter more than once.

    Args:
        phrase (str): The phrase to check.

    Returns:
        bool: True if isogrammatic; otherwise, False.
    """
    letters = NON_LETTERS.sub("", phrase.lower())
    return len(letters) == len(set(letters))
