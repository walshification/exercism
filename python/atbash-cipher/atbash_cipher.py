import string
from typing import Mapping, Union


ENCODE_TABLE = str.maketrans(
    string.ascii_lowercase,  # original characters
    string.ascii_lowercase[::-1],  # encoded values
    string.punctuation + string.whitespace,  # remove this stuff
)
DECODE_TABLE = str.maketrans(
    string.ascii_lowercase[::-1], string.ascii_lowercase, string.whitespace
)


def encode(text: str) -> str:
    """Return an encoded message.

    The Atbash Cipher removes punctuation and evenly spaces characters
    in groups of five.

    :param text: str - the text to encode.
    :return: str - the encoded text.
    """
    chars = _translate(text, ENCODE_TABLE)
    return " ".join(chars[ch : ch + 5] for ch in range(0, len(chars), 5))


def decode(text: str) -> str:
    """Return text in English without spaces or punctuation.

    :param text: str - the text to decode.
    :return: str - the text, decoded.
    """
    return "".join(_translate(text, DECODE_TABLE))


def _translate(text, codex: Mapping[int, Union[int, None]]):
    """Apply table transformations to a text.

    :param text: str - the text to transform.
    :param codex: translation table - the mapping of transformations.
    :return: string
    """
    return text.lower().translate(codex)
