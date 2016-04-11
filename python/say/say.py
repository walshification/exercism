def say(number):
    number = str(number)
    number_name = []
    number_chunks = _chunk_it(number)
    for chunk in number_chunks:
        number_name(_hundredify(chunk))


def _hundredify(int_group):
    numbers = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve'
    }
    translation = []
    for i in int_group:
        translation.append(translate(i))
    if len(int_group) == 2 and int_group[0] == '1' and int_group not in numbers:
        translation.extend((numbers[int_group[1]], 'teen'))
    elif len(int_group) == 2 and int_group[0] == '1':
        translation.append(numbers[int_group])
    elif len(int_group) == 2:
        ten = _proper_ten(int_group[0])
        if int_group[-1] == '0':
            translation.append(ten[:-1])
        else:
            translation.extend((ten, numbers[int_group[1]]))
    else:
        translation.append(numbers[int_group])
    return ''.join(translation)


def translate(single_number_string):
    pass


def _proper_ten(int_string):
    tens = {
        '2': 'twenty-',
        '3': 'thirty-',
        '4': 'forty-',
        '5': 'fifty-',
        '6': 'sixty-',
        '7': 'seventy-',
        '8': 'eighty-',
        '9': 'ninety-',
    }
    return tens[int_string]


def _chunk_it(int_string):
    chunks = []
    i = 0
    while i < len(int_string):
        chunks.append(int_string[-3:])
        i += 3
    return chunks
