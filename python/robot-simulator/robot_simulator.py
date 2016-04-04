NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'


class Robot(object):
    def __init__(self, bearing=NORTH, starting_x=0, starting_y=0):
        self.bearing = bearing
        self.x = starting_x
        self.y = starting_y
        self.coordinates = (self.x, self.y)

    def turn_left(self):
        pivots = {
            NORTH: WEST,
            EAST: NORTH,
            SOUTH: EAST,
            WEST: SOUTH,
        }
        self.bearing = pivots[self.bearing]

    def turn_right(self):
        pivots = {
            NORTH: EAST,
            EAST: SOUTH,
            SOUTH: WEST,
            WEST: NORTH,
        }
        self.bearing = pivots[self.bearing]

    def advance(self):
        delta = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0),
        }
        self.x += delta[self.bearing][0]
        self.y += delta[self.bearing][1]
        self.coordinates = (self.x, self.y)

    def simulate(self, path):
        execute = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }
        for step in path:
            execute[step]()
