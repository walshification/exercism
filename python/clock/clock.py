class Clock(object):
    def __init__(self, hour, minutes):
        self.hour = hour % 24
        self.minutes = self._cycle(minutes)

    def __str__(self):
        return '%02d:%02d' % (self.hour, self.minutes)

    def _cycle(self, minutes):
        if minutes < 59:
            return minutes
        self.hour += 1
        return self._cycle(minutes - 60)
