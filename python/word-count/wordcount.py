import re


def word_count(words):
    word_count = {}
    nominal_word = []
    characters = list(words.lower())
    for i, char in enumerate(characters):
        if re.search(r'[^\W_]', char) is not None:
            nominal_word.append(char)
            if (i + 1) == len(characters):
                filtered_word = ''.join(nominal_word)
                if filtered_word:
                    word_count[filtered_word] = word_count.get(filtered_word, 0) + 1
        else:
            filtered_word = ''.join(nominal_word)
            if filtered_word:
                word_count[filtered_word] = word_count.get(filtered_word, 0) + 1
            nominal_word = []
    return word_count
