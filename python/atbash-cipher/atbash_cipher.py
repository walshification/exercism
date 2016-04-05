import string


ENCODE_TABLE = str.maketrans(
    string.ascii_lowercase,  # original characters
    string.ascii_lowercase[::-1],  # encoded values
    string.punctuation + string.whitespace,  # remove this stuff
)
DECODE_TABLE = str.maketrans(
    string.ascii_lowercase[::-1],
    string.ascii_lowercase,
    string.whitespace
)


def encode(raw_text):
    """Converts `raw_text` into an encoded message with punctuation
    removed, evenly spaced by every five characters.
    """
    return _pentaglob(_translate(raw_text, ENCODE_TABLE))


def decode(encoded_text):
    """Converts `encoded_text` back to English without spaces or
    punctuation.
    """
    return ''.join([_translate(encoded_text, DECODE_TABLE)])


def _translate(text, codex):
    return text.lower().translate(codex)


def _pentaglob(chars):
    return ' '.join([chars[ch:ch + 5] for ch in range(0, len(chars), 5)])
