from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


NORTH, EAST, SOUTH, WEST = 1, 2, 4, 8
DELTA = {
    1: Point(0, 1),
    2: Point(1, 0),
    4: Point(0, -1),
    8: Point(-1, 0),
}


class Robot(object):
    """A robot capable of moving around a grid.

    Attributes:
        * bearing (int): numerical representation of the robot's
            orientation based on cardinal direction configuration.
    """
    def __init__(self, bearing=NORTH, *args):
        self.bearing = bearing
        self._coordinates = Point(*args) if args else Point(0, 0)

    @property
    def coordinates(self):
        """NamedTuple(Point, x, y): The robot's current coordinates on
        a 2-dimensional grid.
        """
        return self._coordinates

    def turn_left(self):
        """Uses bit manipulation to orient the robot."""
        self.bearing = (self.bearing << 3) % 15

    def turn_right(self):
        """Uses bit manipulation to orient the robot."""
        self.bearing = (self.bearing << 1) % 15

    def advance(self):
        """Moves robot's forward and updates its coordinates based on
        its bearing.
        """
        self._coordinates = self._coordinates._replace(
            x=(self._coordinates.x + DELTA[self.bearing].x),
            y=(self._coordinates.y + DELTA[self.bearing].y),
        )

    def simulate(self, path):
        """Moves the robot along the given path.

        `path` can be defined with combinations of three commands:
            * 'L': turn left
            * 'R': turn right
            * 'A': move forward one grid unit

        Args:
            * path (str): instructions for the robot's movement.
        """
        execute = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }
        for step in path:
            execute[step]()
