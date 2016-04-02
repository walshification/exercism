import string


def is_pangram(text):
    for letter in string.ascii_lowercase:
        if letter not in text.lower():
            return False
    return True
