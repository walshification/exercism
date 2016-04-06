import string


def abbreviate(text):
    return ''.join([t for t in _capitalized(text) if t in string.ascii_uppercase])


def _capitalized(words):
    capital_words = []
    for i, char in enumerate(list(words)):
        if char == ':':
            break
        if words[i - 1] == ' ' or words[i - 1] == '-':
            capital_words.append(char.upper())
        else:
            capital_words.append(char)
    return ''.join(capital_words)
