from typing import List, Optional, Tuple


def encode(string: str) -> str:
    encodings = []
    letter_counts: List[int] = []
    cursor = 0

    while cursor < len(string):
        current_char = string[cursor]
        if not letter_counts:
            letter_counts.append(1)

        # If we are at the end of the string ...
        if cursor + 1 == len(string):
            # write the encoding.
            encodings.append(_write_encoding(sum(letter_counts), current_char))
        else:
            # If the next letter matches ...
            if current_char == string[cursor + 1]:
                # count it.
                letter_counts.append(1)
            else:
                # otherwise, write the current encoding values and clear the count.
                encodings.append(_write_encoding(sum(letter_counts), current_char))
                letter_counts = []

        cursor += 1

    return "".join(encodings)


def decode(string: str) -> str:
    decoded_chars = []
    i = 0
    string_index_length = len(string)
    letter = None

    while i < string_index_length:
        current_char = string[i]
        if current_char.isdigit():
            char_count, letter = _split_encoded_unit(i, string)
            decoded_chars.append(letter * char_count)
            i += len(str(char_count)) + 1  # jump to the index of next encoded unit
        else:
            decoded_chars.append(current_char)
            i += 1
    return "".join(decoded_chars)


def _write_encoding(count: int, letter: str) -> str:
    encoding = letter
    if count > 1:
        encoding = str(count) + letter
    return encoding


def _split_encoded_unit(
    index: int, text: str, number_list: Optional[List[str]] = None
) -> Tuple[int, str]:
    number_list = number_list or []
    current_char = text[index]

    if current_char.isdigit():
        number_list.append(current_char)
        return _split_encoded_unit(index + 1, text, number_list=number_list)
    else:
        char_count = int("".join(number_list))
        return char_count, current_char
