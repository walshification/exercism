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


def encode(text):
    return ' '.join(
        text.lower().translate(ENCODE_TABLE)[char:char + 5] for char in range(
            0, len(''.join(list(text.lower().translate(ENCODE_TABLE)))), 5
        )
    )


def decode(text):
    return ''.join(list(text.lower().translate(DECODE_TABLE)))
