def slices(digit_string, n):
    """Takes a string of digits and gives you all the contiguous
    substrings of length `n` in that string.
    """
    if n > len(digit_string) or n == 0:
        raise ValueError
    slice_list = []
    for i in range(len(digit_string) + 1):
        string_slice = digit_string[(0 + i):(n + i)]
        if len(digit_string) - i >= n:
            slice_list.append(list(int(s) for s in string_slice))
    return slice_list
