import datetime


def meetup_day(year, month, weekday, week):
    """Determine a meetup day from a year, month, day, and vague week.

    Args:
        * year (int): the year for the meetup.
        * month (int): the month for the meetup.
        * weekday (str): the day of the week for the meetup.
        * week (str): a vague delineater for which week the meetup
                      should happen on.

    Returns:
        * date: date object representation of the meetup day.

    Raises:
        * MeetupDayException: if the date doesn't exist (e.g. Feb 30).
    """
    intervals = {
        'teenth': 13,
        '1st': 1,
        '2nd': 8,
        '3rd': 15,
        '4th': 22,
        '5th': 29,
        'last': 22,
    }

    try:
        return _match_week(
            _match_day(
                datetime.date(year, month, intervals[week]),
                weekday),
            week,
        )
    except ValueError:
        raise MeetupDayException


def _match_day(date_obj, day):
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday')
    while weekdays[date_obj.weekday()] != day:
        date_obj += datetime.timedelta(days=1)
    return date_obj


def _match_week(date_obj, interval):
    if (date_obj.month != 2 and (interval == 'last' and date_obj.day < 25) or
            date_obj.month == 2 and __is_leap_year(date_obj.year)):
        date_obj += datetime.timedelta(days=7)
    return date_obj


def __is_leap_year(year):
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0


class MeetupDayException(Exception):
    pass
