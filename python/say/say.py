NUMBERS = {
    '00': '',
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
TENS = {
    '00': '',
    '0': '',
    '2': 'twenty-',
    '3': 'thirty-',
    '4': 'forty-',
    '5': 'fifty-',
    '6': 'sixty-',
    '7': 'seventy-',
    '8': 'eighty-',
    '9': 'ninety-',
}


def say(number):
    if number > 999999999999 or number < 0:
        raise AttributeError
    chunk_names = {
        0: '',
        1: ' thousand ',
        2: ' million ',
        3: ' billion ',
    }
    number = str(int(number))
    number_name = []
    number_chunks = _chunk_it(number)
    index = len(number_chunks)
    for chunk in number_chunks:
        translated_chunk = _translate(chunk)
        index -= 1
        if translated_chunk:
            number_name.append(translated_chunk)
        if translated_chunk and chunk_names[index]:
            number_name.append(chunk_names[index])
    return ''.join(number_name).strip()


def _chunk_it(int_string):
    chunks = []
    while int_string:
        chunks.insert(0, int_string[-3:])
        int_string = int_string[:-3]
    return chunks


def _translate(int_group):
    decimal_place = {
        3: _hundredify,
        2: _proper_ten,
        1: _number,
    }
    translation = []
    translation.extend(decimal_place[len(int_group)](int_group))
    return ''.join(translation)


def _hundredify(number_string):
    if number_string[0] == '0':
        hundred_chunk = ''
        if number_string[1:] != '00':
            hundred_chunk = 'and '
        return [hundred_chunk, _proper_ten(number_string[1:])]
    hundred_chunk = '{} hundred'.format(NUMBERS[number_string[0]])
    if number_string[1:] != '00':
        hundred_chunk += ' and '
    return [hundred_chunk, _proper_ten(number_string[1:])]


def _proper_ten(int_string):
    if int_string[0] == '1' and int_string not in NUMBERS:
        return (NUMBERS[int_string[1]], 'teen')
    elif int_string[0] == '1':
        return NUMBERS[int_string]
    elif int_string != '00':
        ten = TENS[int_string[0]]
        if int_string[-1] == '0':
            return ten[:-1]
        else:
            return '{}{}'.format(ten, NUMBERS[int_string[1]])
    elif int_string[0] == '0':
        return _proper_ten(int_string[1])
    return TENS[int_string]


def _number(int_string):
    return NUMBERS[int_string]
