class Clock:
    def __init__(self, hour, minutes) -> None:
        """Create a clock."""
        self._raw_hour = hour
        self._raw_minutes = minutes
        self.hour = hour % 24
        self.minutes = self._cycle(minutes)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return str(self) == str(other)

    def __repr__(self) -> str:
        return f"Clock({self._raw_hour}, {self._raw_minutes})"

    def __str__(self) -> str:
        return "%02d:%02d" % (self.hour, self.minutes)

    def __add__(self, minutes: int) -> "Clock":
        self.minutes = self._cycle(self.minutes + minutes)
        return self

    def __sub__(self, minutes: int) -> "Clock":
        self.minutes = self._cycle(self.minutes - minutes)
        return self

    def _cycle(self, minutes: int) -> int:
        if minutes < 60 and minutes >= 0:
            return minutes

        if minutes < 0:
            self.hour -= 1
            self.hour %= 24
            return self._cycle(minutes + 60)

        self.hour += 1
        self.hour %= 24
        return self._cycle(minutes - 60)
