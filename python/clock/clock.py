class Clock(object):
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def __str__(self):
        return '%02d:%02d' % (self.hour, self.minutes)
