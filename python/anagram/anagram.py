from typing import List


def find_anagrams(word: str, possible_anagrams: List[str]) -> List[str]:
    """Return a list of words that are anagrams of the given word.

    A word is an anagram if it can be created by rearranging a given
    word's letters, with no letters removed or added.

    :param word: str - the origin word for comparison.
    :param possible_anagrams: list - a list of possible anagrams for the word.
    :return: list - all anagrams of the word.
    """
    word = word.lower()
    letters = sorted(word.lower())
    return [
        possible_anagram
        for possible_anagram in possible_anagrams
        if word != possible_anagram.lower()
        and is_anagram(possible_anagram.lower(), letters)
    ]


def is_anagram(possible_anagram: str, letters: List[str]) -> bool:
    """Returns True if a possible anagram uses all of a set of letters.

    :param possible_anagram: str - a word.
    :param letters: list - a list of letters an anagram must use.
    :returns: bool - True if the possible anagram uses all the letters.
    """
    return sorted(possible_anagram) == letters
