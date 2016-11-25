class Clock(object):
    def __init__(self, hour, minutes):
        self.hour = hour % 24
        self.minutes = self._cycle(minutes)

    def __str__(self):
        return '%02d:%02d' % (self.hour, self.minutes)

    def add(self, minutes):
        self.minutes += minutes
        self.minutes = self._cycle(self.minutes)
        return self

    def _cycle(self, minutes):
        if minutes < 59 and minutes >= 0:
            return minutes
        if minutes < 0:
            self.hour -= 1
            self.hour %= 24
            return self._cycle(minutes + 60)
        self.hour += 1
        if self.hour > 23:
            self.hour %= 24
        return self._cycle(minutes - 60)
