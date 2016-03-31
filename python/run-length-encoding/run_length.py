# -*- coding: utf-8 -*-
import re


def encode(string):
    letter_and_count = []
    current_letter_count = 0
    last_char_index = len(string) - 1

    for i, char in enumerate(string):
        previous_char = string[i - 1]
        if current_letter_count == 0:
            current_letter_count += 1
        if i != 0 and char == previous_char:
            current_letter_count += 1
        if i != last_char_index and char != string[i + 1]:
            letter_encoding = _write_encoding(current_letter_count, char)
            letter_and_count.append(letter_encoding)
            current_letter_count = 0
        elif i == last_char_index:
            letter_encoding = _write_encoding(current_letter_count, char)
            letter_and_count.append('{}'.format(letter_encoding))
    return ''.join(letter_and_count)


def decode(string):
    decoded_chars = []
    i = 0
    string_index_length = len(string)
    number = 0
    letter = None

    while i < string_index_length:
        current_char = string[i]
        if _is_number(current_char):
            number, letter = _split_encoded_unit(i, string)
            decoded_chars.append(letter * number)
            i += len(str(number)) + 1  # jump to the index of next encoded unit
        else:
            decoded_chars.append(current_char)
            i += 1
    return ''.join(decoded_chars)


def _write_encoding(count, letter):
    return '{}{}'.format(count, letter) if count > 1 else '{}'.format(letter)


def _split_encoded_unit(index, text, number_list=None):
    number_list = number_list or []
    current_char = text[index]

    if _is_number(current_char):
        number_list.append(current_char)
        return _split_encoded_unit(index + 1, text, number_list=number_list)
    else:
        number_segment = int(''.join(number_list))
        return number_segment, current_char


def _is_number(char):
    return re.search(r'\d', char) is not None
