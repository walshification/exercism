from enum import Enum
from typing import Optional


class BobResponses(Enum):
    QUESTION = "Sure."
    YELLING = "Whoa, chill out!"
    YELLING_QUESTION = "Calm down, I know what I'm doing!"
    SILENCE = "Fine. Be that way!"
    DEFAULT = "Whatever."


def response(text: str) -> str:
    """Returns a response when you say something to Bob.

    Args:
        * text (str): what you say to Bob.

    Returns:
        * str: one of the BobResponses
    """
    text_processors = (
        is_silence,
        is_yelling_question,
        is_question,
        is_yelling,
    )
    text = text.strip()
    determination = BobResponses.DEFAULT.value
    for text_processor in text_processors:
        if new_determination := text_processor(text):
            determination = new_determination.value
            break

    return determination


def is_silence(text: str) -> Optional[BobResponses]:
    if not text:
        return BobResponses.SILENCE
    return None


def is_yelling_question(text: str) -> Optional[BobResponses]:
    if text.endswith("?") and text.isupper():
        return BobResponses.YELLING_QUESTION
    return None


def is_question(text: str) -> Optional[BobResponses]:
    if text.strip().endswith("?"):
        return BobResponses.QUESTION
    return None


def is_yelling(text: str) -> Optional[BobResponses]:
    if text.isupper():
        return BobResponses.YELLING
    return None
