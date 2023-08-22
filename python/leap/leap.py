def leap_year(year: int) -> bool:
    """Returns True if year is a leap year in the Gregorian calendar.

    A year is a leap year if it meets the following conditions:
        * evenly divisible by 4
        * not evenly divisible by 100, unless ...
        * also evenly divisible by 400

    Args:
        * year (int): the year in question.

    Returns:
        * bool: True for leap year; otherwise, False.
    """
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
