import itertools
import re
import string


def abbreviate(text):
    """Return a ``text`` phrase's appropriate abbreviation."""
    return ''.join(filter(lambda t: t in string.ascii_uppercase,
                   _capitalized(_words_in(_title(text)))))


def _title(title_chars):
    """Return the title portion of a phrase without the subtitle."""
    return ''.join(itertools.takewhile(lambda ch: ch != ':', title_chars))


def _words_in(text_string):
    """Split a ``text_string`` into a list of separate words."""
    return re.split('\W', text_string)


def _capitalized(words):
    """Return a string of capitalized words."""
    return ''.join([_capitalize(word) for word in words if word])


def _capitalize(word):
    """Capitalize ``word`` and preserve any capital letters in word."""
    return '{}{}'.format(word[0].upper(), word[1:])
