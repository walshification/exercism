import string


def is_isogram(phrase):
    '''Checks if a phrase is isogrammatic, e.g. doesn't contain the
    same letter more than once.

    :param phrase: The phrase to check.
    :type phrase: str
    :returns: True if isogrammatic; otherwise, False.
    :rtype: bool
    '''
    phrase = phrase.lower()
    return all(phrase.count(c) <= 1 for c in phrase if c in string.ascii_lowercase)
