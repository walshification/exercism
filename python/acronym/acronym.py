import re


UNWANTED_CHARACTERS = re.compile("[^a-zA-Z ']")


def abbreviate(text: str) -> str:
    """Return a text phrase's appropriate abbreviation."""
    # Clean text.
    text = UNWANTED_CHARACTERS.sub(" ", text)
    # Join and capitalize the first letter of each word.
    return "".join(word[0].upper() for word in text.split())
