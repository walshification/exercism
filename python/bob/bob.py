import re


def hey(what):
    """Returns a response when you say something to Bob.

    Args:
        * what (str): what you say to Bob.

    Returns:
        * str: 'Fine. Be that way!'
        * str: 'Sure.'
        * str: 'Whatever.'
        * str: 'Whoa, chill out!'
    """
    responses = (
        (is_blank, 'Fine. Be that way!'),
        (is_inquisitive, 'Sure.'),
        (is_numbers_or_statement, 'Whatever.'),
        (is_shouty, 'Whoa, chill out!'),
    )
    return next(response for prompt, response in responses if prompt(what))


def is_blank(text):
    return not text or _is_whitespace(text)


def is_inquisitive(text):
    return (not _is_allcaps(text)) and _ends_with_question_mark(text)


def is_numbers_or_statement(text):
    conditions = (
        _begins_with_whitespace,
        _is_numbers,
        _is_statement,
    )
    return any(filter(lambda c: c(text), conditions))


def is_shouty(text):
    conditions = (
        _is_forceful_question,
        _is_shouting_numbers,
        _is_allcaps_with_special_characters,
        _is_allcaps,
    )
    return any(filter(lambda c: c(text), conditions))


def _ends_with_question_mark(text):
    return re.search(r'.+[\?]{1}[ \t]*$', text) is not None


def _is_allcaps(text):
    return (text.upper() == text and
            (not _is_numbers(text[:-1])) and
            (re.search(r'^.*[!]*', text)))


def is_forceful(text):
    reg = re.compile(r'(?=A-Z){1}[a-z\b\s{1}]+|[\w{0,}\'\w{0,}\b\s{1}]+[!]{1}')
    return ((not _is_allcaps(text)) and
            re.search(reg, text) is not None)


def _is_numbers(text):
    reg = re.compile(r'^[0-9|,| ]*[^?]$')
    return re.search(reg, text) is not None


def _is_whitespace(text):
    return re.search(r'^[ \t]+$', text) is not None


def _begins_with_whitespace(text):
    return re.search(r'^[\s]+\S+$', text) is not None


def _is_shouting_numbers(text):
    return re.search(r'^[\d, ]+[\w]+[!]{1}$', text)


def _is_allcaps_with_special_characters(text):
    reg = re.compile(r'^A-Z+\W+\d+[!]+$')
    return re.search(reg, text) is not None


def _is_statement(text):
    reg = re.compile(r'(?=A-Z){1}[\w]*[ {1}]+|[\w{0,}\'\w{0,} {1}]+|\?*[.]{1}')
    return ((not _is_allcaps(text)) and
            re.search(reg, text) is not None)


def _is_forceful_question(text):
    return (_is_allcaps(text) and
            (not _is_numbers(text[:-1])) and
            re.search(r'.+[\?]{1}[ \t]*$', text) is not None)
