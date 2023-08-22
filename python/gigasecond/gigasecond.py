from datetime import datetime, timedelta


def add(start: datetime) -> datetime:
    return start + timedelta(seconds=1000000000)
