def detect_anagrams(word, possible_anagrams):
    """Filters a list of words and returns a given word's anagrams.

    A word is an anagram if it can be created by rearranging a given
    word's letters, with no letters removed or added.

    Args:
        * word (str): the origin word for comparison.
        * possible_anagrams (list): a list of words to be filtered
                                    through `word`.

    Returns:
        * list: words that are anagrams of `word`.
    """
    return list(filter(lambda a: is_anagram(word.lower(), a.lower()),
                       possible_anagrams))


def is_anagram(word1, word2):
    """Determines if two words are anagrams.

    Args:
        * word1 (str): the first word.
        * word2 (str): the second word.

    Returns:
        * bool: True if anagram; otherwise, False.
    """
    return sorted(list(word1)) == sorted(list(word2)) and word1 != word2
