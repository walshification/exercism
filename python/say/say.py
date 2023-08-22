import os
from typing import List


NUMBERS = {
    "00": "",
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
TENS = {
    "00": "",
    "0": "",
    "2": "twenty-",
    "3": "thirty-",
    "4": "forty-",
    "5": "fifty-",
    "6": "sixty-",
    "7": "seventy-",
    "8": "eighty-",
    "9": "ninety-",
}
NUMBER_GROUP_NAMES = {
    0: "",
    1: "thousand",
    2: "million",
    3: "billion",
}


def say(number: int, do_speak: bool = False) -> str:
    """Return the English equivalent of a number.

    :param number: int - the number to "say."
    :return: str
    """
    if number > 999999999999 or number < 0:
        raise ValueError("input out of range")

    number_str = str(number)
    number_groups = group_numbers(number_str)

    english_number = convert_to_english(number_groups)

    if do_speak:
        os.system(f"say '{english_number}'")

    return english_number


def group_numbers(int_string: str) -> List[str]:
    """Return numbers in a list grouped by three."""
    number_groups: List[str] = []
    while int_string:
        number_groups.insert(0, int_string[-3:])
        int_string = int_string[:-3]
    return number_groups


def convert_to_english(number_groups: List[str]) -> str:
    number_name = []
    cursor = len(number_groups) - 1  # Start at the end.
    for group in number_groups:
        if translated_group := _translate(group):
            number_name.append(translated_group)

            number_name.append(NUMBER_GROUP_NAMES[cursor])
        cursor -= 1

    return " ".join(number_name).strip()


def _translate(number: str) -> str:
    """Convert a number to English."""
    decimal_place = {
        3: _hundredify,
        2: _proper_ten,
        1: _number,
    }
    return " ".join(decimal_place[len(number)](number))


def _hundredify(number_string):
    if number_string[0] == "0":
        return _proper_ten(number_string[1:])
    hundred_chunk = ["{}".format(NUMBERS[number_string[0]]), "hundred"]
    return hundred_chunk + _proper_ten(number_string[1:])


def _proper_ten(int_string):
    if int_string[0] == "1":
        # 10-19 are idiosyncratic.
        return [NUMBERS[int_string]]

    ten = TENS[int_string[0]]
    if int_string[-1] == "0":
        # Remove the hyphen.
        return [ten[:-1]]

    return [ten + NUMBERS[int_string[1]]]


def _number(int_string):
    return [NUMBERS[int_string]]
