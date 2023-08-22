import datetime


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, weekday):
    """Determine a meetup day from a year, month, day, and vague week.

    :param year: int - the year for the meetup.
    :param month: int - the month for the meetup.
    :param week: str - a vague delineater for the week of the meetup.
    :param weekday: str - the day of the week for the meetup.

    :return: date - the meetup date.

    :raises MeetupDayException: That day does not exist.
    """
    intervals = {
        "teenth": 13,
        "first": 1,
        "second": 8,
        "third": 15,
        "fourth": 22,
        "fifth": 29,
        "last": 22,
    }

    try:
        approximate_day = datetime.date(year, month, intervals[week])
        refined_day = _match_day(approximate_day, weekday)
        return _match_week(refined_day, week)
    except ValueError:
        raise MeetupDayException("That day does not exist.")


def _match_day(approximate_day: datetime.date, day: str) -> datetime.date:
    weekdays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    while weekdays[approximate_day.weekday()] != day:
        approximate_day = datetime.date(
            approximate_day.year, approximate_day.month, approximate_day.day + 1
        )
    return approximate_day


def _match_week(date_obj: datetime.date, interval: int) -> datetime.date:
    if (
        date_obj.month != 2
        and (interval == "last" and date_obj.day < 25)
        or date_obj.month == 2
        and interval == "last"
        and is_leap_year(date_obj.year)
    ):
        date_obj += datetime.timedelta(days=7)
    return date_obj


def is_leap_year(year: int) -> bool:
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
