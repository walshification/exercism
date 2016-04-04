NORTH = 'North'
EAST = 'East'
SOUTH = 'South'
WEST = 'West'


class Robot(object):
    def __init__(self, bearing=NORTH, starting_x=0, starting_y=0):
        self.bearing = bearing
        self.x = starting_x
        self.y = starting_y
        self.coordinates = (self.x, self.y)

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == WEST:
            self.x -= 1
        self.coordinates = (self.x, self.y)

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == EAST:
            self.bearing = NORTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == WEST:
            self.bearing = SOUTH

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH

    def simulate(self, path):
        execute = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }
        for step in path:
            execute[step]()
